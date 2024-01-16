
import interactions as interacts

from snake_water_gun.custmizable import  CURRENT_PLAYER
import database as db
from snake_water_gun import custmizable as custm


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

