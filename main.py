import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

# আপনার টোকেন এখানে দিন
API_TOKEN = '8272232302:AAFQsczsDl0cLTztQQtortFmPR-T7Q5dlyY'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 বোট চালু হয়েছে!\nএসএমএস পাঠাতে লিখুন: /sms 017xxxxxxxx বার্তা")

@dp.message_handler(commands=['sms'])
async def send_sms(message: types.Message):
    args = message.get_args().split(' ', 1)
    if len(args) < 2:
        return await message.reply("❌ ফরম্যাট: /sms নম্বর বার্তা")
    
    number, text = args[0], args[1]
    # আপনার API URL এবং Key এখানে ব্যবহার করুন
    api_url = f"https://bulksms.rgb-boys.my.id/api.php?key=RGB-mhhacker&number={number}&msg={text}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            await message.reply(f"✅ {number} নম্বরে এসএমএস পাঠানো হয়েছে!")
        else:
            await message.reply("❌ এপিআই সার্ভারে সমস্যা।")
    except:
        await message.reply("❌ কোনো একটি ভুল হয়েছে।")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
