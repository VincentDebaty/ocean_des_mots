"""Build index.html (full-screen web app) from game.html, the same page published as a Claude artifact."""
import pathlib, re

root = pathlib.Path(__file__).parent
game = (root / 'game.html').read_text()

# The artifact starts with its title, a Claude-only meta tag and the font links: move them into <head>.
cut = game.index('<style>')
top, body = game[:cut], game[cut:]
title = re.search(r'<title>.*?</title>', top).group(0)
fonts = '\n'.join(re.findall(r'<link [^>]*>', top))

head = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{title}
<meta name="description" content="Jeu d'orthographe : dictée, pendu, anagramme, mémoire flash, bulles et phrases à trous.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Océan des Mots">
<meta name="theme-color" content="#55cddd">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
{fonts}
<style>:root{{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>
<script src="firebase-config.js"></script>
</head>
<body>
'''
tail = '''
<script>if ('serviceWorker' in navigator) addEventListener('load', () => navigator.serviceWorker.register('sw.js'));</script>
</body>
</html>
'''
(root / 'index.html').write_text(head + body + tail)
print('index.html built')
