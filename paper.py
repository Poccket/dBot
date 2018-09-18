import discord
from discord.ext import commands

class Paper():
	'''
	Pen & Paper or RPG related commands
	'''
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def roll(ctx, *, content:str):
		'''
		Rolls dice

		Usage  :
		  roll <amount> <size>
		amount : Amount of dice to be rolled
		size   : Size of the dice
		'''
		params = content.split()
		try:
			int(params[0])
			int(params[1])
		except ValueError:
			await ctx.send("One of your paramaters is not a number\nDo ?help roll to get the usage of this command")
			return
		results = []
		output = "Results: \n`"
		total = 0
		for x in range(0, int(params[0])):
			results.append(random.randint(1,int(params[1])))
			output += str(results[x]) + ", "
			total += results[x]
		output = output[:-2] + "`\nTotal: " + str(total)
		await ctx.send(output)

def setup(bot):
	bot.add_cog(Paper(bot))