import re
import time
from playwright.sync_api import sync_playwright

CHANNELS = [
    # numero = numero canale (LCN), name = nome che appare nel player
    {"number": 1,  "name": "Sky Sport Uno IT",    "url": "https://www.freeshot.live/live-tv/sky-sport-uno-it/26",     "logo": "https://www.freeshot.live/upload/source/sky-sport-uno-logo.png",     "group": "Sky Sport"},
    {"number": 2,  "name": "Sky Sport Calcio IT", "url": "https://www.freeshot.live/live-tv/sky-sport-calcio-it/382", "logo": "https://www.freeshot.live/upload/source/SkySportCalcio-logo.png",    "group": "Sky Sport"},
    {"number": 3,  "name": "Sky Sport F1 IT",     "url": "https://www.freeshot.live/live-tv/sky-sport-f1-it/27",      "logo": "https://www.freeshot.live/upload/source/sky-sport-F1-logo.png",      "group": "Sky Sport"},
    {"number": 4,  "name": "Sky Sport Moto GP IT","url": "https://www.freeshot.live/live-tv/sky-sport-moto-gp-it/350","logo": "https://www.freeshot.live/upload/source/sky_sport_motogp_logo.png",  "group": "Sky Sport"},
    {"number": 5,  "name": "Sky Sport Tennis IT", "url": "https://www.freeshot.live/live-tv/sky-sport-tennis-it/318", "logo": "https://www.freeshot.live/upload/source/Sky-sport-tennis.png",       "group": "Sky Sport"},
    {"number": 6,  "name": "Sky Sport Golf IT",   "url": "https://www.freeshot.live/live-tv/sky-sport-golf-it/346",   "logo": "https://www.freeshot.live/upload/source/SkySportGolfIT-logo.png",    "group": "Sky Sport"},
    {"number": 7,  "name": "Sky Sport Basket IT", "url": "https://www.freeshot.live/live-tv/sky-sport-basket-it/493", "logo": "https://www.freeshot.live/upload/source/sky-sport-basket-logo.png",  "group": "Sky Sport"},
    {"number": 8,  "name": "Sky Sport Max IT",    "url": "https://www.freeshot.live/live-tv/sky-sport-max-it/715",    "logo": "https://www.freeshot.live/upload/source/Sky-Sport-Max-logo.png",     "group": "Sky Sport"},
    {"number": 9,  "name": "Sky Sport Mix IT",    "url": "https://www.freeshot.live/live-tv/sky-sport-mix-it/700",    "logo": "https://www.freeshot.live/upload/source/Sky-Sport-Mix-logo.png",     "group": "Sky Sport"},
    {"number": 10, "name": "Sky Sports Arena IT", "url": "https://www.freeshot.live/live-tv/sky-sports-arena-it/384", "logo": "https://www.freeshot.live/upload/source/Sky_Sport_Arena-Logo.png",   "group": "Sky Sport"},
    {"number": 11, "name": "Sky Sport 24 IT",     "url": "https://www.freeshot.live/live-tv/sky-sport-24-it/383",     "logo": "https://www.freeshot.live/upload/source/SkySport24-logo.png",        "group": "Sky Sport"},
    {"number": 12, "name": "Zona DAZN IT",        "url": "https://www.freeshot.live/live-tv/zona-dazn-it/351",        "logo": "https://www.freeshot.live/upload/source/ZonaDAZN-logo.png",          "group": "DAZN"},
    {"number": 13, "name": "Eurosport 1 IT",      "url": "https://www.freeshot.live/live-tv/eurosport-1-it/763",      "logo": "https://www.freeshot.live/upload/source/Eurosport_1_logo.png",       "group": "Sport"},
    {"number": 14, "name": "Eurosport 2 IT",      "url": "https://www.freeshot.live/live-tv/eurosport-2-it/764",      "logo": "https://www.freeshot.live/upload/source/Eurosport_2_logo.png",       "group": "Sport"},
    {"number": 15, "name": "Milan TV",            "url": "https://www.freeshot.live/live-tv/milan-tv/721",            "logo": "https://www.freeshot.live/upload/source/Milan-TV-logo.png",          "group": "Sport"},
    {"number": 16, "name": "Inter TV",            "url": "https://www.freeshot.live/live-tv/inter-tv/775",            "logo": "https://www.freeshot.live/upload/source/InterTV-logo.png",           "group": "Sport"},
]

def get_stream_url(browser, page_url, channel_name):
    stream_url = None
    page = browser.new_page()

    def on_request(request):
        nonlocal stream_url
        if ".m3u8" in request.url and stream_url is None:
            print(f"  ✅ Trovato: {request.url}")
            stream_url = request.url

    page.on("request", on_request)

    try:
        page.goto(page_url, wait_until="networkidle", timeout=30000)
        # Aspetta un po' in più nel caso il player sia lento
        page.wait_for_timeout(5000)
    except Exception as e:
        print(f"  ⚠️  Timeout/errore per {channel_name}: {e}")
    finally:
        page.close()

    return stream_url

def build_m3u(entries):
    lines = ["#EXTM3U"]
    for ch, url in entries:
        if url:
            lines.append(
                f'#EXTINF:-1 tvg-chno="{ch["number"]}" tvg-logo="{ch["logo"]}" group-title="{ch["group"]}",{ch["name"]}'
            )
            lines.append(url)
        else:
            print(f"  ❌ Nessun link trovato per {ch['name']}")
    return "\n".join(lines) + "\n"

def main():
    entries = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for ch in CHANNELS:
            print(f"🔍 Cerco stream per: {ch['name']}")
            url = get_stream_url(browser, ch["url"], ch["name"])
            entries.append((ch, url))
            time.sleep(2)  # pausa tra un canale e l'altro

        browser.close()

    m3u_content = build_m3u(entries)

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    found = sum(1 for _, u in entries if u)
    print(f"\n✅ playlist.m3u aggiornata: {found}/{len(CHANNELS)} canali trovati")

if __name__ == "__main__":
    main()
