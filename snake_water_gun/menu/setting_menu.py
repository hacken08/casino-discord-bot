
import interactions
from bot import client
from snake_water_gun.menu import main_menu as mm
# from main_menu import menu_options

STYLE = interactions.ButtonStyle.SECONDARY  # Button Style
select_and_del = interactions.api.models.message.Message()
menu_option = ()


# .............. Customizable user setting Variables ..............
play_style = ['Buttons', "Text Command"]

#  ..... Settings options:- ...../
settings_option = [
    interactions.ActionRow(
        components=[
            interactions.Button(
                    label=f"Play style {play_style[0]}".title(),
                    custom_id='next_round_wait',
                    style=STYLE,
            ),
            interactions.Button(
                    label="Start countdown".title(),
                    custom_id='start_countdown',
                    style=STYLE,
            ),
            interactions.Button(
                label="back".title(),
                custom_id='back',
                style=interactions.ButtonStyle.DANGER,
            ),
        ]
    )
]

# ..... settings Action ...../
@client.component("next_round_wait")
async def next_round_wait(ctx: interactions.CommandContext):
    await select_and_del.delete()

    await ctx.send("Waiting for next round...")


@client.component("start_countdown")
async def to_start_countdown(ctx: interactions.CommandContext):
    await select_and_del.delete()

    await ctx.send("countdown...")


@client.command(name="back")
async def to_go_back(ctx: interactions.CommandContext):
    global select_and_del

    await select_and_del.delete()
    mm.select_and_del = await ctx.send('# Main Menu:-\n', components=menu_option)


