
from telegram import Bot
import os

# Leggi i dati dalle variabili d'ambiente
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")

# Inizializza il bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Messaggio di conferma test
message = "✅ EccomiBot è attivo e collegato correttamente! 🔥 (TEST OK)"

# Invia il messaggio
bot.send_message(chat_id=TELEGRAM_CHANNEL, text=message)

print("✅ Test di conferma inviato con successo.")
