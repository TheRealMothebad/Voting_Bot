#required imports
import discord
from discord.ext import commands  # This is the part of discord.py that helps us build bots
from discord.ext.commands.converter import EmojiConverter
from election import STAR
from tok import DontStealMyToken

#functionality specific imports

#local imports
import election
import ballot

#https://discord.com/oauth2/authorize?client_id=899507257212010557&scope=bot

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    print(str(user) + " reacted to \"" + str(reaction.message)+ "\" with:" + str(emoji))


@bot.command(name="election", aliases=["e"])
async def election(ctx, *msg): #style, *msg):
    election.active = STAR(msg)

@bot.command(name="vote", aliases=["v"])
async def vote(ctx, *msg):
    createBallot = True
    for i in election.active.ballots:
        if i.voter == msg.author:
            createBallot = False
            break
    if createBallot:
        election.active.votes.update({msg.author : ballot(msg.author)})
    for i in range(0, msg, 2):
        election.active.votes[msg.author].update({msg[i] : msg[i+1]})

async def star_react(ctx):
    candidates = ["candiate 1", "candidate 2", "candidate 3"]
    reactEmojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    for i in candidates:
        message = await ctx.send(i)
        for e in reactEmojis:
            await message.add_reaction(e)

@bot.command(name="gencan")
async def gen_can(ctx):
    star_react(ctx)
    

@bot.command(name="tabulate", aliases=["t", "tab", "count"])
async def tab(ctx):
    tab = ballot.tabulate(election.active.votes)
    results = ballot.finalists(tab, election.active.votes)
    await ctx.send(str(results))

@bot.command(name="stop")
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("seeya")
    await ctx.bot.close()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.NotOwner):
        await ctx.send("You are not cool enough to do that.")

bot.run(DontStealMyToken)