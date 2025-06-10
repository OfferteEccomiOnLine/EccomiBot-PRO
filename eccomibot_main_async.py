
import asyncio
import os
from telegram import Bot
from keepa import Keepa
import random

# Config
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")
KEEPA_API_KEY = os.getenv("KEEPA_API_KEY")
AFFILIATE_TAG = "eol0a2-21"
MAX_PRODUCTS = 3

CATEGORIES_FULL = {
    "Elettronica": 473452031,
    "Informatica": 425916031,
    "Accessori smartphone": 473453031,
    "Piccoli elettrodomestici": 508065031,
    "Giochi e console": 468642,
    "Cura della persona": 6198092031,
    "Casa e cucina": 6198083031
}

def get_deals():
    keepa = Keepa(KEEPA_API_KEY)
    selected_categories = random.sample(list(CATEGORIES_FULL.items()), 2)
    products = []

    for name, category_id in selected_categories:
        print(f"🔍 Categoria in evidenza: {name}")
        try:
            result = keepa.category_search(category=category_id, domain='IT', page=0)
            for p in result['products']:
                try:
                    asin = p['asin']
                    title = p['title'][:100] + ("..." if len(p['title']) > 100 else "")
                    url = f"https://www.amazon.it/dp/{asin}/?tag={AFFILIATE_TAG}"
                    products.append((name, title, url))
                except:
                    continue
        except Exception as e:
            print(f"❌ Errore: {e}")
            continue

    return products[:MAX_PRODUCTS]

async def main():
    bot = Bot(token=TOKEN)
    deals = get_deals()
    if not deals:
        await bot.send_message(chat_id=CHANNEL, text="⚠️ Oggi nessuna super offerta trovata.
Torna a trovarci più tardi! 💬")
        return

    for cat, title, url in deals:
        message = f"🔥 *{title}*
📦 Categoria: _{cat}_
🔗 [Clicca qui per l'offerta]({url})

🌐 Powered by *Eccomi Online*"
        await bot.send_message(chat_id=CHANNEL, text=message, parse_mode='Markdown')

    print(f"✅ {len(deals)} offerte pubblicate con successo.")

if __name__ == "__main__":
    asyncio.run(main())
