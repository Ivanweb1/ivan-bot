import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

# Настройки
BOT_TOKEN = "8545325086:AAEv7YitvAay6DissaEeIBciBUvolcNaUdk"

# Ссылки на уроки
LESSON_1_URL = "https://kinescope.io/wZwZFxBiXgTjHGk8sH8i9n"
LESSON_2_URL = "https://kinescope.io/7tm3CyytBenSJ1HJ9L4zSy"

# Твой телеграм ID — уведомления когда кто-то пишет СТАРТ
YOUR_TELEGRAM_ID = "670315301"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет первый урок при команде /start"""
    await update.message.reply_text(
        f"Привет! Сейчас беру двух человек в команду через внутреннюю подготовку — "
        f"записал урок на 60 минут где показываю насколько это реально освоить с нуля.\n\n"
        f"Держи ссылку: {LESSON_1_URL}\n\n"
        f"Когда досмотришь — напиши *ГОТОВО*, пришлю следующий материал.",
        parse_mode="Markdown"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()
    user = update.message.from_user

    # АВИТО → первый урок
    if "авито" in text:
        await update.message.reply_text(
            f"Привет! Сейчас беру двух человек в команду через внутреннюю подготовку — "
            f"записал урок на 60 минут где показываю насколько это реально освоить с нуля.\n\n"
            f"Держи ссылку: {LESSON_1_URL}\n\n"
            f"Когда досмотришь — напиши *ГОТОВО*, пришлю следующий материал.",
            parse_mode="Markdown"
        )

    # ГОТОВО → второй урок
    elif "готово" in text:
        await update.message.reply_text(
            f"Отлично! Держи второе видео — рассказываю как устроена работа в команде, "
            f"стажировка и что ты получишь в итоге.\n\n"
            f"{LESSON_2_URL}\n\n"
            f"Если формат откликается — напиши *СТАРТ*",
            parse_mode="Markdown"
        )

    # СТАРТ → уведомление тебе
    elif "старт" in text:
        await update.message.reply_text(
            f"Рад что досмотрел и откликнулось 👋\n\n"
            f"Иван скоро напишет тебе лично — ответит на вопросы и расскажет следующий шаг."
        )
        await context.bot.send_message(
            chat_id=YOUR_TELEGRAM_ID,
            text=f"🔥 Новый СТАРТ!\n\n"
                 f"Имя: {user.first_name} {user.last_name or ''}\n"
                 f"Username: @{user.username or 'нет'}\n"
                 f"ID: {user.id}\n\n"
                 f"Напиши ему лично!"
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
