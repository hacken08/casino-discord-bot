
import interactions as interacts

from snake_water_gun.changeable import  CURRENT_PLAYER
import database as db
from snake_water_gun import changeable as custm


def is_current_user(ctx):
    if ctx.user.username == CURRENT_PLAYER:
        return True
    else:
        return False


async def user_validation(
        ctx: interacts.CommandContext,
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
            if not ctx.user.username == custm.CURRENT_PLAYER:
                await ctx.send(custm.PLYR_NOT_FOUND)
                return True
            else:
                return False

        #  If args not pass
        else:
            print('Nothing to validate about user')

    except Exception as e:
        print(e)


async def second_plyr_validation(ctx, mentioned_member):

    if not mentioned_member:
        await ctx.send('User not found!')
        return True

    elif mentioned_member.user.username == custm.SECOND_PLYR:
        await ctx.send(custm.SECOND_PLYR_EXISTS.replace('<>', mentioned_member.name))
        return True

    elif mentioned_member.user.username == ctx.user.username:
        await ctx.send(custm.CANT_ADD_YOU)
        return True

    return False
