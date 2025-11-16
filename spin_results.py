import random
import functions
from time import sleep

def spin() -> tuple[int, str]:
    random_number = random.randint(0, 36)
    if (random_number % 2 == 0) and (random_number != 0):
        colour = "BLACK"
    elif random_number == 0:
        colour = "GREEN"
    else: 
        colour = "RED"
    return random_number, colour

def spin_results_announce(spin_results):
    number = spin_results[0]
    colour = spin_results[1]
    high_low = functions.low_or_high_check(number)
    dozen = functions.which_dozen(number)
    column = functions.which_column(number)

    print("The wheel is spinning...")
    sleep(10)
    print(f"Results: \n \t number: \t {number} \n\t colour: \t{colour}\n\t high/low: \t{high_low} \n\t dozen: \t{dozen} \n\t column: \t{column}")
    
def check_results_inside_bets(bet_money : int, spin_result : tuple[int, str], guessed_numbers : list[int]) -> tuple[int, str]:
    spinned_number = spin_result[0]
    if spinned_number == 0:
        win = -bet_money
        next_money = 2 * bet_money
    elif spinned_number in guessed_numbers:
        next_money = 0
        match len(guessed_numbers):
            case 1:
                win = 35 * bet_money
            case 2:
                win = 17 * bet_money
            case 3:
                win = 3 * bet_money
            case _:
                print("error...")
    else: 
        win = -bet_money
        next_money = 2 * bet_money
    
    spin_results_announce(spin_result)
    return win, next_money

def check_results_outside_bets(bet_money : int, spin_result : tuple[str, str], outside_bet : tuple[str, str, int, int]) -> tuple[int, int]:
    spinned_number, spinned_colour = spin_result
    bet_colour, bet_high_low, bet_dozen, bet_column = outside_bet

    condition_1 = (bet_colour == spinned_colour)
    condition_2 = (bet_high_low == functions.low_or_high_check(spinned_number))
    condition_3 = (bet_dozen == functions.which_dozen(spinned_number))
    condition_4 = (bet_column == functions.which_column(spinned_number))

    if (spinned_number == 0):
        spin_results_announce(spin_result)
        return (-1) * bet_money, 2 * bet_money

    if (condition_1 or condition_2): #OK
        result = bet_money, bet_money
    elif (condition_3 or condition_4):
        result = bet_money, bet_money
    else:
        result = (-1) * bet_money, 2 * bet_money

    spin_results_announce(spin_result)
    return result