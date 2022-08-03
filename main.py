from pyrogram import Client, filters

app = Client("my_account",
api_id=2236912,
api_hash='2a8db2b1122af3f39aaa6bd8b3f4c935',
bot_token='1690770374:AAH2Lm29zxKyqjpxjkM3JWysNgFzbyMU5Po')


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from bro!")


app.run()