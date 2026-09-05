import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🔍 Pattern Search"), KeyboardButton("📱 Single Number")],
        [KeyboardButton("📦 Bulk Search"), KeyboardButton("📍 Select Pincode")],
        [KeyboardButton("✅ Available Numbers")],
        [KeyboardButton("💎 VIP Categories"), KeyboardButton("📞 Contact Admin")]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Welcome to VIP Number Search Bot!\n\n"
        "Choose an option below:",
        reply_markup=reply_markup
    )

async def pattern(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Pattern Search\n\n"
        "Example:\n"
        "9999\n"
        "0000\n"
        "1234\n\n"
        "Search system will be connected next."
    )

async def single(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Send the 10-digit mobile number you want to search."
    )

async def bulk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Send multiple numbers, one number per line."
    )

async def pincode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 Send your 6-digit pincode.\n\n"
        "Example: 411001"
    )

async def available(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Available Numbers\n\n"
        "No search results yet. Select a pincode and search for a pattern first."
    )

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 VIP Categories\n\n"
        "🔥 9999 Series\n"
        "🔥 0000 Series\n"
        "🔥 786 Series\n"
        "🔥 1234 Series\n"
        "🔥 Repeated Numbers"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Contact Admin\n\n"
        "For VIP number enquiry, contact the admin."
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pattern", pattern))
    app.add_handler(CommandHandler("single", single))
    app.add_handler(CommandHandler("bulk", bulk))
    app.add_handler(CommandHandler("pincode", pincode))
    app.add_handler(CommandHandler("available", available))
    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("contact", contact))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
