import os, asyncio
from groq import Groq
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def analyze_image(image_url, question="What's in this image?"):
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        model="llama-3.2-90b-vision-preview",
        temperature=1,
        max_tokens=1024
    )
    
    return chat_completion.choices[0].message.content

async def send_message_to_discord(message_content):
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are Mira, my super cool personal assistant, always ready to help me on anything and can speak Indonesian. You have extensive knowledge about machine learning, but you can also have casual conversations about anything.",
            },
            {
                "role": "user",
                "content": message_content,
            }
        ],
        model="llama-3.2-90b-vision-preview",
    )
    
    return chat_completion.choices[0].message.content

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        
    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced")

bot = Bot()

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="/ask | for help"
    ))

@bot.tree.command(name="ask", description="Ask Mira a question")
async def ask(interaction: discord.Interaction, question: str, image: discord.Attachment = None):
    await interaction.response.defer()
    
    if image:
        # Verify it's an image
        if not image.content_type.startswith('image/'):
            await interaction.followup.send("The attachment must be an image!")
            return
            
        # Process image with question
        response = await analyze_image(image.url, question)
    else:
        # Process text-only question
        response = await send_message_to_discord(question)
        
    await asyncio.sleep(1)
    await interaction.followup.send(response)

@bot.tree.command(name="analyze", description="Analyze an attached image")
async def analyze(interaction: discord.Interaction, image: discord.Attachment, question: str = "What's in this image?"):
    await interaction.response.defer()
    
    if not image.content_type.startswith('image/'):
        await interaction.followup.send("The attachment must be an image!")
        return

    response = await analyze_image(image.url, question)
    await asyncio.sleep(1)
    await interaction.followup.send(response)

bot.run(os.getenv('DISCORD_TOKEN'))