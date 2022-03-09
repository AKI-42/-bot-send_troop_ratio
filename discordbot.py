from discord.ext import commands
from os import getenv
import traceback
import math

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


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

	await ctx.send(f"歩兵  {inf_heigh_t:<10,}死役  {inf_low_t:<10,}  |  合計  {inf_heigh_t+inf_low_t:>10,}")
	await ctx.send(f"弓兵  {range_heigh_t:<10,}死役  {range_low_t:<10,}  |  合計  {range_heigh_t+range_low_t:>10,}")
	await ctx.send(f"騎兵  {cav_heigh_t:<10,}死役  {cav_low_t:<10,}  |  合計  {cav_heigh_t+cav_low_t:>10,}")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
