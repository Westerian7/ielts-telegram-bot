import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

# Load questions from files
def load_questions(file_name):
    with open(file_name, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

part1_questions = load_questions("part1_questions.txt")
part2_questions = load_questions("part2_questions.txt")
part3_questions = load_questions("part3_questions.txt")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Part 1", callback_data='part1')],
        [InlineKeyboardButton("Part 2", callback_data='part2')],
        [InlineKeyboardButton("Part 3", callback_data='part3')],
    ]
    await update.message.reply_text(
        "Welcome! Choose a question category:", 
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Button callback
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'part1':
        question = random.choice(part1_questions)
    elif query.data == 'part2':
        question = random.choice(part2_questions)
    elif query.data == 'part3':
        question = random.choice(part3_questions)
    else:
        question = "Invalid selection."

    await query.edit_message_text(text=f"Here’s your question:\n\n{question}")

# Main function
async def main():
    TOKEN = os.getenv("7799617257:AAG6mp9kM2GRiT8O5HYlB_J0cG2zrBEx_x4")
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
