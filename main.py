import time

import interactions
from bot import client

from snake_water_gun.menu import main_menu as mm
import database as db




CURRENT_PLAYER = ''

#  ........ Creating new player ........../
@client.command(description='join with casino')
async def join(ctx: interactions.CommandContext):
    user = ctx.user
    new = db.is_plyr_new(user.username)

    if not new:
        await ctx.send(f'**|**  **{ctx.author.name}**  already **joined** this casino :handshake:')
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
        await ctx.send(f' **|**  **{ctx.author.name}** have **joined** our casino, **successfully**   :white_check_mark:')
    except Exception as e:
        await ctx.send('⛔ **|**  Something went wrong ')
        print(e)



# ......... Running game ............/
@client.command(description='To play snake-water-game')
async def snake_water_gun(ctx: interactions.CommandContext):
    """
    To play snake-water
    """
    global CURRENT_PLAYER
    CURRENT_PLAYER = ctx.user.username

    #  Checking if user exits
    if db.is_plyr_new(ctx.user.username):
        await ctx.send('❌**|**   Player **Not Found**. Please **Join** casino first  😿')
        time.sleep(5)

        new_msg = await ctx.channel.get_history()
        await new_msg[0].delete()
        return

    #  Starting game
    await ctx.send(f'# Snake Water Gun :-', components=mm.menu_options)



@client.command(description='To play slot machine')
async def slot(ctx: interactions.CommandContext):
    """
    To play slot machine
    """
    await ctx.send('This game will come soon')



@client.command(description='To play coin flip')
async def coin_flip(ctx: interactions.CommandContext):
    """
    To play slot machine
    """
    await ctx.send('This game will come soon')


#  ......... Additional commands ........./
@client.command(description="To know current balance of yours")
async def balance(ctx: interactions.CommandContext):
    """
    to get the current balance of user
    """
    #  Checking if user exits
    if db.is_plyr_new(ctx.user.username):
        await ctx.send('❌ **|**  Your account **Not Found**. Please **Join** casino first  😿')
        return

    data = db.get_plyr_data(ctx.user.username)
    bal = data['balance']['value']

    show_bal = f'**| {ctx.author.name}** account balance = **{bal} 💰 **'
    await ctx.channel.send(show_bal)


def is_current_user(ctx):
    if ctx.user.username == CURRENT_PLAYER:
        return True
    else:
        return False



if __name__ == '__main__':
    client.start()

