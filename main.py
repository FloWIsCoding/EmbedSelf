import discord
from discord.ext import commands

def main(token, prefix="$"):
	toi= commands.Bot(command_prefix=prefix,self_bot=True)
	
	@toi.event
	async def on_connect():
		print(f"The Selfbot is Running on {toi.user.name} !\nPrefix : {prefix}")

	@toi.command()
	async def msg(ctx,*msg):
		await ctx.message.delete()
		embed = discord.Embed(description= " ".join(msg),color=0x2f3136)
		await ctx.send(embed=embed)
	
	toi.run(token,bot=False)

connect=True
while connect:
	ur_token= input("What's your token ?\n> ")
	ur_prefix= input("Your prefix (Leave blank if you don't want one!)\n> ")
	try:
		if ur_prefix:
			main(ur_token,ur_prefix)
		else:
			main(ur_token)
		connect = False
	except Exception: 
		print("Wrong token")
	