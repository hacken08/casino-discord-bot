import time

from snake_water_gun.menu import main_menu as mm
from snake_water_gun import custmizable as custm
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
        msg = await ctx.send(f'**|**  **{ctx.author.name}**  already **joined** this casino :handshake:')
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
        await ctx.send(
            f' **|**  **{ctx.author.name}** have **joined** our casino, **successfully**   :white_check_mark:')

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
        msg = await ctx.send('❌ **|**  Your account **Not Found**. Please **Join** casino first  😿')
        time.sleep(custm.ERROR_MSG_INTERVEL)

        await msg.delete()
        return

    data = db.get_plyr_data(ctx.user.username)
    bal = data['balance']['value']

    show_bal = f'**| {ctx.author.name}** account balance = **{bal} 💰 **'
    await ctx.channel.send(show_bal)


if __name__ == '__main__':
    client.start()
