import random
# import time
import interactions as interact

from snake_water_gun.lib import game_func as gm_f
from snake_water_gun.lib import game_style as gm_s
from snake_water_gun import basin_funct as bs_f

# from snake_water_gun.menu import setting_menu as sm
from snake_water_gun.menu import main_menu as mm

from bot import client


select_and_del = interact.api.models.message.Message()
rounds = 1

STYLE = interact.ButtonStyle.SUCCESS
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


#  ................. Playing  .................
async def pvc(ctx: interact.CommandContext, key_cio: int):
    """
    Args:
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
    plyr_choice = gm_s.choice[key_cio]
    cpu_choice = gm_f.cpu_choice(plyr_choice)


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
        plyr_choice=plyr_choice,
        cpu_choice=cpu_choice
    )
    await gm_f.bal_update(
        ctx=ctx,
        bal=gm_s.betting_amt,
        winner_val=winner[1],
        plyr_choice=plyr_choice,
        cpu_choice=cpu_choice
    )

    #  Presenting Winner and Win/Loss balance.../
    winner_msg = await original_msg.edit(f'{check_msg.content}\n |  {winner[0]}')

    if winner[1] == plyr_choice:
        await original_msg.edit(f'{winner_msg.content}'
                                f'\n |          :trophy:   ***Winner :***     {plyr_name}  |'
                                f'\n |          :moneybag:   ***Loot :***     {gm_s.betting_amt[plyr_choice]}rs')
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')

        # await gm_f.countdown_timer(ctx, 3, next_round)
        await gm_f.update_stats(ctx, wins=1)  # Updating stats.../

    elif winner[1] == cpu_choice:
        await original_msg.edit(f'{winner_msg.content}'
                                f'\n |          :trophy:   ***Winner :***     CPU|'
                                f'\n |          ❌   ***Lost :***     {gm_s.betting_amt[plyr_choice]}rs')
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
    await pvc(ctx, 1)


#  .................... Choice water ..................../
@client.component('water')
async def water(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    await pvc(ctx, 2)


#  .................... Choice gun ..................../
@client.component("gun")
async def gun(ctx: interact.CommandContext):
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    await pvc(ctx, 3)


#  .................... Quite ..................../
@client.component('quite')
async def quite(ctx: interact.CommandContext):
    global rounds
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    await select_and_del.delete()
    mm.select_and_del = await ctx.send('# Main Menu:-\n', components=mm.menu_options)
