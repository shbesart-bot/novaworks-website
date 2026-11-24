// GuestFlow Team: Push-Benachrichtigungen (eigener Service Worker, getrennt von Flutter).
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });

self.addEventListener('push', function (e) {
  var d = {};
  try { d = e.data ? e.data.json() : {}; } catch (_) { d = { titel: 'GuestFlow', text: e.data ? e.data.text() : '' }; }
  var sos = d.kategorie === 'sos';
  e.waitUntil(self.registration.showNotification(d.titel || 'GuestFlow Team', {
    body: d.text || '',
    icon: new URL('../icons/Icon-192.png', self.registration.scope).toString(),
    badge: new URL('../icons/Icon-192.png', self.registration.scope).toString(),
    tag: d.tag || d.kategorie || 'gf',
    renotify: true,
    requireInteraction: sos,
    vibrate: sos ? [400, 150, 400, 150, 400] : [150],
    data: { url: d.url || '/' }
  }));
});

self.addEventListener('notificationclick', function (e) {
  e.notification.close();
  var basis = new URL('../', self.registration.scope).toString();
  var ziel = basis + '#' + ((e.notification.data && e.notification.data.url) || '/');
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function (fenster) {
    for (var i = 0; i < fenster.length; i++) {
      if (fenster[i].url.indexOf(basis) === 0 && 'focus' in fenster[i]) {
        fenster[i].navigate ? fenster[i].navigate(ziel) : null;
        return fenster[i].focus();
      }
    }
    return self.clients.openWindow(ziel);
  }));
});
