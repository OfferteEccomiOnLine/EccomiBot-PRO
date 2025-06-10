import keepa
from telegram import Bot
import time
import os

# --- CONFIG DA ENV ---
KEEPA_API_KEY = os.getenv("KEEPA_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")
AFFILIATE_TAG = os.getenv("AFFILIATE_TAG")
MAX_PRODUCTS = 3

# --- CONNESSIONE ---
api = keepa.Keepa(KEEPA_API_KEY)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# --- CATEGORIE SCELTE ---
category_ids = [
    412609031,   # Games
    6198167031,  # Cura della persona
    6198052031   # Casa e cucina
]

# --- CERCA PRIMA CATEGORIA DISPONIBILE ---
products = []
for cat_id in category_ids:
    asin_list = api.best_sellers_query(domain='IT', category=cat_id)
    if asin_list:
        print(f"✅ Categoria trovata: {cat_id}")
        products = api.query(asin_list[:10], domain='IT')
        break

if not products:
    print("❌ Nessuna categoria ha restituito risultati.")
    exit()

# --- PUBBLICAZIONE SU TELEGRAM ---
sent = 0

for product in products:
    if 'title' not in product or 'asin' not in product:
        continue

    asin = product['asin']
    title = product['title'].replace("*", "").replace("_", "")
    url = f"https://www.amazon.it/dp/{asin}/?tag={AFFILIATE_TAG}"
    message = f"🔥 {title[:100]}...\n👉 Scopri su Amazon: {url}"
    
    try:
        bot.send_message(
            chat_id=TELEGRAM_CHANNEL,
            text=message
        )
        print(f"✅ Inviato: {title}")
        sent += 1
        time.sleep(2)
    except Exception as e:
        print(f"❌ Errore: {e}")

    if sent >= MAX_PRODUCTS:
        break

print("🎉 EccomiBot ha pubblicato le offerte con successo.")
