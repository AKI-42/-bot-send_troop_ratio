from discord.ext import commands
from os import getenv
import traceback
import discord
import math

bot = commands.Bot(command_prefix='/')

@bot.command()
async def ratio(ctx, main: int, ratio: int, max_size: int):
	
	info = ratio
	main /= 10

	inf_ratio = math.floor(ratio/100)
	ratio = math.floor(ratio%100)
	range_ratio = math.floor(ratio/10)
	cav_ratio = ratio % 10

	total = inf_ratio + range_ratio + cav_ratio
	uni = max_size / total

	inf_heigh_t = math.floor((inf_ratio*uni)*main)
	inf_low_t = math.floor((inf_ratio*uni) - inf_heigh_t)

	range_heigh_t = math.floor((range_ratio*uni)*main)
	range_low_t = math.floor((range_ratio*uni) - range_heigh_t)

	cav_heigh_t = math.floor((cav_ratio*uni)*main)
	cav_low_t = math.floor((cav_ratio*uni) - cav_heigh_t)

	embed = discord.Embed(
		title="比率 : " + str(info) + "   派兵数 : " + str(max_size),
		color=0x00ff00,
		description="死役 " + str(math.floor(10 - (main*10))) + "割"
		)
	embed.add_field(name="歩兵",value=str(inf_heigh_t) + "aaaaksjdkasjfosiaejfoaijef")
	embed.add_field(name="弓兵",value=str(range_heigh_t))
	embed.add_field(name="騎兵",value=str(cav_heigh_t))
	await ctx.send(embed=embed)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)


"""
	embed.add_field(name="歩兵",value=str(inf_heigh_t),value=str(value=inf_low_t))
 	embed.add_field(name="弓兵",value=range_heigh_t,value=range_low_t)
	embed.add_field(name="騎兵",value=cav_heigh_t,value=cav_low_t)
 """

""" 	await ctx.send(f"死役 {math.floor(10 - (main*10))}割\n\
歩兵  {inf_heigh_t:<10,}死役  {inf_low_t:<10,}  |  合計  {inf_heigh_t+inf_low_t:>10,}\n\
弓兵  {range_heigh_t:<10,}死役  {range_low_t:<10,}  |  合計  {range_heigh_t+range_low_t:>10,}\n\
騎兵  {cav_heigh_t:<10,}死役  {cav_low_t:<10,}  |  合計  {cav_heigh_t+cav_low_t:>10,}") """