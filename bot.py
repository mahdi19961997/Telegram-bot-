from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import MessageEntity

# توکن ربات
TOKEN = '7876652380:AAHxPYfrN-fkElbhKAP7Ajp1wInw91LRSZ4'

# کلیدواژه‌ها و پاسخ‌ها
keywords = {
    "سلام": "سلام عمو جون خوش اومدین",
    "مرسی": "چش مایی عمو",
    "صبح بخیر": "صبح شمام بخیر عمو جون",
    "ظهر بخیر": "ظهر شمام بخیر عمو جون",
    "شب بخیر": "شب شمام بخیر عمو جون",
    "خوبی": "قربونت عموجون، تو خوبی؟",
    "چخبر": "خبرا که پیش شماست عموجون!",
    "چه خبر": "خبرا که پیش شماست عموجون!",
    "چ خبر": "خبرا که پیش شماست عموجون!",
    "دلتنگم": "بیا باهم یه فنجون قهوه بخوریم، دلتنگ‌هات رو شریک بشیم.",
    "دوستت دارم": "من یه فنجون بیشتر عموجون!",
    "خوابم میاد": "یه خواب ناز زیر پتو با صدای بارون، نوش جانت!",
    "عمو جون": "جان دلم؟ بگو ببینم چی شده!",
    "عموجون": "جان دلم؟ بگو ببینم چی شده!",
}

# نوشیدنی‌ها و طرز تهیه
drinks = {
    "اسپرسو": "اسپرسو: قهوه آسیاب‌شده را در دستگاه اسپرسوساز قرار دهید و با فشار آب داغ، عصاره قهوه را استخراج کنید.",
    "کاپوچینو": "کاپوچینو: یک شات اسپرسو را با شیر بخار داده‌شده و کف شیر ترکیب کنید.",
    "لاته": "لاته: یک شات اسپرسو را با مقدار بیشتری شیر بخار داده‌شده و کمی کف شیر ترکیب کنید.",
    "آمریکانو": "آمریکانو: یک شات اسپرسو را با آب داغ رقیق کنید.",
    "ماکیاتو": "ماکیاتو: یک شات اسپرسو را با کمی کف شیر تزئین کنید.",
    "موکا": "موکا: اسپرسو، شیر بخار داده‌شده و شکلات داغ را ترکیب کنید.",
    "هات چاکلت": "هات چاکلت: شیر گرم را با پودر کاکائو و شکلات ذوب‌شده مخلوط کنید.",
    "چای ماسالا": "چای ماسالا: چای سیاه را با ادویه‌های ماسالا (مثل دارچین، زنجبیل و هل) و شیر گرم ترکیب کنید.",
    "فراپه": "فراپه: قهوه فوری، یخ، شیر و شکر را در مخلوط‌کن ترکیب کنید.",
    "موهیتو": "موهیتو: برگ نعناع، لیمو و شکر را له کنید، سپس یخ و آب گازدار اضافه کنید.",
}

# دستور /start یا "منوی کافه"
def menu(update, context):
    menu_text = "سلام عموجون!\n\nمنوی کافه:\n" + "\n".join(
        ["- " + kw for kw in list(keywords.keys()) + list(drinks.keys())]
    )
    update.message.reply_text(menu_text)

# پاسخ‌دهی به پیام‌ها
def handle_message(update, context):
    msg = update.message

    if msg.reply_to_message:
        return  # پیام‌های ریپلی شده رو نادیده بگیر

    if msg.chat.type != "private" and not msg.text:
        return  # فقط متن‌ها در چت‌های گروهی بررسی شن

    text = msg.text.strip().lower()

    # چک کلمات دقیق
    if text in keywords:
        msg.reply_text(keywords[text])
        return

    # جلوگیری از تشخیص اشتباه مثل "اصلاح" به جای "اصل"
    if text == "اصل":
        msg.reply_text("شما مامور ثبت احوالی عموجون؟", reply_to_message_id=msg.message_id)
        return

    # طرز تهیه نوشیدنی
    for drink in drinks:
        if text == drink:
            msg.reply_text(drinks[drink])
            return

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
