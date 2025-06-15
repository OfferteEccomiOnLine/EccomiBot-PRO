from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7543112786:AAEpZera3CnPtiLPrA4DvYr35IdssAf3-XM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Eccomi! Sono attivo e pronto a pubblicare offerte 🔥")

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Ecco la tua offerta manuale! (DEMO)")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))
    app.run_polling()
