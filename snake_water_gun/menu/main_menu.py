
import time
import interactions
from bot import client
from main import is_current_user

from .setting_menu import  settings_option
from .mode_menu import  mode_option
# from snake_water_gun.Game_functions import main as mm


STYLE = interactions.ButtonStyle.SECONDARY  #  Button Style

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
                    label="Reset score".title(),
                    custom_id="reset",
                    style=STYLE,
            ),
            interactions.Button(
                    label="Quite game".title(),
                    custom_id="quite_game",
                    style=interactions.ButtonStyle.DANGER,
            ),
        ]
    )
)


#  --- Main menu actions ----/
@client.component('play_game')
async def _play_game(ctx: interactions.CommandContext):

    if not is_current_user(ctx):
        await ctx.send('❌**|** You can\'t **interfere**')
        return

    await  ctx.send('# Mode:-',components=mode_option)


@client.component('how_to_play')
async def _instruction(ctx: interactions.CommandContext):
    with open('description.txt', 'r') as f:
        await ctx.send(f.read())


@client.component('settings_menu')
async def _open_settings_menu(ctx: interactions.CommandContext):
    await ctx.send(components=settings_option)


@client.component('reset')
async def _to_reset_game(ctx: interactions.CommandContext):
    await ctx.send('Resetting game...')
    time.sleep(1)
    await ctx.send('Game reset successfully')


@client.component('quite_game')
async def _quite_game(ctx: interactions.CommandContext):
    await ctx.send("Quiting game...")
    time.sleep(1)
    await ctx.send("Game quited")
