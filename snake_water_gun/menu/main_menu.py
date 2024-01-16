import interactions
import time
import main as m

from snake_water_gun.menu import mode_menu as mm
from snake_water_gun.menu import setting_menu as sm
from snake_water_gun import basin_funct as bs_f

from .txt import description
from bot import client
from .. import custmizable as custm

# from snake_water_gun.Game_functions import main as mm


STYLE = interactions.ButtonStyle.SECONDARY  # Button Style
select_and_del = interactions.api.models.message.Message()

#  --Menu options:- .../
menu_options = (
    interactions.ActionRow(
        components=[
            interactions.Button(
                label='start game'.title(),
                custom_id="play_game",
                style=STYLE,
            ),
            interactions.Button(
                label="How to Play".title(),
                custom_id="how_to_play",
                style=STYLE,
            ),
            interactions.Button(
                label="settings".title(),
                custom_id="settings_menu",
                style=STYLE,
            ),
            interactions.Button(
                label="stats".title(),
                custom_id="stats",
                style=STYLE,
            ),
            interactions.Button(
                label="Quite".title(),
                custom_id='quite',
                style=interactions.ButtonStyle.DANGER,
            ),
        ]
    )
)


#  --- Main menu actions ----/
@client.component('play_game')
async def _play_game(ctx: interactions.CommandContext):
    global select_and_del

    #  Validating player before executing
    validate = await bs_f.user_validation(ctx, new_player=True)
    if validate:
        return

    # Deleting previous msg after selection
    await select_and_del.delete()
    mm.select_and_del = await ctx.send('# Mode:-', components=mm.mode_option)


@client.component('how_to_play')
async def _instruction(ctx: interactions.CommandContext):
    global select_and_del

    #  Validating player before executing
    validate = await bs_f.user_validation(ctx, new_player=True)
    if validate:
        return

    # Deleting previous msg after selection
    await select_and_del.delete()

    await ctx.user.get_dm_channel().send(description)


@client.component('settings_menu')
async def _open_settings_menu(ctx: interactions.CommandContext):
    global select_and_del

    #  Validating player before executing
    validate = await bs_f.user_validation(ctx, new_player=True)
    if validate:
        return

    # Deleting previous msg after selection
    await select_and_del.delete()

    sm.select_and_del = await ctx.send(components=sm.setting_option)


@client.component('stats')
async def _to_reset_game(ctx: interactions.CommandContext):
    global select_and_del

    #  Validating player before executing
    validate = await bs_f.user_validation(ctx, new_player=True)
    if validate:
        return

    # Deleting previous msg after selection
    await select_and_del.delete()

    await ctx.send('Working on this feature')
    await ctx.send('Game reset successfully')

    await ctx.send(components=menu_options)


@client.component('quite')
async def _quite_game(ctx: interactions.CommandContext):
    global select_and_del

    #  Validating player before executing
    if await bs_f.user_validation(ctx, new_player=True):
        return

    # Deleting previous msg after selection
    await select_and_del.delete()
    m.CURRENT_PLAYER = ''

    time.sleep(1)
    await ctx.send(
        f"{ctx.author.name}"
        f"\nWin : "
        f"\nLoss : "
        f"\nCurrent Balance : "
        f"\n quited successfully"
    )
