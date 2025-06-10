
from telegram import Bot
import os

# Leggi variabili d'ambiente
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

# Inizializza il bot
bot = Bot(token=TOKEN)

# Messaggio di test personalizzato
test_message = "🚀 TEST DI INVIO: EccomiBot è attivo, Telegram e Render collegati correttamente."

# Invia il messaggio al canale
bot.send_message(chat_id=CHANNEL, text=test_message)

print("✅ Messaggio di test inviato con successo.")
