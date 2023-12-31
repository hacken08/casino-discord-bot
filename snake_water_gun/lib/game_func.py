
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
        edit_msg = new_msg.content.replace(str(seconds_left), f'{str(i-1)}')

        await new_msg.edit(edit_msg)
        time.sleep(0.5)

    return new_msg


def chk_result(CHOICE, name, plyr_choice, cpu_choice):
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
    if plyr_choice == CHOICE['s'] and cpu_choice == CHOICE['w']:
        return {f"{snake_win}", plyr_choice}

    elif plyr_choice == CHOICE['w'] and cpu_choice == CHOICE['g']:
        return f"{water_win}", plyr_choice

    elif plyr_choice == CHOICE['g'] and cpu_choice == CHOICE['s']:
        return f"{gun_win}", plyr_choice

    elif plyr_choice == cpu_choice:
        return f"{draw}", 'draw'

    else:
        return f"{loss}", cpu_choice


async def updt_bal(ctx: interactions.CommandContext,bal, winner_val, plyr_choice, cpu_choice):
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


def want_to_play_again():
    """
    Asks the user to play again
    :return: True or False
    """
    while True:
        play_again = input('Would you like to play? (y/n): ')

        if play_again.lower() == 'y':
            return True
            break
        elif play_again.lower() == 'n':
            return False

        else:
            print('Invalid input. Try again.')



def reset():
    """
    Resets the
    """
    global plr_score
    plr_score = 0

    print('Score Reset Successfully')
    print('Current Score: ', plr_score)

    print('menu...')
    time.sleep(1.3)

def new_line(input_string):
    words = input_string.split()
    output_string = '\n |   '.join(' '.join(words[i:i + 5]) for i in range(0, len(words), 5))
    return output_string
