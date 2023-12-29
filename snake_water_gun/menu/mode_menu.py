import time

import interactions as interact
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

async def countdown_timer(ctx, seconds_left, countdown_msg: str):
    send = countdown_msg.replace('<>', str(seconds_left))
    new_msg = await ctx.send(send)

    for i in range(seconds_left, 0, -1):
        edit_msg = countdown_msg.replace('<>', f'{str(i-1)}')

        await new_msg.edit(edit_msg)
        time.sleep(0.5)

    return new_msg


@client.component('single_player')
async def single_player(ctx: interact.CommandContext):

    #  Deleting mode option
    new_msg = await ctx.channel.get_history()
    await new_msg[0].delete()

    await countdown_timer(ctx, 5, 'Game starts in ** <> **'.title())


@client.component('multi_player')
async def multi_player(ctx: interact.CommandContext):

    #  Deleting mode option
    new_msg = await ctx.channel.get_history()
    await new_msg[0].delete()

    await countdown_timer(ctx, 4, 'Game starts in ** <> **'.title())


