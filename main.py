import interactions
import time

from snake_water_gun.menu import main_menu as mm
from snake_water_gun.lib.players import Player
from snake_water_gun.lib import multi_player as mplr

from snake_water_gun import changeable as custm
from snake_water_gun import basin_funct as bs_f

from bot import client
import database as db



plyr1 = Player()
plyr2 = Player()


#  ........ Creating new player ........../
@client.command(description='join with casino')
async def join(ctx: interactions.CommandContext):
    user = ctx.user
    new = db.is_plyr_new(user.username)

    if not new:
        await ctx.send(custm.ALRDY_PLYR_JOIN.replace('<>', ctx.author.name))
        # time.sleep(ERROR_MSG_INTERVAL)
        #
        # await msg.delete()
        return

    try:
        db.create_player(
            player_uid=user.username,
            name=ctx.author.name,
            email=user.email,
            avatar=user.avatar_url,
            bot=user.bot,
            date=time.ctime(),
        )
        await ctx.send(custm.NEW_PLYR_JOIN.replace('<>', ctx.author.user))

    except Exception as e:
        msg = await ctx.send('⛔ **|**  Something went wrong ')
        time.sleep(custm.ERROR_MSG_INTERVEL)

        await msg.delete()
        print(e)


# ......... Running game ............/
@client.command(description='To play snake-water-game')
async def snake_water_gun(ctx: interactions.CommandContext):
    """
    To play snake-water
    """
    global plyr1

    #  Checking if user exits
    if await bs_f.user_validation(ctx, new_player=True):
        return

    plyr1 = Player(ctx.author.name, ctx.user.username, ctx.user.mention)

    #  Starting game
    mm.select_and_del = await ctx.send(f'# Snake Water Gun :-', components=mm.menu_options)


@client.command(description='To play slot machine')
async def slot(ctx: interactions.CommandContext):
    """
    To play slot machine
    """
    msg = await ctx.send('This game will come soon')
    time.sleep(custm.ERROR_MSG_INTERVEL)
    await msg.delete()


@client.command(description='To play coin flip')
async def coin_flip(ctx: interactions.CommandContext):
    """
    To play slot machine
    """
    msg = await ctx.send('This game will come soon')
    time.sleep(custm.ERROR_MSG_INTERVEL)
    await msg.delete()


#  ......... Additional commands ........./
@client.command(description="To know current balance of yours")
async def balance(ctx: interactions.CommandContext):
    """
    to get the current balance of user
    """
    #  Checking if user exits
    if db.is_plyr_new(ctx.user.username):
        msg = await ctx.send(custm.ACCOUNT_NOT_FOUND)
        time.sleep(custm.ERROR_MSG_INTERVEL)

        await msg.delete()
        return

    data = db.get_plyr_data(ctx.user.username)
    bal = data['balance']['value']

    show_bal = f'**| {ctx.author.name}** account balance = **{bal} 💰 **'
    await ctx.channel.send(show_bal)


@client.command(
    description='To play coin flip',
    options=[
        interactions.Option(
            name='second_player',
            description='Tag second player',
            required=True,
            type=interactions.OptionType.STRING  # Use STRING type for mentions
        ),
    ]
)
async def add_player(ctx: interactions.CommandContext, second_player: str):
    global plyr1
    global plyr2
    try:
        joining_msg = await ctx.send(custm.CHECKING_PLYR2)
        plyr1 = Player(ctx.author.name, ctx.user.username, ctx.user.mention)

        # Extracting the user ID from the mention
        user_id = int(second_player[2:-1])

        # Getting the Member object using the user ID
        mentioned_member = await ctx.guild.get_member(user_id)

        # Validation user and second player
        if await bs_f.user_validation(ctx, interfere=True, new_player=True):
            return
        elif await bs_f.second_plyr_validation(ctx, mentioned_member, joining_msg):
            return

        # Joining second player to play with
        plyr2 = Player(mentioned_member.name, mentioned_member.user.username, mentioned_member.mention)
        await joining_msg.edit(custm.SECOND_PLYR_JOIN.replace('<>', plyr2.name))
        custm.SECOND_PLYR = mentioned_member.user.username

    except Exception as e:
        print(e)


if __name__ == '__main__':
    client.start()
