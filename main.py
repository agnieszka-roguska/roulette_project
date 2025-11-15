from time import sleep
import functions
import making_bets
import spin_results

def game(init_bet : int, current_money : int):
    if init_bet == 0:
        print(f"Place your bets... \n You curently have {current_money} money. How much of it would you like to bet? \n")
        your_bet = making_bets.bet_money(current_money)
    else:
        your_bet = init_bet
    print("You put ", your_bet, " money on this game. Please place your bets. \n\n")
    answer = making_bets.inside_outside_question()
    if answer == "INSIDE":
        bets = making_bets.inside_bets()
        spinned_number, spinned_colour = spin_results.spin()
        print(functions.low_or_high_check(spinned_number), functions.which_dozen(spinned_number), functions.which_column(spinned_number))
        print(spinned_number, spinned_colour)
        win, current_bet = spin_results.check_results_inside_bets(your_bet, (spinned_number, spinned_colour), bets)
    else:
        bets = making_bets.outside_bets()
        spinned_number, spinned_colour = spin_results.spin()
        print(spinned_number, spinned_colour)
        print(functions.low_or_high_check(spinned_number), functions.which_dozen(spinned_number), functions.which_column(spinned_number))
        win, current_bet = spin_results.check_results_outside_bets(your_bet, (spinned_number, spinned_colour), bets)
        if current_bet == your_bet:
            current_bet = 0
    return win, current_bet

def main():
    current_money = 100
    number_of_games = 5
    init_bet = 0
    current_bet = 0
    for game_counter in range(number_of_games):
        if current_bet == init_bet:
            if game_counter != 0:
                print(f"congrats! you won the game! You have {game_counter} more tries. \n you have {current_money} money on your account")
            win, current_bet = game(init_bet, current_money)
        else:
            print(f"You lose. You next game will start with doubled bet.You have {game_counter} more tries. \n you have {current_money} money on your account")
            win, current_bet = game(2 * current_bet, current_money)
        sleep(0)
        current_money += win 


if __name__ == "__main__":
    main()
