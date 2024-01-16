import random
import time
import interactions

import database as db
from snake_water_gun.lib import status_messages as win

plr_score = 0


async def countdown_timer(ctx, seconds_left, new_msg: interactions.api.models.message.Message):
    """
    Countdown timer
    Args:
        ctx:
        new_msg:
        seconds_left:

    Returns:

    """
    for i in range(seconds_left, 0, -1):
        edit_msg = new_msg.content.replace(str(seconds_left), f'{str(i - 1)}')

        await new_msg.edit(edit_msg)
        time.sleep(0.5)

    return new_msg


def cpu_choice(plyr_chio, choices: dict):
    if plyr_chio == choices[1]:
        chio = [choices[2], choices[2], choices[3], choices[1]]
        return random.choice(chio)

    elif plyr_chio == choices[2]:
        chio = [choices[3], choices[3], choices[1], choices[2]]
        return random.choice(chio)

    elif plyr_chio == choices[3]:
        chio = [choices[1], choices[1], choices[2], choices[3]]
        return random.choice(chio)


def chk_result(CHOICE, plyr_choice, cpu_choice):
    """
    Check plyr choice and cpu choice
    :param CHOICE
    :param name:
    :param plyr_choice:
    :param cpu_choice:
    :return: winner choice
    """
    #  some random status message for user......../
    snake_win = random.choice(win.snake_win_msgs)
    snake_win = new_line(snake_win)

    water_win = random.choice(win.water_win_msgs)
    water_win = new_line(water_win)

    gun_win = random.choice(win.gun_win_msgs)
    gun_win = new_line(gun_win)

    draw = random.choice(win.draw_msgs)
    draw = new_line(draw)

    loss = random.choice(win.loss_msgs)
    loss = new_line(loss)

    # Checking if user is losing or winning..../
    if plyr_choice == CHOICE[1] and cpu_choice == CHOICE[2]:
        return f"{snake_win}", plyr_choice

    elif plyr_choice == CHOICE[2] and cpu_choice == CHOICE[3]:
        return f"{water_win}", plyr_choice

    elif plyr_choice == CHOICE[3] and cpu_choice == CHOICE[1]:
        return f"{gun_win}", plyr_choice

    elif plyr_choice == cpu_choice:
        return f"{draw}", 'draw'

    else:
        return f"{loss}", cpu_choice


async def bal_update(ctx: interactions.CommandContext, bal, winner_val, plyr_choice, cpu_choice):
    """
    Updates the score of player according to win and lose
    :param bal:
    :param ctx:
    :param winner_val:
    :param plyr_choice:
    :param cpu_choice:
    :return: updated score
    """
    user = ctx.user.username
    print(bal)
    print(plyr_choice)

    #  User data
    data = db.get_plyr_data(user)
    balance = data['balance']['value']

    if winner_val == plyr_choice and winner_val != cpu_choice:
        balance += bal[plyr_choice]

    elif winner_val == cpu_choice and winner_val != plyr_choice:
        balance -= bal[plyr_choice]

    elif winner_val == 'draw':
        return

    db.update_plyr_data(user, 'balance.value', balance)


async def update_stats(ctx: interactions.CommandContext, wins=0, loses=0, draws=0):
    """
    Args:
        ctx:
        wins:
        loses:
        draws:

    Returns:
    """
    data = db.get_plyr_data(ctx.user.username)

    total_wins = data['games']['snake_water_gun']['wins']
    total_loses = data['games']['snake_water_gun']['loses']
    total_draws = data['games']['snake_water_gun']['draws']

    total_wins += wins  # Remove the comma here
    total_loses += loses  # Remove the comma here
    total_draws += draws  # Remove the comma here

    val = {
        'games.snake_water_gun.wins': total_wins,
        'games.snake_water_gun.loses': total_loses,
        'games.snake_water_gun.draws': total_draws,
    }

    for key, value in val.items():
        db.update_plyr_data(ctx.user.username, key, value)


def new_line(input_string):
    words = input_string.split()

    if len(words[5]) > 22:
        output_string = '\n |   '.join(' '.join(words[i:i + 5]) for i in range(0, len(words), 5))
        return output_string

    output_string = '\n |   '.join(' '.join(words[i:i + 6]) for i in range(0, len(words), 6))
    return output_string
