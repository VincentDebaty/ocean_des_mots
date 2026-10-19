// Offline support: the game shell comes from the network when possible (to get updates), from the cache otherwise.
const CACHE = 'odm-v6';
const SHELL = ['./', 'index.html', 'manifest.webmanifest', 'firebase-config.js', 'icons/icon-192.png', 'icons/apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.hostname === 'firestore.googleapis.com') return; // Firestore manages its own offline cache
  const store = res => { if (res && (res.ok || res.type === 'opaque')) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); } return res; };
  if (url.origin === location.origin) {
    e.respondWith(fetch(req).then(store).catch(() => caches.match(req).then(r => r || caches.match('index.html'))));
  } else if (/(^|\.)gstatic\.com$|^fonts\.googleapis\.com$/.test(url.hostname)) {
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(store)));
  }
});
