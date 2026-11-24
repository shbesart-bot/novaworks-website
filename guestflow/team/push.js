// GuestFlow Team: Push anmelden/abmelden – wird aus Dart aufgerufen (window.gfPush…).
(function () {
  function b64ZuBytes(s) {
    var pad = '='.repeat((4 - s.length % 4) % 4);
    var raw = atob((s + pad).replace(/-/g, '+').replace(/_/g, '/'));
    var out = new Uint8Array(raw.length);
    for (var i = 0; i < raw.length; i++) out[i] = raw.charCodeAt(i);
    return out;
  }
  function reg() {
    return navigator.serviceWorker.register('push-sw.js', { scope: 'gf-push/' }).then(function (r) {
      return navigator.serviceWorker.ready.then(function () { return r; }, function () { return r; });
    });
  }
  function warteAktiv(r) {
    if (r.active) return Promise.resolve(r);
    return new Promise(function (ok) {
      var sw = r.installing || r.waiting;
      if (!sw) return ok(r);
      sw.addEventListener('statechange', function () { if (sw.state === 'activated') ok(r); });
      setTimeout(function () { ok(r); }, 5000);
    });
  }
  // Ergebnis: JSON {endpoint,p256dh,auth} oder Fehlertext mit Präfix "FEHLER:"
  window.gfPushStatus = function () {
    if (!('serviceWorker' in navigator) || !('PushManager' in window) || !('Notification' in window)) return Promise.resolve('nicht_unterstuetzt');
    if (Notification.permission === 'denied') return Promise.resolve('blockiert');
    return navigator.serviceWorker.getRegistration('gf-push/').then(function (r) {
      if (!r) return 'aus';
      return r.pushManager.getSubscription().then(function (s) { return s ? 'an' : 'aus'; });
    }).catch(function () { return 'aus'; });
  };
  window.gfPushAn = function (oeffentlich) {
    if (!('serviceWorker' in navigator) || !('PushManager' in window)) return Promise.resolve('FEHLER:Dieser Browser kann keine Benachrichtigungen. Auf dem iPhone: Seite zuerst „Zum Home-Bildschirm“ hinzufügen und von dort öffnen.');
    return Notification.requestPermission().then(function (p) {
      if (p !== 'granted') return 'FEHLER:Benachrichtigungen wurden nicht erlaubt. Bitte in den Browser-Einstellungen für diese Seite erlauben.';
      return reg().then(warteAktiv).then(function (r) {
        return r.pushManager.getSubscription().then(function (alt) {
          return alt || r.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: b64ZuBytes(oeffentlich) });
        });
      }).then(function (s) {
        var j = s.toJSON();
        return JSON.stringify({ endpoint: j.endpoint, p256dh: j.keys.p256dh, auth: j.keys.auth });
      });
    }).catch(function (e) { return 'FEHLER:' + (e && e.message ? e.message : e); });
  };
  window.gfPushAus = function () {
    return navigator.serviceWorker.getRegistration('gf-push/').then(function (r) {
      if (!r) return '';
      return r.pushManager.getSubscription().then(function (s) {
        if (!s) return '';
        var ep = s.endpoint;
        return s.unsubscribe().then(function () { return ep; });
      });
    }).catch(function () { return ''; });
  };
  window.gfPushTest = function (titel, text) {
    return navigator.serviceWorker.getRegistration('gf-push/').then(function (r) {
      if (r) return r.showNotification(titel, { body: text, icon: 'icons/Icon-192.png' }).then(function () { return 'ok'; });
      return 'aus';
    }).catch(function (e) { return 'FEHLER:' + e; });
  };
})();
