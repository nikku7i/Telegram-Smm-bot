
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

TOKEN = "7944752991:AAFYJo35ksfkSsxggFXFQErJdaLHBCxiuOM"
ADMIN_USERNAME = "@nikku_b0t"

# Logging setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Welcome {user.first_name}!

"
        "This is your personal SMM bot.
"
        "Use the buttons below to navigate.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Add Funds", callback_data="add_funds")],
            [InlineKeyboardButton("Buy Services", callback_data="buy_services")],
            [InlineKeyboardButton("Check Balance", callback_data="check_balance")],
        ])
    )

# Callback handler
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "add_funds":
        await query.edit_message_text("Please send your deposit screenshot. Admin will verify and credit your wallet.")
    elif data == "buy_services":
        await query.edit_message_text("Select a category:
- Instagram
- Telegram
- YouTube")
    elif data == "check_balance":
        await query.edit_message_text("Your current wallet balance is ₹0.00")  # Example value

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))

    app.run_polling()

if __name__ == "__main__":
    main()
