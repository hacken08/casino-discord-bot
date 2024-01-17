import random
# import time
import interactions as interact

from snake_water_gun import basin_funct as bs_f
from snake_water_gun.lib import game_func as gm_f

# from snake_water_gun.menu import setting_menu as sm
from snake_water_gun.menu import main_menu as mm

from bot import client

choice = {
    1: ':snake: snake',
    2: ':ocean: water',
    3: ':gun: gun',
}
betting_amt = {
    choice[1]: 200,
    choice[2]: 500,
    choice[3]: 700
}

STYLE = interact.ButtonStyle.SUCCESS
select_and_del = interact.api.models.message.Message()
rounds = 1

choices = [
    interact.ActionRow(
        components=[
            interact.Button(
                label=f'Snake / 200rs'.title(),
                custom_id="snake",
                style=STYLE,
            ),
            interact.Button(
                label=f'Water / 500rs'.title(),
                custom_id="water",
                style=STYLE,
            ),
            interact.Button(
                label=f'Gun / 700rs'.title(),
                custom_id="gun",
                style=STYLE,
            ),
            interact.Button(
                label='Exist to main menu'.title(),
                custom_id="quite",
                style=interact.ButtonStyle.DANGER,
            ),
        ]
    )
]


def choice_style(choices_style):
    global choice
    global choices
    global betting_amt

    display = ''
    if choices_style == 'snake water gun':
        choice = {
            1: ':newspaper2: papers',
            2: ':rock: rocks',
            3: ':scissors: scissors',
        }
        choices_style = 'rock papers scissor'
        display = 'Papers Rocks Scissors'

    elif choices_style == 'rock papers scissor':
        choice = {
            1: ':snake: snake',
            2: ':ocean: water',
            3: ':gun: gun',
        }
        choices_style = 'snake water gun'
        display = 'Snake Water Gun'

    betting_amt = {
        choice[1]: 200,
        choice[2]: 500,
        choice[3]: 700
    }

    display = display.split(' ')
    choices = [
        interact.ActionRow(
            components=[
                interact.Button(
                    label=f'{display[0]} / 200rs'.title(),
                    custom_id="snake",
                    style=STYLE,
                ),
                interact.Button(
                    label=f'{display[1]} / 500rs'.title(),
                    custom_id="water",
                    style=STYLE,
                ),
                interact.Button(
                    label=f'{display[2]} / 700rs'.title(),
                    custom_id="gun",
                    style=STYLE,
                ),
                interact.Button(
                    label='Exist to main menu'.title(),
                    custom_id="quite",
                    style=interact.ButtonStyle.DANGER,
                ),
            ]
        )
    ]
    return choices_style


#  ................. Playing  .................
async def playing(ctx: interact.CommandContext, key_cio: int, second_plyr=False):
    """
    Args:
        second_plyr:
        ctx:
        key_cio (object):
    """
    global rounds
    global select_and_del

    plyr_name = ctx.author.name
    if len(plyr_name) > 7:
        plyr_name = plyr_name[:7] + ' . . .'

    #  Round Counting.../
    original_msg = await ctx.send(f'╭─────── :dagger:  **Round {rounds}** :dagger:    ───────╮')

    #  Player input.../
    cpu_choice = ''
    plyr_choice = ''

    if not second_plyr:
        plyr_choice = choice[key_cio]
        cpu_choice = gm_f.cpu_choice(plyr_choice, choice)
    elif second_plyr:
        pass

    # Player vs CPU.../
    msg = (f'{original_msg.content}'
           f'\n |    **↓ {plyr_name} ↓                            ↓ CPU ↓**'
           f'\n |   {plyr_choice}           *** __vs__***         {cpu_choice}')
    vs_msg = await original_msg.edit(msg)

    #  Checking and Updating results.../
    check_msg = await original_msg.edit(f'{vs_msg.content}'
                                        f'\n |  ───── :gear: *Checking Result* :gear: ───── |'
                                        f'\n |'
                                        )

    winner = gm_f.chk_result(
        CHOICE=choice,
        plyr_choice=plyr_choice,
        cpu_choice=cpu_choice
    )
    await gm_f.bal_update(
        ctx=ctx,
        bal=betting_amt,
        winner_val=winner[1],
        plyr_choice=plyr_choice,
        cpu_choice=cpu_choice
    )

    #  Presenting Winner and Win/Loss balance.../
    winner_msg = await original_msg.edit(f'{check_msg.content}\n |  {winner[0]}')

    if winner[1] == plyr_choice:
        await original_msg.edit(f'{winner_msg.content}'
                                f'\n |          :trophy:   ***Winner :***     {plyr_name}  |'
                                f'\n |          :moneybag:   ***Loot :***     {betting_amt[plyr_choice]}rs')
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')

        # await gm_f.countdown_timer(ctx, 3, next_round)
        await gm_f.update_stats(ctx, wins=1)  # Updating stats.../

    elif winner[1] == cpu_choice:
        await original_msg.edit(f'{winner_msg.content}'
                                f'\n |          :trophy:   ***Winner :***     CPU|'
                                f'\n |          ❌   ***Lost :***     {betting_amt[plyr_choice]}rs')
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')
        # await gm_f.countdown_timer(ctx, 3, next_round)

        await gm_f.update_stats(ctx, loses=1)  # Updating stats.../

    elif winner[1] == 'draw':
        # next_round = await original_msg.edit(f"{winner_msg.content}\n |          :arrows_counterclockwise:   *Next
        # Round in **3** seconds* | \n╰───────────────────────╯")
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')
        # await gm_f.countdown_timer(ctx, 5, next_round)

        await gm_f.update_stats(ctx, draws=1)  # Updating stats.../

    #  Next Round.../
    rounds += 1
    select_and_del = await ctx.send(components=choices)


#  .................... choice snake ..................../
@client.component('snake')
async def water(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    await playing(ctx, 1)


#  .................... Choice water ..................../
@client.component('water')
async def water(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    await playing(ctx, 2)


#  .................... Choice gun ..................../
@client.component("gun")
async def gun(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    await playing(ctx, 3)


#  .................... Choice gun ..................../
@client.component('quite')
async def quite(ctx: interact.CommandContext):
    global rounds
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    mm.select_and_del = await ctx.send('# Main Menu:-\n', components=mm.menu_options)
