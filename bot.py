import os
import discord
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
from flask import Flask
import threading

# Webserver für Render
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Starte Webserver in separatem Thread
threading.Thread(target=run).start()

# Discord Bot
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CHANNELS_TO_TRANSLATE = ["𝔸𝕝𝕝𝕘𝕖𝕞𝕖𝕚𝕟", "𝔸𝕟𝕜ü𝕟𝕕𝕚𝕘𝕦𝕟𝕘𝕖𝕟", "𝕋𝕣𝕒𝕕𝕖𝕟"]

@client.event
async def on_ready():
    print(f'✅ Bot ist online als {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name in CHANNELS_TO_TRANSLATE:
        translated = GoogleTranslator(source='auto', target='en').translate(message.content)
        await message.channel.send(f"🇬🇧 **Übersetzung:**\n> {translated}")

client.run(TOKEN)
