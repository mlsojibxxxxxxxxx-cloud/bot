import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from faker import Faker

# ১. তোমার বট টোকেন এখানে দাও (Replace with your actual Bot Token)
BOT_TOKEN = "8493465528:AAHHc9-a1RFCwGyLNmBWiSfA5Fg3MHR9TPo"

# ২. লগিং সেটআপ (Setup Logging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ৩. ফেক জেনারেটরের সূচনা (Initialize the Faker Generator)
# 'de_DE' ব্যবহার করা হয়েছে, কারণ এটি জার্মান লোকেলের জন্য
fake = Faker('de_DE')

# ৪. /start কমান্ডের ফাংশন
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """যখন ইউজার /start কমান্ড দেবে তখন এই মেসেজটি দেখাবে।"""
    user = update.effective_user
    await update.message.reply_html(
        f"স্বাগতম, {user.mention_html()}! আমি তোমার  জার্মান আইডেন্টিটি জেনারেটর বট।\n\n"
        "জার্মান লোকেশন পেতে এই কমান্ডটি ব্যবহার করো:\n"
        "**/generate_de**"
    )

# ৫. /generate_de কমান্ডের মূল ফাংশন
async def generate_fake_german_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ফেক জার্মান নাম, নাম্বার এবং ঠিকানা জেনারেট করবে।"""
    
    # ফেক ডেটা জেনারেট করা
    name = fake.name()
    phone_number = fake.phone_number()
    street_address = fake.street_address()
    city = fake.city()
    postcode = fake.postcode()
    
    # সম্পূর্ণ ঠিকানা একত্রিত করা
    full_address = f"{street_address}, {postcode} {city}"
    
    # আউটপুট মেসেজ তৈরি করা
    response_text = (
        "🇩🇪 **ফেক জার্মান আইডেন্টিটি জেনারেটেড** 🇩🇪\n\n"
        f"**নাম (Name):** `{name}`\n"
        f"**ফোন নাম্বার (Phone):** `{phone_number}`\n"
        f"**ঠিকানা (Location):** `{full_address}`\n\n"
        "*(এই ডেটা শুধুমাত্র ব্যক্তিগত, অনৈতিক  ব্যবহারের জন্য প্রস্তুত করা হয়েছে। এই বটটি বানিয়েছেন @MLSOJIB)*"
    )

    # ইউজারকে মেসেজটি পাঠানো
    await update.message.reply_text(
        response_text,
        parse_mode='Markdown' # আউটপুটকে সুন্দর করে দেখানোর জন্য Markdown ব্যবহার করা হয়েছে
    )

# ৬. মূল ফাংশন (Main Function to Run the Bot)
def main() -> None:
    """বটকে শুরু করে এবং সব হ্যান্ডলার যুক্ত করে।"""
    # Application ক্লাস ব্যবহার করে বটের জন্য একটি ইন্টারফেস তৈরি করা
    application = Application.builder().token(BOT_TOKEN).build()

    # কমান্ড হ্যান্ডলার যুক্ত করা
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("generate_de", generate_fake_german_id))

    # বটকে অবিরাম চলতে দাও (Start the Bot)
    print(f"[*] বট চালু হচ্ছে... টোকেন: {BOT_TOKEN[:5]}...")
    application.run_polling(poll_interval=3)
    # poll_interval = 3 মানে প্রতি 3 সেকেন্ডে নতুন মেসেজের জন্য চেক করবে

if __name__ == "__main__":
    main()