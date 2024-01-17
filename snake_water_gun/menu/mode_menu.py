
import time
import interactions as interact

from snake_water_gun.lib import single_player as ch
from snake_water_gun import changeable as custm
from snake_water_gun import basin_funct as bs_f

from bot import client



STYLE = interact.ButtonStyle.SECONDARY  # Button Style
select_and_del = interact.api.models.message.Message()



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

    if await bs_f.user_validation(ctx, new_player=True):
        return

    await select_and_del.delete()
    ch.select_and_del = await ctx.send(components=ch.choices)


@client.component('multi_player')
async def multi_player(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, new_player=True):
        return

    await select_and_del.delete()
    await ctx.send('Coming soon')



@client.component('back')
async def back(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, new_player=True):
        return

    await select_and_del.delete()  # Deleting old menu

    from snake_water_gun.menu import main_menu as mm
    mm.select_and_del = await ctx.send('# Menu:-\n', components=mm.menu_options)
