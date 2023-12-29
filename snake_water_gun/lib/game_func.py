import random
import time

SCORES = {'Snake': 3, 'Water': 5, 'Gun': 7}
CHOICE = {
    's': 'Snake',
    'w': 'Water',
    'g': 'Gun'
}
plr_score = 0


def print_countdown(seconds):
    """
    Print countdown before the round starts.
    :param seconds:
    """
    for i in range(seconds, -1, -1):
        animation(f"| Game starting in {i} seconds<>", 1, 1)


def get_user_choice(name):
    """
    Get the user's choice for the game.
    :pram name
    :return plyr and cpu choices
    """
    while True:
        try:
            user_choice = CHOICE[input(f"\r| {name} is choosing: ").lower()]
            cpu_choice = random.choice(list(CHOICE.values()))
            return user_choice, cpu_choice

        except (KeyError, ValueError):
            for _ in range(3, -1, -1):
                animation(f'| Invalid choice! try again in {_} seconds<>', 1, 1)

            print('\n')



def chk_result(name, plyr_choice, cpu_choice):
    """
    Check plyr choice and cpu choice
    :param name:
    :param plyr_choice:
    :param cpu_choice:
    :return: winner choice
    """
    if plyr_choice == 'Snake' and cpu_choice == 'Water':
        return f"\n| {name} winn this with {plyr_choice} (^▽^) !! ", plyr_choice

    elif plyr_choice == 'Water' and cpu_choice == 'Gun':
        return f"\n| {name} winn this with {plyr_choice} (^▽^) !! ", plyr_choice

    elif plyr_choice == 'Gun' and cpu_choice == 'Snake':
        return f"\n| {name} winn this with {plyr_choice} (^▽^) !! ", plyr_choice

    elif plyr_choice == cpu_choice:
        return f"\n| {name} Draw this with {plyr_choice} (>_<) !!", 'draw'

    else:
        return f"\n| {name} lose this with {plyr_choice} (x_x) !! ", cpu_choice


def update_scr(winner_val, user_choice, cpu_choice):
    """
    Updates the score of player according to win and lose
    :param winner_val:
    :param user_choice:
    :param cpu_choice:
    :return: updated score
    """
    global plr_score
    if winner_val == user_choice and winner_val != cpu_choice:
        plr_score += SCORES[user_choice]

    elif winner_val == cpu_choice and winner_val != user_choice:
        plr_score -= SCORES[user_choice]

    elif winner_val == 'draw':
        plr_score = plr_score

    return plr_score


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


def animation(msg, dur, cnt=random.randrange(1, 4)):
    """
     Animate waiting messages
    :param msg:
    :param dur:
    :param cnt:
    """
    animation = ['.', '..', '...']

    for i in range(cnt):
        for _ in range(0, 3):
            print(f'\r{msg.replace("<>", animation[_])}', end='', flush=True)
            time.sleep(0.3)
        time.sleep(dur-0.9)

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

