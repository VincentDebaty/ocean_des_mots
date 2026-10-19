# L'Océan des Mots

Jeu d'orthographe pour enfants, pensé pour iPhone et iPad : dictée, pendu, anagramme, mémoire flash, bulles et phrases à trous, avec médailles, records, badges et une tortue qui grandit.

- `game.html` : le jeu (une seule page, sans dépendance).
- `build.py` : génère `index.html`, la version web-app plein écran (`python3 build.py`).
- `firebase-config.js` : configuration Firebase publique. Les données sont rangées sous un code famille secret.
- `sw.js`, `manifest.webmanifest`, `icons/` : installation sur l'écran d'accueil et mode hors ligne.

Sur iPhone : ouvrir le site dans Safari, Partager, « Sur l'écran d'accueil ».
