import discord
import random
from discord.ext import commands

prefix = "?"
startup_extensions = ["paper", "debug"]
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
	activity = discord.Game(name="Prefix is \'?\'")
	await bot.change_presence(status=discord.Status.dnd, activity=activity)
	print("Everything's all ready to go~")

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))

	bot.run("NDI2NjQwMjEzMDAzOTkzMDk5.DoFyBQ.XkuXHDh3es6UtXLlCeq_v0QNWd0")