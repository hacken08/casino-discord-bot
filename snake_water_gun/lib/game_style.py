import interactions as interact


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


def change_button(display):
    display = display.split(' ')

    from snake_water_gun.lib import single_player as splr
    splr.choices = [
        interact.ActionRow(
            components=[
                interact.Button(
                    label=f'{display[0]} / 200rs'.title(),
                    custom_id="snake",
                    style=splr.STYLE,
                ),
                interact.Button(
                    label=f'{display[1]} / 500rs'.title(),
                    custom_id="water",
                    style=splr.STYLE,
                ),
                interact.Button(
                    label=f'{display[2]} / 700rs'.title(),
                    custom_id="gun",
                    style=splr.STYLE,
                ),
                interact.Button(
                    label='Exist to main menu'.title(),
                    custom_id="quite",
                    style=interact.ButtonStyle.DANGER,
                ),
            ]
        )
    ]

    from snake_water_gun.lib import multi_player as mplr
    mplr.choices = [
        interact.ActionRow(
            components=[
                interact.Button(
                    label=f'{display[0]} / 200rs'.title(),
                    custom_id="snake",
                    style=mplr.STYLE,
                ),
                interact.Button(
                    label=f'{display[1]} / 500rs'.title(),
                    custom_id="water",
                    style=mplr.STYLE,
                ),
                interact.Button(
                    label=f'{display[2]} / 700rs'.title(),
                    custom_id="gun",
                    style=mplr.STYLE,
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

    change_button(display)
    return choices_style
