from aiogram import Bot, Dispatcher, executor, types
import requests
import json

bot = Bot(token="5534370677:AAHmgRG46RQ7UDkL8ZHnTpL2ZeEQMc05r6k")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def get_weather(message: types.Message):
    weather="http://api.openweathermap.org/data/2.5/forecast?q="+message.text+"&appid=53ca5ec4fe9f4763ce0a7571162b5b25"
    data=requests.get(weather).text
    result=json.loads(data)
    print(result)
    temp=result["list"][0]["main"]["temp"]
    main=result["list"][0]["weather"][0]["main"]
    await message.reply("weather in city " + message.text + " temperature- " + str(temp) + " weather- " + main)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    weather in city
    kiev
    next: temperature - 287.52
    weather - Clouds