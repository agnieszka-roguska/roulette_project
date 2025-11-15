import random
import functions

def spin() -> tuple:
    random_number = random.randint(0, 36)
    if (random_number % 2 == 0) and (random_number != 0):
        colour = "BLACK"
    elif random_number == 0:
        colour = "GREEN"
    else: 
        colour = "RED"
    return random_number, colour


def check_results_inside_bets(bet_money : int, spin_result : tuple, guessed_numbers : list) -> int:
    if spin_result[0] == 0:
        win = 0
        bet_money = 2 * bet_money

    elif spin_result[0] in guessed_numbers:
        match len(guessed_numbers):
            case 1:
                win = 35 * bet_money
            case 2:
                win = 17 * bet_money
            case 3:
                win = 3 * bet_money

    else: 
        win = (-1) * bet_money
        bet_money = 2 * bet_money
    
    return win, bet_money
    
def check_results_outside_bets(bet_money : int, spin_result : tuple[int, str], outside_bet : tuple[str, str, str, int, int]) -> tuple[int, int]:
    spinned_number, spinned_colour = spin_result
    bet_colour, bet_high_low, bet_dozen, bet_column = outside_bet

    condition_1 = (bet_colour == spinned_colour)
    condition_2 = (bet_high_low == functions.low_or_high_check(spinned_number))
    condition_3 = (bet_dozen == functions.which_dozen(spinned_number))
    condition_4 = (bet_column == functions.which_column(spinned_number))

    if (condition_1 or condition_2):
        return bet_money, bet_money
    elif (condition_3 or condition_4):
        return 2 * bet_money, bet_money
    else:
        return (-1) * bet_money, 2 * bet_money