
import asyncio
from telegram import Bot
import os

async def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHANNEL = os.getenv("TELEGRAM_CHANNEL")

    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL, text="🚀 TEST OK: EccomiBot è attivo e funzionante!")
    print("✅ Messaggio di test inviato correttamente.")

if __name__ == "__main__":
    asyncio.run(main())
