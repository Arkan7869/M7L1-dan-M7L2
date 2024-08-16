import discord
from discord.ext import commands
from utils import get_class
with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variabel token
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
                   
@bot.command()
async def check_image(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")


bot.run("MTIxODQyMzk3MTQ2OTMzMjU1MQ.G5q78Z.cgySjgAvo4pVY0j1zPccVC6KhG9OENgh0kcq14")
