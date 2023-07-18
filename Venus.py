import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # This is required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("-----")
    print("Bot is online!")
    print("-----")

@bot.command()
async def say(news, *, message):
    # Delete the original command message
    await news.message.delete()

    # Send the user's message as the bot
    await news.send("Here are the financial news and economic events for Jul 18:")
    await news.send({
        "actual_value": "",
        "datetime": "Jul 18",
        "event_name": "Tertiary Industry Activity m/m",
        "event_time": "12:30am",
        "forecast_value": "0.4%",
        "impact": "Low",
        "pairname": "JPY",
        "previous_value": "1.2%"
    },
    {
        "actual_value": "",
        "datetime": "Jul 18",
        "event_name": "G20 Meetings",
        "event_time": "Day 5",
        "forecast_value": "",
        "impact": "Medium",
        "pairname": "All",
        "previous_value": ""
    },
    {
        "actual_value": "",
        "datetime": "Jul 18",
        "event_name": "Foreign Direct Investment ytd/y",
        "event_time": "Tentative",
        "forecast_value": "",
        "impact": "Low",
        "pairname": "CNY",
        "previous_value": "0.1%"
    },
    {
        "actual_value": "",
        "datetime": "Jul 18",
        "event_name": "EU Economic Forecasts",
        "event_time": "Tentative",
        "forecast_value": "",
        "impact": "Low",
        "pairname": "EUR",
        "previous_value": ""
    },
    {
        "actual_value": "",
        "datetime": "Jul 18",
        "event_name": "30-y Bond Auction",
        "event_time": "Tentative",
        "forecast_value": "",
        "impact": "Low",
        "pairname": "GBP",
        "previous_value": "4.39|2.6"
    },
    # Add the rest of the events here...
    )

bot.run('MTEzMDY0MDUyMTE3NDQ1MDIxNw.G28UBM.PeUL9S6yPFncdVH9HZU3EBK8EuICyVHKK-uoyg')
