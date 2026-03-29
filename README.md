# 📺 IPTV Playlist Auto-Updater

Playlist italiana aggiornata automaticamente ogni giorno tramite GitHub Actions.

## 📡 URL della Playlist

```
https://raw.githubusercontent.com/TUO_USERNAME/TUO_REPO/main/playlist.m3u
```

> Sostituisci `TUO_USERNAME` e `TUO_REPO` con i tuoi dati GitHub.

## 📋 Canali inclusi

| Canale | Gruppo |
|--------|--------|
| Eurosport 1 IT | Sport |
| Eurosport 2 IT | Sport |
| Milan TV | Sport |
| Inter TV | Sport |
| Sky Sport Max IT | Sky Sport |
| Sky Sport Mix IT | Sky Sport |
| Sky Sport Basket IT | Sky Sport |
| Sky Sports Arena IT | Sky Sport |
| Sky Sport 24 IT | Sky Sport |
| Sky Sport Calcio IT | Sky Sport |
| Zona DAZN IT | DAZN |
| Sky Sport Moto GP IT | Sky Sport |
| Sky Sport Golf IT | Sky Sport |
| Sky Sport Tennis IT | Sky Sport |
| Sky Sport F1 IT | Sky Sport |
| Sky Sport Uno IT | Sky Sport |

## 🚀 Setup

1. Crea un nuovo repo su GitHub
2. Carica tutti questi file mantenendo la struttura delle cartelle
3. Vai su **Settings → Actions → General** e assicurati che i workflow abbiano i permessi di scrittura:
   - Spunta **"Read and write permissions"**
4. Il workflow parte automaticamente ogni giorno alle 06:00 UTC
5. Puoi avviarlo manualmente da **Actions → Update IPTV Playlist → Run workflow**

## 🔧 Aggiornamento manuale

Vai su GitHub → tab **Actions** → **Update IPTV Playlist** → **Run workflow**

## 📱 Compatibile con

- Kodi (plugin PVR IPTV Simple Client)
- VLC
- TiviMate
- Qualsiasi player che supporta playlist `.m3u`
