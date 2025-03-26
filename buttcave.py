from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome, Buttcoiner. Join here: https://t.me/+pB0InMHwqFhmYjIx 🍑🪙"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("join", join))
    print("ButtCaveBot is running...")
    app.run_polling()