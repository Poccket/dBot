import discord
import random
import praw
import config as cfg
from discord.ext import commands

from pokedex import pokedex
pokedex = pokedex.Pokedex()
reddit = praw.Reddit(	client_id=cfg.redID,
						client_secret=cfg.redSecret,
						user_agent=cfg.redAgent)
class Games():
	'''
	Gaming related commands
	'''
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def roll(self, ctx, *, content:str):
		'''
		Rolls die, then returns the seperate results and a total

		Usage  : roll <amount> <size>	  
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

	@commands.command()
	async def beget(self, ctx, *, content:str):
		'''
		Gets a post from the hot page of a subreddit

		Usage  : beget <sub> [top]
		sub    : an existing subreddit
		top    : if true, do top posts
		'''
		params = content.split()
		try:
			if params[1] == "true":
				redSub = reddit.subreddit(params[0]).top()
			else:
				redSub = reddit.subreddit(params[0]).hot()
		except:
				redSub = reddit.subreddit(params[0]).hot()
		try:
			post_to_pick = random.randint(1, 10)
			for i in range(0, post_to_pick):
				submission = next(x for x in redSub if not x.stickied)
			await ctx.send(submission.url)
		except:
			await ctx.send("Ran into a problem! Is that a subreddit that exists?")

	@commands.command()
	async def pokedex(self, ctx, *, content:str):
		'''
		Pokédex lookup tool, returns information about a pokémon

		Usage  : pokedex <number/name>
		number : Pokémon's Ndex number
		name   : Pokémon's name
		'''
		params = content.split()
		easter = False
		try:
			params[1]
			if params[1] == "f":
				easter = True
		except IndexError:
			pass
		try:
			currPoke = pokedex.get_pokemon_by_number(int(params[0]))
		except ValueError:
			currPoke = pokedex.get_pokemon_by_name(params[0])

		try:
			currPoke[0]["name"]
		except KeyError:
			await ctx.send("Pokemon does not exist!\nDid you spell it right?")
			return


		msgContent		= ""

		embedColor		= 0xff0000
		embedIcon		= "https://upload.wikimedia.org/wikipedia/en/3/39/Pokeball.PNG"
		embedLink		= "https://bulbapedia.bulbagarden.net/wiki/" + currPoke[0]["name"]

		embedFooter		= "Pokédex Lookup"
		embedFooterIcon	= "https://cdn.bulbagarden.net/upload/9/9f/Key_Pok%C3%A9dex_m_Sprite.png"

		pName			= currPoke[0]["name"]
		pNumber 		= currPoke[0]["number"]
		pSpecies		= currPoke[0]["species"] + " Pokémon"
		pTypes			= currPoke[0]["types"]
		pAbilities		= currPoke[0]["abilities"]
		pEvolutions		= currPoke[0]["family"]["evolutionLine"]
		pThumbnail		= currPoke[0]["sprite"]

		fTypes			= ""
		pAbilitiesN		= ""
		pAbilitiesH		= ""
		fAbilities 		= ""
		fEvolutions		= ""

		titleTypes		= "Type(s)"
		titleAbilities	= "Abilities"
		titleEvolutions	= "Evolution Line"

		for x in pTypes:
			fTypes += x + ", "
		fTypes = fTypes[:-2]
		for x in pAbilities["normal"]:
			pAbilitiesN += x + ", "
		for x in pAbilities["hidden"]:
			pAbilitiesH += x + ", "
		fAbilities = "Normal: " + pAbilitiesN[:-2] + "\n" + "Hidden: " + pAbilitiesH[:-2]
		for x in pEvolutions:
			fEvolutions += x + ", "
		fEvolutions = fEvolutions[:-2]

		#stupid easter egg shit

		if easter:
			if str(pNumber) == "123":
				fEvolutions = "\"fuck\""
				titleEvolutions = "Qoutes"
			if str(pNumber) == "420":
				fTypes = "Grass, Fire"
				fEvolutions = "Weedie, Cannabilis, Blazitkin"
				fAbilities = "Normal: Hit It\nHidden: Hide It From The Cops"
				pName = "Weedie"
				pSpecies = "Lit Pokémon"
				pThumbnail = "https://i.kym-cdn.com/photos/images/original/001/165/778/f7c.jpg"
				embedFooter = "Tokédex Lookup"
			if str(pNumber) == "69":
				await ctx.send(":eyes:")
				return

		# end easter egg shit

		embed = discord.Embed	(	title	= pSpecies 			,
							  		colour	= embedColor		)
		embed.set_author		(	name	= pName 			,
						 			url		= embedLink 		,
						 			icon_url= embedIcon 		)
		embed.set_thumbnail 	(	url		= pThumbnail 		)
		embed.add_field 		(	name 	= titleTypes 		,
									value 	= fTypes			)
		embed.add_field			(	name 	= titleAbilities 	, 
									value 	= fAbilities		)
		embed.add_field			(	name 	= titleEvolutions 	, 
									value 	= fEvolutions		)
		embed.set_footer 		(	text 	= embedFooter 		, 
									icon_url= embedFooterIcon 	)

		await ctx.send(content	= msgContent, embed = embed)

	@commands.command(hidden=True)
	async def pokeList(self, ctx, *, content:str):
		'''
		Pokédex lookup tool, returns information about a pokémon in the form of a python list

		Usage  : pokedex <number>
		number : Pokémon's Ndex number
		'''
		params = content.split()
		try:
			int(params[0])
		except ValueError:
			await ctx.send("NaN")
			return
		currPoke = pokedex.get_pokemon_by_number(int(params[0]))
		await ctx.send(currPoke)


def setup(bot):
	bot.add_cog(Games(bot))
