
import interactions
from bot import client
# from main_menu import menu_options

STYLE = interactions.ButtonStyle.SECONDARY  # Button Style
play_style = 'Buttons'

#  ..... Settings options:- ...../
settings_option = [
    interactions.ActionRow(
        components=[
            interactions.Button(
                    label=f"Play style {play_style}".title(),
                    custom_id='next_round_wait',
                    style=STYLE,
            ),
            interactions.Button(
                    label="Start countdown".title(),
                    custom_id='start_countdown',
                    style=STYLE,
            ),
            interactions.Button(
                    label="Go back".title(),
                    custom_id='back',
                    style=STYLE,
            )
        ]
    )
]

# ..... settings Action:- ...../
@client.component("next_round_wait")
async def next_round_wait(ctx: interactions.CommandContext):
    await ctx.send("Waiting for next round...")


@client.component("start_countdown")
async def to_start_countdown(ctx: interactions.CommandContext):
    await ctx.send("countdown...")


# @client.command(name="back")
# async def to_go_back(ctx: interactions.CommandContext):
#     await ctx.send('# Main Menu:-\n', components=menu_options)


