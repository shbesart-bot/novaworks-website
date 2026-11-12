// GuestFlow: Hinweis auf neue Version.
// Beim Bauen schreibt GuestFlow-live-bauen.ps1 eine Build-Nummer in index.html
// (meta gf-build) und in build.txt. Ist build.txt auf dem Server neuer als die
// geladene Seite, erscheint unten ein Hinweis mit "Jetzt aktualisieren".
(function () {
  var meta = document.querySelector('meta[name="gf-build"]');
  var mine = meta ? meta.content : '';
  if (!mine || mine.indexOf('__') === 0) return; // lokaler Test-Build
  var base = document.baseURI;
  var box = null, snoozeUntil = 0, busy = false;

  function check() {
    if (box || busy || Date.now() < snoozeUntil) return;
    busy = true;
    fetch(new URL('build.txt?t=' + Date.now(), base).toString(), { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.text() : ''; })
      .then(function (t) { t = (t || '').trim(); if (t && t !== mine) show(); })
      .catch(function () {})
      .then(function () { busy = false; });
  }

  function show() {
    box = document.createElement('div');
    box.setAttribute('role', 'alert');
    box.style.cssText = 'position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:2147483647;' +
      'background:#1f2a44;color:#fff;font:15px/1.4 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;' +
      'padding:14px 16px;border-radius:12px;box-shadow:0 8px 30px rgba(0,0,0,.3);display:flex;gap:12px;' +
      'align-items:center;flex-wrap:wrap;max-width:calc(100vw - 32px);';
    var txt = document.createElement('span');
    txt.innerHTML = '<b>Neue Version verf\u00fcgbar.</b> Bitte aktualisieren, damit alles richtig funktioniert.';
    var ok = document.createElement('button');
    ok.textContent = 'Jetzt aktualisieren';
    ok.style.cssText = 'background:#4f8cff;color:#fff;border:0;border-radius:8px;padding:9px 14px;font:inherit;font-weight:600;cursor:pointer;';
    var later = document.createElement('button');
    later.textContent = 'Sp\u00e4ter';
    later.style.cssText = 'background:transparent;color:#cfd6e6;border:0;padding:9px 6px;font:inherit;cursor:pointer;';
    ok.onclick = function () { ok.disabled = true; later.style.display = 'none'; ok.textContent = 'Wird aktualisiert \u2026'; update(); };
    later.onclick = function () { box.remove(); box = null; snoozeUntil = Date.now() + 30 * 60 * 1000; };
    box.appendChild(txt); box.appendChild(ok); box.appendChild(later);
    document.body.appendChild(box);
  }

  function update() {
    var jobs = [];
    if ('serviceWorker' in navigator) {
      jobs.push(navigator.serviceWorker.getRegistrations().then(function (rs) {
        return Promise.all(rs.map(function (r) { return r.unregister(); }));
      }));
    }
    if (window.caches) {
      jobs.push(caches.keys().then(function (ks) { return Promise.all(ks.map(function (k) { return caches.delete(k); })); }));
    }
    // Browser-Zwischenspeicher mit den neuen Dateien \u00fcberschreiben
    ['index.html', 'flutter_bootstrap.js', 'flutter.js', 'main.dart.js', 'update_check.js'].forEach(function (f) {
      jobs.push(fetch(new URL(f, base).toString(), { cache: 'reload' }).catch(function () {}));
    });
    Promise.all(jobs).catch(function () {}).then(function () {
      var u = new URL(location.href);
      u.searchParams.set('v', Date.now());
      location.replace(u.toString());
    });
  }

  setTimeout(check, 5000);
  setInterval(check, 5 * 60 * 1000);
  document.addEventListener('visibilitychange', function () { if (!document.hidden) check(); });
})();
