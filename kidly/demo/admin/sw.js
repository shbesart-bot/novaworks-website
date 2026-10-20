// Service Worker für Kidly Admin als installierbare PWA (Progressive Web App).
//
// Warum eine PWA statt einer nativen App für das Admin-Dashboard: anders als
// Kidly Family/Team (siehe eas.json in eltern-app/erzieher-app) richtet sich
// Kidly Admin an Träger/Leitung, die es meist am Rechner nutzen, aber auch
// unterwegs auf dem Handy aufrufen wollen - ohne App-Store-Review-Prozess.
// "Zum Home-Bildschirm hinzufügen" installiert es trotzdem dauerhaft mit
// eigenem Icon, eigenem Fenster (kein Browser-Rahmen) und funktioniert auch
// bei schlechter Verbindung mit einer Offline-Hinweisseite statt eines
// nackten Browser-Fehlers.
//
// Absichtlich EINFACH gehalten (kein Workbox/next-pwa) - für einen
// Prototyp reicht eine klare, nachvollziehbare Strategie:
//   - Navigationen (Seitenaufrufe): Netzwerk zuerst, bei Fehler zurück auf
//     die zuletzt im Cache liegende Version, sonst die Offline-Seite.
//   - Statische Next.js-Assets (/_next/static/...): Cache-zuerst, die sind
//     inhaltsadressiert (Hash im Dateinamen) und ändern sich nie nachträglich.
//   - ALLES andere (insbesondere API-Aufrufe ans Backend, anderer Origin):
//     unangetastet durchreichen, NICHT cachen - Personendaten/Anwesenheit/
//     Rechnungen etc. müssen immer frisch vom Server kommen, ein veralteter
//     Cache-Stand wäre hier fachlich falsch, nicht nur unbequem.

const CACHE_VERSION = 'kidly-admin-v2';
const OFFLINE_URL = '/offline.html';
const APP_SHELL = [OFFLINE_URL, '/icon-192.png', '/icon-512.png', '/manifest.webmanifest'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION).then((cache) => cache.addAll(APP_SHELL)).then(() => self.skipWaiting()),
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((key) => key !== CACHE_VERSION).map((key) => caches.delete(key))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return; // POST/PATCH/DELETE (Formulare, API-Schreibzugriffe) unangetastet lassen.

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return; // Backend-API (anderer Origin) nie abfangen.

  // Seitenaufruf/Navigation - Netzwerk zuerst (immer aktuelle Version, wenn
  // online), Cache als Rückfallebene, Offline-Seite als letzte Instanz.
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(CACHE_VERSION).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request).then((cached) => cached || caches.match(OFFLINE_URL))),
    );
    return;
  }

  // Inhaltsadressierte Next.js-Build-Assets - Cache-zuerst, danach Netzwerk.
  if (url.pathname.startsWith('/_next/static/')) {
    event.respondWith(
      caches.match(request).then(
        (cached) =>
          cached ||
          fetch(request).then((response) => {
            const copy = response.clone();
            caches.open(CACHE_VERSION).then((cache) => cache.put(request, copy));
            return response;
          }),
      ),
    );
  }
});
