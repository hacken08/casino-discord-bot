import random
import time

import interactions as interact
import database as db

from snake_water_gun.lib import game_func as gm_f
from bot import client
import main as m

STYLE = interact.ButtonStyle.SUCCESS
BETTING_AMT = {
    ':snake: snake': 200,
    ':ocean: water': 500,
    ':gun: gun': 700
}
CHOICES = {
    's': ':snake: snake',
    'w': ':ocean: water',
    'g': ':gun: gun',
}

rounds = 1
wins = 0

choices = [
    interact.ActionRow(
            components=[
                interact.Button(
                        label='snake / 200rs'.title(),
                        custom_id="snake",
                        style=STYLE,
                ),
                interact.Button(
                        label='water / 500rs'.title(),
                        custom_id="water",
                        style=STYLE,
                ),
                interact.Button(
                        label='gun / 700rs'.title(),
                        custom_id="gun",
                        style=STYLE,
                ),
            ]
    )
]


#  ................. Playing  .................
async def playing(ctx: interact.CommandContext, key_cio: str):
    global balance
    global rounds

    plyr_name = ctx.author.name
    if len(plyr_name) > 7:
        plyr_name = plyr_name[:7]+' . . .'

    #  Round Counting.../
    original_msg = await ctx.send(f'╭─────── :dagger:  **Round {rounds}** :dagger:    ───────╮')

    #  Player input.../
    plyr_choice = CHOICES[key_cio]
    cpu_choice = random.choice(list(CHOICES.values()))

    # Player vs CPU.../
    msg = f'{original_msg.content}\n |    **↓ {plyr_name} ↓              ↓ CPU ↓**\n |   {plyr_choice}          *** __vs__***       {cpu_choice}'
    vs_msg = await original_msg.edit(msg)

    #  Checking and Updating results.../
    check_msg = await original_msg.edit(f'{vs_msg.content}\n |  ───── :gear: *Checking Result* :gear: ───── |\n |')
    time.sleep(2)

    winner = gm_f.chk_result(
            CHOICE=CHOICES,
            name=ctx.author.name,
            plyr_choice=plyr_choice,
            cpu_choice=cpu_choice
    )
    await gm_f.updt_bal(
            ctx=ctx,
            bal=BETTING_AMT,
            winner_val=winner[1],
            plyr_choice=plyr_choice,
            cpu_choice=cpu_choice
    )

    #  Presenting Winner and Win/Loss balance.../
    winner_msg = await original_msg.edit(f'{check_msg.content}\n |  {winner[0]}')

    if winner[1] == plyr_choice:
        winner_reward = await original_msg.edit(
            f'{winner_msg.content}\n |          :trophy:   ***Winner :***     {plyr_name}  |\n |          :moneybag:   ***Loot :***     {BETTING_AMT[plyr_choice]}rs')
        # next_round = await original_msg.edit(f"{winner_reward.content}\n |         :arrows_counterclockwise:   *Next Round in **3** seconds* | \n╰────────────────────────╯")
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')

        # await gm_f.countdown_timer(ctx, 3, next_round)
        time.sleep(3)


    elif winner[1] == cpu_choice:
        winner_reward = await original_msg.edit(
            f'{winner_msg.content}\n |          :trophy:   ***Winner :***     CPU|\n |          ❌   ***Lost :***     {BETTING_AMT[plyr_choice]}rs')
        #         next_round = await original_msg.edit(f"{winner_reward.content}\n |          :arrows_counterclockwise:   *Next Round in **3** seconds* | \n╰────────────────────────╯")
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')

        # await gm_f.countdown_timer(ctx, 3, next_round)
        time.sleep(3)


    elif winner[1] == 'draw':
        #         next_round = await original_msg.edit(f"{winner_msg.content}\n |          :arrows_counterclockwise:   *Next Round in **3** seconds* | \n╰───────────────────────╯")
        await original_msg.edit(f'{winner_msg.content} \n╰────────────────────────╯')

        # await gm_f.countdown_timer(ctx, 5, next_round)
        time.sleep(3)

    #  Next Round.../
    rounds += 1
    await ctx.send(components=choices)


#  .................... Choice snake ..................../
@client.component('snake')
async def water(ctx: interact):
    if not m.is_current_user(ctx):
        await ctx.send('❌**|** You can\'t **interfere, another player** in game.')
        return

    to_del = await ctx.channel.get_history()
    await  to_del[0].delete()

    await playing(ctx, 's')


#  .................... Choice water ..................../
@client.component('water')
async def water(ctx: interact):
    if not m.is_current_user(ctx):
        await ctx.send('❌**|** You can\'t **interfere, another player** in game.')
        return

    to_del = await ctx.channel.get_history()
    await  to_del[0].delete()

    await playing(ctx, 'w')


#  .................... Choice gun ..................../
@client.component('gun')
async def gun(ctx: interact):
    if not m.is_current_user(ctx):
        await ctx.send('❌**|** You can\'t **interfere, another player** in game.')
        return

    to_del = await ctx.channel.get_history()
    await  to_del[0].delete()

    await playing(ctx, 'w')
