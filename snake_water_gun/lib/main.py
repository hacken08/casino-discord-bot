import time
from snake_water_gun.lib import game_func as func

SCORES = {
    'snake': 3,
    'water': 5,
    'gun': 7
}
CHOICE = {
    's': 'Snake',
    'w': 'Water',
    'g': 'Gun'
}

name = ''
rnd = 1
start_countdown = 3
next_rnd_intervals = 2
func.plr_score = 0

def play_game():
    global rnd
    while True:
        print(f'╭ Round {rnd}')
        func.print_countdown(start_countdown)

        try:
            choices = func.get_user_choice(name)
            user_choice = choices[0]
            cpu_choice = choices[1]
            print(f"| {name} -> {user_choice}   vs   {cpu_choice} <- CPU")

        except Exception as e:
            print('Something went wrong, try again')
            main_menu()
            return
        # \.................. checking results ................../
        print('|')
        func.animation("| Checking results<> ", 1)
        winner = func.chk_result(name, user_choice, cpu_choice)
        print(winner[0])

        #  \___________________Updating current score___________________/
        score = func.update_scr(winner[1], user_choice, cpu_choice)
        print(f'╰ Total Score: {score}')
        rnd += 1

        #  \..............Asking to play again ............../
        time.sleep(next_rnd_intervals)
        play_again = func.want_to_play_again()

        if not play_again:
            main_menu()
            break
        else:
            print()

def how_to_play():
    with open('../menu/txt.py', 'r') as f:
        print(f.read())

    while True:
        if input('Go to main menu? (y): ').lower() == 'y':
            main_menu()
            break
        else:
            print('Error: Invalid Option')


def exit_game():
    func.animation('Quieting Game<>', 1)
    print('\n')
    exit()


def settings():
    global next_rnd_intervals
    global start_countdown

    print(' 1) Want to stop for few second before going to next round? <sec>')
    print(' 2) seconds do you want to wait before rounds starts? <sec>'.casefold())
    print(' 0) Main Menu')

    try:
        select = input('Select option <option number> <corresponding val>: ').split()
    except ValueError:
        print('Error: input expected to be an integer')
        settings()

    match select[0]:
        case '1':
            try:
                if int(select[1]) >= 0:
                    next_rnd_intervals = int(select[1])
                    print('Done')
                else:
                    print('value can\'t less then 0, Try again')
            except (IndexError, ValueError):
                print('Error: seconds not mentioned')
        case '2':
            try:
                if int(select[1]) >= 0:
                    start_countdown = int(select[1])
                    print('Done')
                else:
                    print('value can\'t less then 0, Try again')
            except (IndexError, ValueError):
                print('Error: seconds not mentioned')
        case '0':
            main_menu()
        case _:
            print('Error: invalid option, choose from settings menu')

    settings()

def main_menu():
    print('\nMenu Options:-')
    print(' 1) Play game')
    print(' 2) How to play')
    print(' 3) settings'.capitalize())
    print(' 4) reset score'.capitalize())
    print(' 0) Exit')

    try:
        select = int(input('Select option: '))
    except ValueError:
        print('Error: input expected to be an integer')
        main_menu()

    match select:
        case 1:
            print('............... Game started ..............\n'.title().center(30))
            play_game()
        case 2:
            how_to_play()
        case 0:
            exit_game()
        case 3:
            print('\nSettings Menu:-')
            settings()
        case 4:
            func.reset()
            main_menu()
        case _:
            print('Error: Choose valid option from above menu')
            main_menu()


if __name__ == '__main__':
    print('\n' + ' Welcome to the snake Water game '.title().center(50, '-'))
    name = input('Enter your name before start: ')

    main_menu()
