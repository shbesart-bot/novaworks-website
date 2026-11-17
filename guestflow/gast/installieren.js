// Hinweis „Zum Startbildschirm hinzufügen“ für die Gäste-App im Browser.
(function () {
  var standalone = (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) || window.navigator.standalone;
  if (standalone) return;
  var KEY = 'gf-install-aus';
  try { var aus = Number(localStorage.getItem(KEY) || 0); if (aus && Date.now() - aus < 30 * 86400000) return; } catch (e) {}
  var de = (navigator.language || 'de').toLowerCase().indexOf('de') === 0;
  var T = de
    ? { titel: 'GuestFlow als App', text: 'Zum Startbildschirm hinzufügen – dann ist alles mit einem Tipp da.', knopf: 'Hinzufügen', ios: 'Tippen Sie unten auf <b>Teilen</b> (□↑) und dann auf <b>„Zum Home-Bildschirm“</b>.' }
    : { titel: 'Get GuestFlow as an app', text: 'Add it to your home screen for one-tap access.', knopf: 'Add', ios: 'Tap <b>Share</b> (□↑) at the bottom, then <b>“Add to Home Screen”</b>.' };
  var ua = navigator.userAgent || '';
  var ios = /iphone|ipad|ipod/i.test(ua) && /safari/i.test(ua) && !/crios|fxios/i.test(ua);
  var ereignis = null;
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); ereignis = e; });

  function zeigen() {
    if (!ereignis && !ios) return;
    if (document.getElementById('gf-install')) return;
    var box = document.createElement('div');
    box.id = 'gf-install';
    box.style.cssText = 'position:fixed;left:12px;right:12px;bottom:12px;z-index:2147483646;background:#fff;color:#1f2a44;' +
      'font:14px/1.4 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;border-radius:14px;box-shadow:0 8px 30px rgba(0,0,0,.25);' +
      'padding:14px 14px 14px 16px;display:flex;gap:12px;align-items:center;max-width:520px;margin:0 auto;';
    var img = document.createElement('img');
    img.src = 'icons/Icon-192.png'; img.width = 44; img.height = 44; img.style.borderRadius = '10px';
    var txt = document.createElement('div');
    txt.style.flex = '1';
    txt.innerHTML = '<b>' + T.titel + '</b><br>' + (ios ? T.ios : T.text);
    box.appendChild(img); box.appendChild(txt);
    if (!ios) {
      var ok = document.createElement('button');
      ok.textContent = T.knopf;
      ok.style.cssText = 'background:#4f8cff;color:#fff;border:0;border-radius:8px;padding:9px 12px;font:inherit;font-weight:600;cursor:pointer;';
      ok.onclick = function () { box.remove(); if (ereignis) { ereignis.prompt(); ereignis = null; } };
      box.appendChild(ok);
    }
    var x = document.createElement('button');
    x.textContent = '×'; x.setAttribute('aria-label', 'Schließen');
    x.style.cssText = 'background:none;border:0;font-size:22px;line-height:1;color:#8a92a6;cursor:pointer;padding:4px;';
    x.onclick = function () { box.remove(); try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {} };
    box.appendChild(x);
    document.body.appendChild(box);
  }
  // erst nach einer Weile zeigen, damit der Gast die App schon gesehen hat
  setTimeout(zeigen, 25000);
})();
