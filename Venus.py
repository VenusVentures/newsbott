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
    await news.send(message)

bot.run('MTEzMDY0MDUyMTE3NDQ1MDIxNw.G28UBM.PeUL9S6yPFncdVH9HZU3EBK8EuICyVHKK-uoyg')

[
  {
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
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Housing Starts",
    "event_time": "8:15am",
    "forecast_value": "221K",
    "impact": "Low",
    "pairname": "CAD",
    "previous_value": "202K"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "CPI m/m",
    "event_time": "8:30am",
    "forecast_value": "0.3%",
    "impact": "High",
    "pairname": "CAD",
    "previous_value": "0.4%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Median CPI y/y",
    "event_time": "8:30am",
    "forecast_value": "3.7%",
    "impact": "High",
    "pairname": "CAD",
    "previous_value": "3.9%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Trimmed CPI y/y",
    "event_time": "8:30am",
    "forecast_value": "3.6%",
    "impact": "High",
    "pairname": "CAD",
    "previous_value": "3.8%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Common CPI y/y",
    "event_time": "8:30am",
    "forecast_value": "5.0%",
    "impact": "Medium",
    "pairname": "CAD",
    "previous_value": "5.2%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Core CPI m/m",
    "event_time": "8:30am",
    "forecast_value": "",
    "impact": "Low",
    "pairname": "CAD",
    "previous_value": "0.4%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "IPPI m/m",
    "event_time": "8:30am",
    "forecast_value": "-0.2%",
    "impact": "Low",
    "pairname": "CAD",
    "previous_value": "-1.0%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "RMPI m/m",
    "event_time": "8:30am",
    "forecast_value": "-0.3%",
    "impact": "Low",
    "pairname": "CAD",
    "previous_value": "-4.9%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Core Retail Sales m/m",
    "event_time": "8:30am",
    "forecast_value": "0.4%",
    "impact": "High",
    "pairname": "USD",
    "previous_value": "0.1%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Retail Sales m/m",
    "event_time": "8:30am",
    "forecast_value": "0.5%",
    "impact": "High",
    "pairname": "USD",
    "previous_value": "0.3%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Industrial Production m/m",
    "event_time": "9:15am",
    "forecast_value": "0.0%",
    "impact": "Medium",
    "pairname": "USD",
    "previous_value": "-0.2%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Capacity Utilization Rate",
    "event_time": "9:15am",
    "forecast_value": "79.5%",
    "impact": "Low",
    "pairname": "USD",
    "previous_value": "79.6%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "Business Inventories m/m",
    "event_time": "10:00am",
    "forecast_value": "0.2%",
    "impact": "Low",
    "pairname": "USD",
    "previous_value": "0.2%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "FOMC Member Barr Speaks",
    "event_time": "10:00am",
    "forecast_value": "",
    "impact": "Low",
    "pairname": "USD",
    "previous_value": ""
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "NAHB Housing Market Index",
    "event_time": "10:00am",
    "forecast_value": "56",
    "impact": "Low",
    "pairname": "USD",
    "previous_value": "55"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "CB Leading Index m/m",
    "event_time": "10:30am",
    "forecast_value": "",
    "impact": "Low",
    "pairname": "AUD",
    "previous_value": "-0.2%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "GDT Price Index",
    "event_time": "Tentative",
    "forecast_value": "",
    "impact": "Low",
    "pairname": "NZD",
    "previous_value": "-3.3%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "TIC Long-Term Purchases",
    "event_time": "4:00pm",
    "forecast_value": "110.7B",
    "impact": "Low",
    "pairname": "USD",
    "previous_value": "127.8B"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "CPI q/q",
    "event_time": "6:45pm",
    "forecast_value": "0.9%",
    "impact": "High",
    "pairname": "NZD",
    "previous_value": "1.2%"
  },
  {
    "actual_value": "",
    "datetime": "Jul 18",
    "event_name": "MI Leading Index m/m",
    "event_time": "8:30pm",
    "forecast_value": "",
    "impact": "Low",
    "pairname": "AUD",
    "previous_value": "-0.3%"
  }
]