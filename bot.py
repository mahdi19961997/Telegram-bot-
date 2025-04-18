from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# توکن ربات
TOKEN = '7876652380:AAHxPYfrN-fkElbhKAP7Ajp1wInw91LRSZ4'

# تابع منو (دستور /start)
def menu(update, context):
    update.message.reply_text(
        "سلام عموجون!\n\nمنوی کافه:\n- خوبی\n- چخبر\n- دلتنگم\n- دوستت دارم\n- خوابم میاد\n- عمو جون"
    )

# پاسخ خودکار به پیام‌ها
def handle_message(update, context):
    text = update.message.text.strip().lower()
    
    if "خوبی" in text:
        update.message.reply_text("قربونت عموجون، تو خوبی؟")
    elif "چخبر" in text or "چه خبر" in text or "چ خبر" in text:
        update.message.reply_text("خبرا که پیش شماست عموجون!")
    elif "دلتنگم" in text:
        update.message.reply_text("بیا باهم یه فنجون قهوه بخوریم، دلتنگ‌هات رو شریک بشیم.")
    elif "دوستت دارم" in text:
        update.message.reply_text("من یه فنجون بیشتر عموجون!")
    elif "خوابم میاد" in text:
        update.message.reply_text("یه خواب ناز زیر پتو با صدای بارون، نوش جانت!")
    elif "عمو جون" in text or "عموجون" in text:
        update.message.reply_text("جان دلم؟ بگو ببینم چی شده!")
    else:
        update.message.reply_text("چی گفتی عموجون؟ دوباره بگو!")

# اجرای ربات
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", menu))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("ربات روشن شد عموجون!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
