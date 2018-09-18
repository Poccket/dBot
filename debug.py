import discord
from discord.ext import commands

class Debug():
	'''
	Commands for testing and fixing issues
	'''
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(ctx):
		'''
		Sends the latency of the bot

		Usage  :
		  ping
		'''
		# Get the latency of the bot
		latency = bot.latency  # Included in the Discord.py library
		# Send it to the user
		await ctx.send(latency)


	@commands.command()
	async def echo(ctx, *, content:str):
		'''
		Repeats the given paramaters

		Usage  :
		  echo <message>
		message: Any amount of text
		'''
		await ctx.send(content)

def setup(bot):
	bot.add_cog(Debug(bot))