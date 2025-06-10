
import asyncio
import os
from telegram import Bot
from keepa import Keepa
import datetime

# Configurazioni
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")
KEEPA_API_KEY = os.getenv("KEEPA_API_KEY")
CATEGORIES = {
    "Games": 468642,
    "Cura della persona": 6198092031,
    "Casa e cucina": 6198083031
}
MAX_PRODUCTS = 3  # per ogni esecuzione
AFFILIATE_TAG = "eol0a2-21"

# Funzione per ottenere prodotti scontati da Keepa
def get_deals():
    keepa = Keepa(KEEPA_API_KEY)
    products = []

    for name, category_id in CATEGORIES.items():
        print(f"🔍 Scansione: {name}")
        deals = keepa.query(
            category=category_id,
            domain='IT',
            product_code=None,
            page=0,
            per_page=10,
            stats=180,
            history=False
        )
        for p in deals:
            try:
                price = p['buyBoxSellerIdHistory'][-1]
                if price:
                    asin = p['asin']
                    title = p['title'][:100] + ("..." if len(p['title']) > 100 else "")
                    url = f"https://www.amazon.it/dp/{asin}/?tag={AFFILIATE_TAG}"
                    products.append((title, url))
            except:
                continue
    return products[:MAX_PRODUCTS]

# Funzione di invio messaggio Telegram
async def main():
    bot = Bot(token=TOKEN)
    deals = get_deals()
    if not deals:
        await bot.send_message(chat_id=CHANNEL, text="❌ Nessuna offerta trovata al momento.")
        return

    for title, url in deals:
        message = f"🔥 *{title}*\n🔗 [Acquista ora]({url})"
        await bot.send_message(chat_id=CHANNEL, text=message, parse_mode='Markdown')

    print(f"✅ {len(deals)} offerte inviate!")

if __name__ == "__main__":
    asyncio.run(main())
