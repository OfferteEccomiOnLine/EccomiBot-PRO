
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
            asin_list = keepa.best_sellers_query(domain='IT', category=category_id)
            if not asin_list:
                print(f"❌ Nessun ASIN trovato per la categoria {name}")
                continue

            product_info = keepa.query(asin_list[:10], domain='IT')
            if not product_info or "products" not in product_info:
                print(f"❌ Nessun prodotto valido trovato per {name}")
                continue

            for product in product_info['products']:
                title = product.get("title", "Offerta Amazon")[:100]
                asin = product.get("asin")
                if asin and title:
                    url = f"https://www.amazon.it/dp/{asin}/?tag={AFFILIATE_TAG}"
                    products.append((name, title, url))
        except Exception as e:
            print(f"❌ Errore nella categoria {name}: {e}")
            continue

    return products[:MAX_PRODUCTS]

async def main():
    bot = Bot(token=TOKEN)
    deals = get_deals()
    if not deals:
        await bot.send_message(chat_id=CHANNEL, text="⚠️ Oggi nessuna super offerta trovata.\nTorna a trovarci più tardi! 💬")
        return

    for cat, title, url in deals:
        message = f"🔥 *{title}*\n📦 Categoria: _{cat}_\n🔗 [Scopri l'offerta su Amazon]({url})\n\n🌐 Powered by *Eccomi Online*"
        await bot.send_message(chat_id=CHANNEL, text=message, parse_mode='Markdown')

    print(f"✅ {len(deals)} offerte pubblicate con successo.")

if __name__ == "__main__":
    asyncio.run(main())
