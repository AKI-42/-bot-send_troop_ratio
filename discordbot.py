from discord.ext import commands
from os import getenv
import traceback
import discord
import math

bot = commands.Bot(command_prefix='/')

@bot.command()
async def ratio(ctx, main: int, ratio: int, max_size: int):

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

	await ctx.send(f"死役 {math.floor(10 - (main*10))}割\n\
歩兵  {inf_heigh_t:<10,}死役  {inf_low_t:<10,}  |  合計  {inf_heigh_t+inf_low_t:>10,}\n\
弓兵  {range_heigh_t:<10,}死役  {range_low_t:<10,}  |  合計  {range_heigh_t+range_low_t:>10,}\n\
騎兵  {cav_heigh_t:<10,}死役  {cav_low_t:<10,}  |  合計  {cav_heigh_t+cav_low_t:>10,}")

@bot.command()
async def embed_test(ctx):

	embed = discord.Embed( # Embedを定義する
    	title="Example Embed",# タイトル
        color=0x00ff00, # フレーム色指定(今回は緑)
        description="Example Embed for Advent Calendar", # Embedの説明文 必要に応じて
        url="https://example.com" # これを設定すると、タイトルが指定URLへのリンクになる
        )
	embed.set_author(name=client.user, # Botのユーザー名
                     url="https://repo.exapmle.com/bot", # titleのurlのようにnameをリンクにできる。botのWebサイトとかGithubとか
                     icon_url=client.user.avatar_url # Botのアイコンを設定してみる
                     )
	embed.add_field(name="フィールド１",value="値１") # フィールドを追加。
	embed.add_field(name="フィールド２",value="値２")

	await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
