import discord
import datetime
from discord.ext import commands


bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Paladin is online in join143!")

@bot.command()
async def hello(ctx):
    username = ctx.message.author.mention
    await ctx.send("Hello " + username)

@bot.command()
@commands.has_any_role("Admin", "Moderator", "Helper")
async def ban(ctx, member_id: int, *, reason=None):
    member = ctx.guild.get_member(member_id) 
    if member is not None: 
        await member.ban()
# async def ban(ctx, member:discord.Member, *, reason: None):
    # if reason == None:
        # reason = "This user was banned by " + ctx.message.author.name

    # await member.ban(reason=reason)

@bot.command()
@commands.has_any_role("Admin", "Moderator", "Helper")
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)

@bot.command()
@commands.has_any_role("Admin", "Moderator", "Helper")
async def kick(ctx, member_id: int, *, reason=None):
    member = ctx.guild.get_member(member_id)
    if member is not None:
        await member.kick()
# async def kick(ctx, member:discord.Member, *, reason: None):
    # if reason == None:
        # reason = "This user was kicked by " + ctx.message.author.name

    # await member.kick(reason=reason)

@bot.command()
@commands.has_any_role("Admin", "Moderator", "Helper")
async def mute(ctx, member:discord.Member, timelimit):
    if "s" in timelimit:
        gettime = timelimit.strip("s")
        if int(gettime) > 2419000:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else: 
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    elif "m" in timelimit:
        gettime = timelimit.strip("m")
        if int(gettime) > 40320:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else: 
            newtime = datetime.timedelta(minutes=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    elif "h" in timelimit:
        gettime = timelimit.strip("h")
        if int(gettime) > 672:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else: 
            newtime = datetime.timedelta(hours=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    elif "d" in timelimit:
        gettime = timelimit.strip("d")
        if int(gettime) > 28:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else: 
            newtime = datetime.timedelta(days=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)

@bot.command()
@commands.has_any_role("Admin", "Moderator", "Helper")
async def unmute(ctx, member:discord.Member):
    await member.edit(timed_out_until=None)

@bot.command()
@commands.has_any_role("Admin", "Moderator", "Helper")
async def help(ctx):
    embed = discord.Embed(title="Ayuda", description="Este comando muestra todos los comandos disponibles para usar con Paladin HK. Usar prefijo **>** para todos los comandos", color=0xF0E68C)
    embed.add_field(name=">ban", value="Usa este comando para banear. >ban USER ID", inline=False)
    embed.add_field(name=">unban", value="Usa este comando para desbanear. >unban USER ID", inline=False)
    embed.add_field(name=">kick", value="Usa este comando para para echar a alguien. >kick USER ID", inline=False)
    embed.add_field(name=">mute", value="Usa este comando para silenciar a alguien. >mute USER ID", inline=False)
    embed.add_field(name=">unmute", value="Usa este comando para quitar el silencio a alguien. >unmute USER ID", inline=False)
    embed.add_field(name=">useri", value="Usa este comando para obtener información sobre algún usuario. >useri USER ID NO FUNCIONAL", inline=False)
    embed.set_footer(text="Bot made by DNX for HK")
    await ctx.send(embed=embed)

bot.run("TOKEN")