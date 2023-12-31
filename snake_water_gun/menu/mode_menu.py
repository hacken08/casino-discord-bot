
import time
import interactions as interact

from snake_water_gun.lib import game_func as gm_f
from snake_water_gun.lib.single_player import choices
from bot import client


STYLE = interact.ButtonStyle.SECONDARY  # Button Style

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
        ]
    )
]

@client.component('single_player')
async def single_player(ctx: interact.CommandContext):

    #  Deleting mode option
    new_msg = await ctx.channel.get_history()
    await new_msg[0].delete()

    # Counting.../
    # game_start = await ctx.send('# Game starts in **<>**'.title())
    #
    # await gm_f.countdown_timer(ctx, 3, game_start)
    # new_msg = await ctx.channel.get_history()

    # Giving choices.../
    # await new_msg[0].delete()
    await  ctx.send(components=choices)


@client.component('multi_player')
async def multi_player(ctx: interact.CommandContext):

    #  Deleting mode option
    new_msg = await ctx.channel.get_history()
    await new_msg[0].delete()

    await ctx.send('Coming soon')


