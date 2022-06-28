from PIL import Image
import pytesseract
import asyncio
from pyrogram import Client,filters,enums
from os import remove 

api_id = 15296051
api_hash = "4c3e35efa89e4a71172e986f80f57c7b"
token = input("Enter token : \n")
app = Client("ocr", bot_token=token, api_id = api_id, api_hash = api_hash)

@app.on_message(filters.private)
async def private(c,msg):
  if msg.text == "/start" :
    await msg.reply("• اهلا بك في بوت استخراج النصوص من الصور \n• طريفه الاستخدام : \n فقط ارسل الصوره وسوف يتم استخراج النص")
    return False 
  if msg.photo :
    try :
      dell = await msg.reply("• جاري تحميل الصوره... ")
      await msg.download("./photo.jpg")
      txx = pytesseract.image_to_string(image = Image.open('./photo.jpg'))
      await dell.delete(revoke=True)
      await msg.reply(txx)
      remove("./photo.jpg")
    except Exception as e:
      await msg.reply(e)

## print()


try:
  print("\n• Done bot started ..\n")
  await app.run()
except :
  print("• التوكن غير صحيح")
