import discord
from discord.ext import commands

class Debug:
	'''
	Commands for testing and fixing issues
	'''
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='ping', hidden=True)
	async def ping(self, ctx):
		'''
		Returns the latency of the bot

		Usage  : ping
		'''
		latency = self.bot.latency
		await ctx.send(latency)


	@commands.command(hidden=True)
	async def echo(self, ctx, *, content:str):
		'''
		Repeats the given paramaters

		Usage  : echo <message>
		message: Any amount of text
		'''
		await ctx.send(content)

	@commands.command(name='embeds', hidden=True)
	async def example_embed(self, ctx):
		"""
		A sample embed

		Usage  : example_embed
		"""

		embed = discord.Embed(title='Example Embed',
							  description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
							  colour=0x98FB98)
		embed.set_author(name='MysterialPy',
						 url='https://gist.github.com/MysterialPy/public',
						 icon_url='http://i.imgur.com/ko5A30P.png')
		embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

		embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
		embed.add_field(name='Command Invoker', value=ctx.author.mention)
		embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

		await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)

def setup(bot):
	bot.add_cog(Debug(bot))