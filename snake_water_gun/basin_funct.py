import interactions as interacts

from snake_water_gun.changeable import CURRENT_PLAYER
from snake_water_gun import changeable as custm

import database as db
import main as m

def is_current_user(ctx):
    if ctx.user.username == CURRENT_PLAYER:
        return True
    else:
        return False


async def user_validation(
        ctx,
        new_player=False,
        interfere=False,
):
    """
    Checks if the
    Args:
        ctx: context
        new_player: bool
        interfere: bool

    Returns: True if any of the mention args is right

    """

    try:
        #  New player validations ..../
        if new_player:
            if db.is_plyr_new(ctx.user.username):
                await ctx.send(custm.PLYR_NOT_FOUND)
                return True
            else:
                return False


        #  Player interfering ..../
        elif interfere:
            if ctx.user.username is not custm.CURRENT_PLAYER and ctx.user.username is not custm.SECOND_PLYR:
                await ctx.send(custm.PLYR_NOT_FOUND)
                return True
            else:
                return False

        #  If args not pass
        else:
            print('Nothing to validate about user')

    except Exception as e:
        print(e)


async def second_plyr_validation(ctx, mentioned_member, joining_msg):
    if not mentioned_member:
        await ctx.send('User not found!')
        return True

    elif mentioned_member.user.username == m.plyr2.username:
        await joining_msg.edit(custm.SECOND_PLYR_EXISTS.replace('<>', mentioned_member.name))
        return True

    elif mentioned_member.user.username == ctx.user.username:
        await joining_msg.edit(custm.CANT_ADD_YOU)
        return True

    # elif db.is_plyr_new(mentioned_member.user.username):
    #     await ctx.send(custm.PLYR_NOT_FOUND)
    #     return True

    return False


async def validate_choices(ctx):
    if m.plyr1.choice == '':
        mention = m.plyr1.mention
        msg = custm.PLAYER_MAKE_CHOICE.replace('<p1>', m.plyr2.name).replace('<p2>', mention)
        await ctx.send(msg)
        return True

    elif m.plyr2.choice == '':
        mention = m.plyr2.mention
        msg = custm.PLAYER_MAKE_CHOICE.replace('<p1>', m.plyr1.name).replace('<p2>', mention)
        await ctx.send(msg)
        return True

    return False


def players_choice(ctx, key: int):
    if ctx.user.username == m.plyr1.username:
        m.plyr1.take_choice(key)

    elif ctx.user.username == m.plyr2.username:
        m.plyr2.take_choice(key)
