import telebot  # pyTelegramBotAPI থেকে telebot আসে
import json
from utils import play_audio_from_url

# Load config
with open("config.json") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["telegram_token"])
ADMIN_CHAT_ID = config["admin_chat_id"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "🤖 OrangeCarrier Call Bot Active!")

def notify_call(call_data):
    """Send Telegram notification when new call arrives"""
    cid = call_data.get("cid_num")
    name = call_data.get("client_name")
    duration = call_data.get("duration")
    uuid = call_data.get("uuid")

    msg = (
        f"📞 *Incoming Call Detected!*\n"
        f"👤 Name: {name}\n"
        f"📱 CID: `{cid}`\n"
        f"⏱ Duration: {duration}s"
    )

    bot.send_message(ADMIN_CHAT_ID, msg, parse_mode="Markdown")

    # Audio link
    sound_url = f"{config['audio_base_url']}?did={cid}&uuid={uuid}"
    play_audio_from_url(sound_url)

def run_bot():
    print("🤖 Telegram bot started...")
    bot.infinity_polling()
