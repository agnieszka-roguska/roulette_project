from time import sleep
import functions
import making_bets
import spin_results

def game(init_bet : int, current_money : int):
    if init_bet == 0:
        print(f"Place your bets... \n")
    your_bet = init_bet if init_bet > 0 else making_bets.bet_money(current_money)
    print("You put ", your_bet, " money on this game. \n\n")
    answer = making_bets.inside_outside_question()
    spinned_number, spinned_colour = spin_results.spin()
    if answer == "INSIDE":
        guessed_numbers = making_bets.inside_bets_only_ints()
        win, next_bet = spin_results.check_results_inside_bets(your_bet, (spinned_number, spinned_colour), guessed_numbers)
    else:
        guessed_numbers = making_bets.outside_bets()
        win, next_bet = spin_results.check_results_outside_bets(your_bet, (spinned_number, spinned_colour), guessed_numbers)
    
    net_gain = win - your_bet if win > 0 else win
    return win, net_gain, next_bet

def main():
    current_money = 100
    number_of_games = 5
    current_bet = 0
    
    for game_counter in range(number_of_games):
            print(f"Game {game_counter+1}: You have {current_money} money.")
            win, net_gain, current_bet = game(current_bet, current_money)
            current_money += win

            if win > 0:
                print("You won! Resetting bet.\n\n")
                current_bet = 0
            else:
                print("You lost! Next bet will be doubled: ", current_bet, "\n\n")
                if current_bet > current_money:
                    current_money = 0
                    print("You don't have enough money to place a bet")
            if game_counter == 4:
                print("That was your 5th game, thank you for playing! ")
                sleep(10)
            if current_money <= 0:
                print("You ran out of money. GAME OVER! You lost :<<<<<<< ")
                sleep(10)
                break

if __name__ == "__main__":
    main()
