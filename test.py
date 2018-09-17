from discord.ext import commands
import random
prefix = "?"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def syn(ctx):
	'''
	The TCP 3-way Handshake
	'''
	await ctx.send("syn-ack")

@bot.command()
async def roll_d6(ctx):
	'''
	Rolls a D6 die
	'''
	await ctx.send(random.randint(1,6))

@bot.command()
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


bot.run("NDI2NjQwMjEzMDAzOTkzMDk5.DoFyBQ.XkuXHDh3es6UtXLlCeq_v0QNWd0")