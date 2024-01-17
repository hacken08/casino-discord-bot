import interactions

from snake_water_gun import basin_funct as bs_f
from snake_water_gun.lib import single_player as sp

from bot import client

# from main_menu import menu_options


STYLE = interactions.ButtonStyle.SECONDARY  # Button Style
select_and_del = interactions.api.models.message.Message()

# .............. Customizable user setting Variables ..............
play_style = ['Buttons', "Text Command"]
choices_style = 'snake water gun'
change_style = 'Rock Paper scissors'

#  ..... Settings options:- ...../
setting_option = [
    interactions.ActionRow(
        components=[
            interactions.Button(
                label=f"Play style {play_style[0]}".title(),
                custom_id='next_round_wait',
                style=STYLE,
            ),
            interactions.Button(
                label=change_style.title(),
                custom_id='cho_style',
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


def chck_style(x):
    global choices_style
    global setting_option
    global change_style

    #  ..... Settings options:- ...../
    change_style = choices_style
    choices_style = x

    setting_option = [
        interactions.ActionRow(
            components=[
                interactions.Button(
                    label=f"Play style {play_style[0]}".title(),
                    custom_id='play_style',
                    style=STYLE,
                ),
                interactions.Button(
                    label=change_style.title(),
                    custom_id='cho_style',
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

,,
# ..... settings Action ...../
@client.component('play_style')
def change_ply_style(ctx: interactions.CommandContext):
    pass


@client.component("cho_style")
async def choice_style(ctx: interactions.CommandContext):
    global select_and_del
    global choices_style

    if await bs_f.user_validation(ctx, new_player=True):
        return
    await select_and_del.delete()

    #  Changing Value by calling out function
    changed = sp.choice_style(choices_style)

    #  Sending changed message
    await ctx.send(f':sparkles: Your **Choice Style** Change to __*{changed}*__ **| Successfully**!  '
                   f':white_check_mark:')
    chck_style(changed)

    #  Going back to menu
    from snake_water_gun.menu import main_menu as mm
    mm.select_and_del = await ctx.send('# Menu:-\n', components=mm.menu_options)


@client.component("back")
async def to_go_back(ctx: interactions.CommandContext):
    global select_and_del

    # if await bs_f.user_validation(ctx, new_player=True):
    #     return

    await select_and_del.delete()  # Deleting old menu

    from snake_water_gun.menu import main_menu as mm
    mm.select_and_del = await ctx.send('# Menu:-\n', components=mm.menu_options)
