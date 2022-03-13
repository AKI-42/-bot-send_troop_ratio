from discord.ext import commands
from os import getenv
import traceback
import math

bot = commands.Bot(command_prefix='/')

@bot.command()
async def ratio(ctx, ratio: int, max_size: int):

	inf_ratio = math.floor(ratio/100)
	ratio = math.floor(ratio%100)
	range_ratio = math.floor(ratio/10)
	cav_ratio = ratio % 10

	total = inf_ratio + range_ratio + cav_ratio
	uni = max_size / total

	inf_heigh_t = math.floor((inf_ratio*uni)*0.6)
	inf_low_t = math.floor((inf_ratio*uni)*0.4)

	range_heigh_t = math.floor((range_ratio*uni)*0.6)
	range_low_t = math.floor((range_ratio*uni)*0.4)

	cav_heigh_t = math.floor((cav_ratio*uni)*0.6)
	cav_low_t = math.floor((cav_ratio*uni)*0.4)

	await ctx.send(f"歩兵  {inf_heigh_t:<10,}死役  {inf_low_t:<10,}  |  合計  {inf_heigh_t+inf_low_t:>10,}\n\
弓兵  {range_heigh_t:<10,}死役  {range_low_t:<10,}  |  合計  {range_heigh_t+range_low_t:>10,}\n\
騎兵  {cav_heigh_t:<10,}死役  {cav_low_t:<10,}  |  合計  {cav_heigh_t+cav_low_t:>10,}")

@bot.command()
async def test1(ctx, *arg):

	inf_ratio = math.floor(arg[0]/100)
	arg[0] = math.floor(arg[0]%100)
	range_ratio = math.floor(arg[0]/10)
	cav_ratio = arg[0] % 10

	total = inf_ratio + range_ratio + cav_ratio
	uni = arg[1] / total

	if len(arg) == 2:
		main_troop__ratio = 0.6
	elif len(arg) == 3:
		main_troop_ratio = arg[2] / 10

	sac_troop_ratio = 1 - main_troop__ratio

	inf_heigh_t = math.floor((inf_ratio*uni)*main_troop__ratio)
	inf_low_t = math.floor((inf_ratio*uni)*sac_troop_ratio)

	range_heigh_t = math.floor((range_ratio*uni)*main_troop__ratio)
	range_low_t = math.floor((range_ratio*uni)*sac_troop_ratio)

	cav_heigh_t = math.floor((cav_ratio*uni)*main_troop_ratio)
	cav_low_t = math.floor((cav_ratio*uni)*sac_troop_ratio)

	await ctx.send(f"歩兵  {inf_heigh_t:<10,}死役  {inf_low_t:<10,}  |  合計  {inf_heigh_t+inf_low_t:>10,}\n\
弓兵  {range_heigh_t:<10,}死役  {range_low_t:<10,}  |  合計  {range_heigh_t+range_low_t:>10,}\n\
騎兵  {cav_heigh_t:<10,}死役  {cav_low_t:<10,}  |  合計  {cav_heigh_t+cav_low_t:>10,}")

async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
