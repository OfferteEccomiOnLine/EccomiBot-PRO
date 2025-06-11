
import asyncio
import time
from keepa import Keepa
import logging

# Setup log
logging.basicConfig(filename='token_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Keepa setup
API_KEY = "YOUR_API_KEY"
keepa = Keepa(API_KEY)

TOKEN_SAFETY_LIMIT = 300  # Soglia per attivare sleep intelligente
SLEEP_DURATION = 600      # 10 minuti

async def fetch_offers():
    # Controllo token disponibili
    tokens_left = keepa.tokensLeft
    if tokens_left < TOKEN_SAFETY_LIMIT:
        print(f"⚠️ Solo {tokens_left} token disponibili. Attendo {SLEEP_DURATION//60} minuti per ricarica...")
        logging.info(f"TOKENS LOW: {tokens_left} - Attesa forzata")
        await asyncio.sleep(SLEEP_DURATION)

    print(f"🔁 Token disponibili: {tokens_left}")
    logging.info(f"TOKENS OK: {tokens_left}")

    # Simulazione richiesta categoria
    try:
        # Inserisci qui la tua query Keepa es.:
        # products = keepa.query(["B01N6S068R", "B07YFGQ28K"], domain=1)
        print("🔍 Simulazione richiesta Keepa...")
        await asyncio.sleep(2)
        print("✅ Offerte recuperate (simulazione).")

    except Exception as e:
        print(f"❌ Errore durante la richiesta Keepa: {e}")
        logging.error(f"Errore Keepa: {e}")

# Run main
if __name__ == "__main__":
    asyncio.run(fetch_offers())
