from collections import namedtuple

Constants = namedtuple("Constants", ["COLOUR_VALUES", "HIGH_LOW_VALUES", "DOZEN_VALUES", "COLUMN_VALUES"])
constants = Constants(COLOUR_VALUES = ["BLACK", "RED"], 
                      HIGH_LOW_VALUES = ["HIGH", "LOW"], 
                      DOZEN_VALUES = ["1", "2", "3"], 
                      COLUMN_VALUES = ["1", "2", "3"]
                      )

def inside_outside_question():
    x = 1
    allowed_answers = ["OUTSIDE", "INSIDE"]
    while x:
        answer = input("Would you like to choose inside bets (numbers) or outside bets? \t ").upper()
        if answer in allowed_answers:
            return answer
        print("Invalid answer. Try again... ")

def bet_money(current_money : int) -> int:
    bet_checker = 1
    while bet_checker:
        bet = input("How much money would you like to bet? ")
        try:
            bet = int(bet)
            if bet > current_money:
                print("Your bet is bigger than the amount of money in your account")
            elif bet < 1:
                print("Your bet can't be 0 nor negative")
            elif (bet) == 0:
                print("You have to bet something, try again. ")
            else:
                return bet
        except:
            print("Incorrect input, please try again. ")

"""def inside_bets() -> list[int]:
    x = 1
    while x:
        chosen_numbers = input("Enter the guessed numbers. You shall enter up to 3 numbers - only positive ones, separated by comma ")
        chosen_numbers = chosen_numbers.replace(" ", "").replace(",", " ").split(" ")
        #chosen_numbers = chosen_numbers[:3]
        try: 
            chosen_numbers_ints = list(map(lambda x : abs(int(x)), chosen_numbers))
        except: 
            print("You've entered incorrect values, try again... ")
            continue
        
        if 0 in chosen_numbers_ints:
            print("You can't bet on 0. Try again... ")
        else: 
            x = 0
    values =  ["BLACK" if number % 2 == 0 else "RED" for number in chosen_numbers_ints]
    chosen_numbers = [str(x) for x in chosen_numbers_ints]
    result = list(zip(chosen_numbers, values))
    return result"""

def inside_bets_only_ints() -> list[int]:
    x = 1
    while x:
        chosen_numbers = input("Enter the guessed numbers. You shall enter up to 3 numbers (only 3 first will be taken into account) - only positive ones, separated by comma ")
        chosen_numbers = chosen_numbers.replace(" ", "").replace(",", " ").split(" ")
        chosen_numbers = chosen_numbers[:3]
        try: 
            chosen_numbers_ints = list(map(lambda x : abs(int(x)), chosen_numbers))
        except: 
            print("You've entered incorrect values, try again... ")
            continue
        
        if 0 in chosen_numbers_ints:
            print("You can't bet on 0. Try again... ")
        else: 
            x = 0
    chosen_numbers = [str(x) for x in chosen_numbers_ints]
    return chosen_numbers

def outside_bets() -> tuple[str, str, int, int]:
    questions = ["which colour?\t", "low (between 1 and 18) or high (between 19 and 36) number?\t", "which dozen? (1: numbers between 1-12, 2: number between 13-24, 3: number between 25-36)?\t", "which column?\t"]
    x = 1
    question_number = 0
    results = []
    for allowed_values in constants:
        x = 1
        while x:
            print("\n\nValues allowed for this bet: ", allowed_values)
            guess = input(questions[question_number]).upper()
            if guess in allowed_values:
                results.append(guess)
                x = 0
                question_number += 1
            else: 
                print("Incorrect value, please try again... ")

    bet_colour, bet_high_low, bet_dozen, bet_column = results

    return bet_colour, bet_high_low, int(bet_dozen), int(bet_column)