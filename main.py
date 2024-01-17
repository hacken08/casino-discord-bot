import time

from snake_water_gun.menu import main_menu as mm
from snake_water_gun import changeable as custm
from snake_water_gun import basin_funct as bs_f

import interactions
from bot import client
import database as db


#  ........ Creating new player ........../
@client.command(description='join with casino')
async def join(ctx: interactions.CommandContext):
    user = ctx.user
    new = db.is_plyr_new(user.username)

    if not new:
        msg = await ctx.send(custm.ALRDY_PLYR_JOIN.replace('<>', ctx.author.name))
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
    custm.CURRENT_PLAYER = ctx.user.username

    #  Checking if user exits
    if await bs_f.user_validation(ctx, new_player=True):
        return

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
async def add_plry(ctx: interactions.CommandContext, second_player: str):

    try:
        # Extracting the user ID from the mention
        user_id = int(second_player[2:-1])

        # Getting the Member object using the user ID
        mentioned_member = await ctx.guild.get_member(user_id)

        if mentioned_member.user.username == custm.SECOND_PLYR:
            await ctx.send(custm.SECOND_PLYR_EXISTS.replace('<>', mentioned_member.name))
            return

        elif mentioned_member.user.username == ctx.user.username:
            await ctx.send(custm.CANT_ADD_YOU)
            return

        elif mentioned_member:
            custm.SECOND_PLYR = mentioned_member.user.username
            await ctx.send(custm.SECOND_PLYR_JOIN.replace('<>', mentioned_member.name))
            print(custm.SECOND_PLYR)

        else:
            await ctx.send('User not found!')

    except (TypeError, ValueError) as e:
        await ctx.send(custm.PLYR_NOT_MENTION)


if __name__ == '__main__':
    client.start()
