
import time
import interactions as interact

from snake_water_gun.lib import game_func as gm_f
from snake_water_gun.lib import single_player as ch
from bot import client
import main as m

STYLE = interact.ButtonStyle.SECONDARY  # Button Style
select_and_del = interact.api.models.message.Message()
menu_option = ()


mode_option = [
    interact.ActionRow(
        components=[
            interact.Button(
                label='player vs cpu'.title(),
                custom_id="single_player",
                style=STYLE,
            ),
            interact.Button(
                label='player vs player'.title(),
                custom_id="multi_player",
                style=STYLE,
            ),
            interact.Button(
                label="Go Back".title(),
                custom_id='back',
                style=interact.ButtonStyle.DANGER,
            ),
        ]
    )
]

@client.component('single_player')
async def single_player(ctx: interact.CommandContext):
    global select_and_del
    await select_and_del.delete()

    ch.select_and_del = await ctx.send(components=ch.choices)


@client.component('multi_player')
async def multi_player(ctx: interact.CommandContext):
    global select_and_del
    await select_and_del.delete()

    msg = await ctx.send('Coming soon')
    time.sleep(m.ERROR_MSG_INTERVEL)


@client.component('back')
async def multi_player(ctx: interact.CommandContext):
    global select_and_del
    await select_and_del.delete()  # Deleting old menu

    await ctx.send('# Main Menu:-\n', components=menu_option)

