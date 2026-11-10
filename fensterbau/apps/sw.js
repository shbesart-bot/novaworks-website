/* ProFitAR & PassFort: App-Dateien offline verfügbar (Daten liegen in IndexedDB, nicht hier) */
const CACHE = 'fensterbau-2026-11-09b';
const SHELL = ['./profitar.html', './passfort.html', './konto.html', './pass.html', './planung.html', './angebot.html', './fb.css?v=2026-11-09b', './fb-core.js?v=2026-11-09b', './vendor/supabase.js', './vendor/jspdf.umd.min.js', './vendor/qrcode.min.js',
  './vendor/figtree-latin-400-normal.woff2', './vendor/figtree-latin-600-normal.woff2', './vendor/figtree-latin-700-normal.woff2', './icon-profitar.svg', './icon-passfort.svg', './icon-planung.svg'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('fensterbau-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  const html = e.request.mode === 'navigate' || u.pathname.endsWith('.html');
  if (html) { // Seiten: erst Netz, offline aus dem Speicher
    e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(CACHE).then(x => x.put(u.pathname.split('/').pop() ? './' + u.pathname.split('/').pop() : e.request, c)); return r; }).catch(() => caches.match('./' + u.pathname.split('/').pop()).then(r => r || caches.match('./profitar.html'))));
    return;
  }
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(res => { if (res.ok && /\/vendor\/|\.css|\.js|\.svg|\.png|\.woff2|\.ttf/.test(u.pathname)) { const c = res.clone(); caches.open(CACHE).then(x => x.put(e.request, c)); } return res; })));
});
