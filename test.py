import discord
from discord.ext import commands
import config as cfg 

startup_extensions = ["games", "debug"]
bot = commands.Bot(command_prefix=cfg.prefix)

@bot.event
async def on_ready():
	activity = discord.Game(name="Prefix is \'" + cfg.prefix + "\'")
	await bot.change_presence(status=discord.Status.dnd, activity=activity)
	print("Everything's all ready to go~")

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))

	bot.run(cfg.token)
