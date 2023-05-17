import random

# saved variable for later
continue_game = True

# stored value for bets. outside loop so it is constant
pocket = 100

# greeting
print("Welcome to Dice Over/Under!")

# as long as this is true game will keep looping back to the start.
while continue_game == True:

    # see how many dice we want to play with, checks for any non int and loops back if input is invalid.
    try:
        dice_thrown = int(input("How many dice do you wish to play with?\n"))
    except ValueError:
        print("Invalid input. Numbers only\n")
        continue

    # stored values for throws
    first_throw_total = 0
    second_throw_total = 0

    # generate die rolls. random number 1-6. repeats per die, adds total as it goes, also prints die to screen
    for _ in range(dice_thrown):
        random_die = random.randint(1, 6)
        print(f"[{random_die}]")
        first_throw_total += random_die
    print(f"First throw total is {first_throw_total}.")

    # get the users guess for if the second roll will be higher or lower. checks for errors and loops back to ask again if needed
    while True:
        try:
            print("\nDo you think the second roll will be higher or lower?")
            user_guess = input("h for higher, l for lower: ")
            if user_guess not in ("h", "l"):
                raise ValueError
            break
        except ValueError:
            print("ERROR! Invalid input. Please enter 'h' for higher or 'l' for lower.")

    # get user bet, show current total by displaying pocket, remove bet from pocket. Check that user didn't overbet
    # if user over bets ask them to try again.
    while True:
        try:
            print(f"\nWanna make a bet? You currently have {pocket}.")
            user_bet = int(input("Place your bet: "))
            if user_bet > pocket:
                print("You don't have enough to cover that bet...")
                print("Lets try again.")
            else:
                pocket -= user_bet
                break
        except ValueError:
            print("Invalid input. Numbers only\n")

    # generate die rolls. random number 1-6. repeats per die, adds total as it goes
    for _ in range(dice_thrown):
        random_die = random.randint(1, 6)
        print(f"[{random_die}]")
        second_throw_total += random_die
    print(f"Second throw total is {second_throw_total}.\n")

    # placeholder for the result of the game
    result = "pass"

    # we compare, if both rolls are equal it ends in a tie, and we give user their bet back
    if first_throw_total == second_throw_total:
        result = "tie"
        pocket += user_bet

    # compare rolls for which one is higher, then check user guess, if user guesses correctly they win, if not they lose.
    elif first_throw_total < second_throw_total:
        if user_guess == "h":
            result = "win"
        else:
            result = "lose"

    # same as last comparison
    elif first_throw_total > second_throw_total:
        if user_guess == "l":
            result = "win"
        else:
            result = "lose"

        # print results, print updated betting pocket
    print(f"You {result}!")

    # update betting, if win double the user bet, add back to pocket, if user loses just skip through,
    # since we already removed the bet from pocket we don't have to do anything extra for a loss
    if result == "win":
        user_bet *= 2
        pocket += user_bet
    else:
        pass

    # check if user went bacnkrupt, if so end program
    if pocket == 0:
        print("BANKRUPT!")
        break
    else:
        print(f"Your updated total is {pocket}.")

    # check if we want to play again
    play_again = input("Play again (y/n): ")
    print("\n")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        continue_game = False