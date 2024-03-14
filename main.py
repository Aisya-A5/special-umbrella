import discord
from bot_logic import gen_pass, coin_sides, gen_emodji, detected, anorganik_organik
from discord.ext import commands
import random
import os
import requests


# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()

# Mengaktifkan hak istimewa message-reading
intents.members = True
intents.message_content = True

# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} on the go')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def pwd(ctx,number):
    await ctx.send(gen_pass(int(number)))

@bot.command()
async def koin(ctx):
    await ctx.send(coin_sides())

@bot.command()
async def react(ctx):
    await ctx.send(gen_emodji())
    
@bot.command()
async def deleteme(ctx):
    await ctx.send("I will delete it in 3 seconds...", delete_after=3.0)
    async for message in ctx.channel.history(limit=3):
        await message.delete()

@bot.command()
async def joined(ctx, member: discord.Member):
    #Says when a member joined.
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    await ctx.send(f'you can use a command by using "$" in front of your text')

@bot.command()
async def meme(ctx):
    daftar_gambar = os.listdir('image')
    gambar = random.choice(daftar_gambar)

    with open(f'image/{gambar}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)

    # Kita kemudian dapat mengirim file ini sebagai tolak ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def tips_mengurangi_polusi(ctx):
    await ctx.send(f'1 Membuang sampah pada tempatnya')
    await ctx.send (f'2 Menggunakan transportasi umum')
    await ctx.send(f'3 Mengurangi penggunaan limbah plastik')

@bot.command()
async def deteksiGambar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save('image/'+attachment.filename)
            prob, name = detected("image/"+attachment.filename)
            if name == 'angsa':
                await ctx.send(f'saya yakin {prob}%, ini adalah {name} angsa ini memiliki leher yang cenderung lebih panjang dan paruh yang lebih besar dibandingkan bebek. Mereka hidup berkelompok dan merupakan unggas yang sering dilambangkan sebagai bentuk kesetiaan cinta')
            elif name == 'bebek':
                await ctx.send(f'saya yakin {prob}%, ini adalah {name} bebek cenderung memiliki leher pendek dan badan yang kecil dibandingkan dengan angsa, mereka hidup berkelompok dan merupakan unggas yang sering bermigrasi ke tempat yang lebih hangat apabila habitat yang sedang mereka tinggali mengalami musim dingin.')

    else:
        await ctx.send("Images not found!")

@bot.command()
async def AnorganikOrganik(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save('image/'+attachment.filename)
            prob, name = anorganik_organik("image/"+attachment.filename)
            if name == 'anorganik':
                await ctx.send(f'saya yakin {prob}%, ini adalah {name} sampah jenis anorganik adalah sampah yang membutuhkan waktu yang lama untuk bisa diuraikan oleh lingkungan, biasanya sampah ini bukan berasal dari makhluk hidup, sampah ini bisa dipilah-pilih lagi dan dibagi antara yang bisa didaur ulang dari rumah dan yang memerlukan penanganan yang lebih kompleks.')
            elif name == 'organik':
                await ctx.send(f'saya yakin {prob}%, ini adalah {name} sampah jenis organik adalah sampah yang mudah diuraikan secara natural oleh lingkungan (pembusukan), biasanya sampah ini berasal dari makhluk hidup seperti tanaman dan hewan. Sampah jenis ini bisa dipilah-pilih dan digunakan sebagai pupuk kompos untuk menyuburkan tanaman.')

    else:
        await ctx.send("Images not found!")

bot.run("bot token")
