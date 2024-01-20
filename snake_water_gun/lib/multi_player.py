import interactions as interacts

from snake_water_gun.lib import game_func as gm_f
from snake_water_gun.lib import game_style as gm_s
from snake_water_gun.lib.players import Player

from snake_water_gun.menu import main_menu as mm
from snake_water_gun import basin_funct as bs_f
from snake_water_gun import changeable as custom

from bot import client
import main as m


select_and_del = interacts.api.models.message.Message()
plry1_choice = ''
plry2_choice = ''
rounds = 1

STYLE = interacts.ButtonStyle.SUCCESS
choices = [
    interacts.ActionRow(
        components=[
            interacts.Button(
                label=f'Snake / 200rs'.title(),
                custom_id="m_snake",
                style=STYLE,
            ),
            interacts.Button(
                label=f'Water / 500rs'.title(),
                custom_id="m_water",
                style=STYLE,
            ),
            interacts.Button(
                label=f'Gun / 700rs'.title(),
                custom_id="m_gun",
                style=STYLE,
            ),
            interacts.Button(
                label='Exist to main menu'.title(),
                custom_id="quite",
                style=interacts.ButtonStyle.DANGER,
            ),
        ]
    )
]


async def pvp(ctx: interacts.CommandContext):
    """
    Args:
        ctx:
    """
    global rounds
    global select_and_del

    plyr1_name = m.plyr1.name
    if len(plyr1_name) > 7:
        plyr1_name = plyr1_name[:8] + ' . . .'

    plyr2_name = m.plyr2.name
    if len(plyr2_name) > 7:
        plyr2_name = plyr2_name[:8] + ' . . .'

    #  Round Counting.../
    original_msg = await ctx.send(f'╭─────── :dagger:  **Round {rounds}** :dagger:    ───────╮')

    #  Player input.../
    plyr_1 = m.plyr1.choice
    plyr_2 = m.plyr2.choice


    # Player vs CPU.../
    msg = (f'{original_msg.content}'
           f'\n |    **↓ {plyr1_name} ↓                        ↓ {plyr2_name} ↓**'
           f'\n |     {plyr_1}             *** __vs__***         {plyr_2}')
    vs_msg = await original_msg.edit(msg)

    #  Checking and Updating results.../
    check_msg = await original_msg.edit(f'{vs_msg.content}'
                                        f'\n |  ───── :gear: *Checking Result* :gear: ───── |'
                                        f'\n |'
                                        )

    winner = gm_f.pvp_chck_result(
        plyr1_choice=plyr_1,
        plyr2_choice=plyr_2
    )
    # await gm_f.bal_update(
    #     ctx=ctx,
    #     bal=gm_s.betting_amt,
    #     winner_val=winner[1],
    #     plyr_choice=plyr_1,
    #     cpu_choice=plyr_2
    # )

    #  Presenting Winner and Win/Loss balance.../
    winner_msg = await original_msg.edit(f'{check_msg.content}\n |  {winner[0]}')

    if winner[1] == plyr_1:
        await original_msg.edit(f'{winner_msg.content}'
                                f'\n |          :trophy:   ***Winner :***     {plyr1_name}  |'
                                f'\n |          :moneybag:   ***Loot :***     {gm_s.betting_amt[plyr_1]}rs'
                                f'\n |                    ────────── '
                                f'\n |          :o:   ***Loses :***     {plyr2_name}  |'
                                f'\n |          :x:   ***Lost :***     {gm_s.betting_amt[plyr_2]}rs'
                                )
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')

        # await gm_f.countdown_timer(ctx, 3, next_round)
        # await gm_f.update_stats(ctx, wins=1)  # Updating stats.../

    elif winner[1] == plyr_2:
        await original_msg.edit(f'{winner_msg.content}'
                                f'\n |          :trophy:   ***Winner :***     {plyr2_name}  |'
                                f'\n |          :moneybag:   ***Loot :***     {gm_s.betting_amt[plyr_2]}rs'
                                f'\n |                    ────────── '
                                f'\n |          :o:   ***Loses :***     {plyr1_name}  |'
                                f'\n |          :x:   ***Lost :***     {gm_s.betting_amt[plyr_1]}rs'
                                )
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')
        # await gm_f.countdown_timer(ctx, 3, next_round)

#         await gm_f.update_stats(ctx, loses=1)  # Updating stats.../

    elif winner[1] == 'draw':
        # next_round = await original_msg.edit(f"{winner_msg.content}\n |          :arrows_counterclockwise:   *Next
        # Round in **3** seconds* | \n╰───────────────────────╯")
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')
        # await gm_f.countdown_timer(ctx, 5, next_round)

#         await gm_f.update_stats(ctx, draws=1)  # Updating stats.../

    #  Next Round.../
    rounds += 1
    m.plyr1.choice = ''
    m.plyr2.choice = ''
    select_and_del = await ctx.send(components=choices)


#  .................... choice snake ..................../
@client.component('m_snake')
async def water(ctx: interacts.CommandContext):
    global select_and_del

    # Validating Player
    if m.plyr1.username == m.plyr2.username:
        await ctx.send(custom.P1_P2_SAME)
        return

    elif await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    # Both player making choice
    bs_f.players_choice(ctx, 1)

    if await bs_f.validate_choices(ctx):
        return

    await select_and_del.delete()
    await pvp(ctx)


#  .................... Choice water ..................../
@client.component('m_water')
async def water(ctx: interacts.CommandContext):
    global select_and_del

    # Validating Player
    if m.plyr1.username == m.plyr2.username:
        await ctx.send(custom.P1_P2_SAME)
        return

    elif await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    # Both player making choice
    bs_f.players_choice(ctx, 2)

    if await bs_f.validate_choices(ctx):
        return

    await select_and_del.delete()
    await pvp(ctx)


#  .................... Choice gun ..................../
@client.component("m_gun")
async def gun(ctx: interacts.CommandContext):
    global select_and_del

    # Validating Player
    if m.plyr1.username == m.plyr2.username:
        await ctx.send(custom.P1_P2_SAME)
        return

    elif await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    # Both player making choice
    bs_f.players_choice(ctx, 3)

    if await bs_f.validate_choices(ctx):
        return

    await select_and_del.delete()
    await pvp(ctx)


#  .................... Quite ..................../
@client.component('quite')
async def quite(ctx: interacts.CommandContext):
    global rounds
    global select_and_del

    if await bs_f.user_validation(ctx, interfere=True, new_player=True):
        return

    m.plyr1 = Player()
    m.plyr2 = Player()
    mm.select_and_del = await ctx.send('# Main Menu:-\n', components=mm.menu_options)
    await select_and_del.delete()
