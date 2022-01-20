# Imports the random module
import random


# This function contains the gameboard
def game_board():
    num_of_guesses = 0
    max_guesses = 20
    ships = [random.randint(0, 49) for i in range(5)]
    correct = 0
    place = 0

    # Here is the start of the printed gameboard
    print('Choose a target between 0 and 49.\n''Hit 3 Battleships to win.\n')
    print("       Let's play Battleships       ")
    print('     0  1  2  3  4  5  6  7  8  9      ')
    for row in range(5):
        location = ' '
        for character in range(10):
            character = ' - '
            location = location + character
        print(row, location)

    # Targets already guessed will be appended to this list
    used_guesses = []

    # While loop that contains the gameboard after each guess
    while num_of_guesses < max_guesses:
        # Try statement
        try:
            # Users input
            guess = int(input('Choose your target:\n'))
            num_of_guesses += 1
            # Handles already correct guesses
            if guess in used_guesses and guess in ships:
                correct -= 1
            # Handles already made guesses
            if guess in used_guesses:
                print('           ALREADY GUESSED!          ')
                num_of_guesses -= 1
                used_guesses.remove(guess)
            # Appends guesses already made to the used_guesses list
            used_guesses.append(guess)

            place = 0
            # Updated gameboard
            print('             Battleships           ')
            print('    0  1  2  3  4  5  6  7  8  9      ')
            for row in range(5):
                location = ' '
                for character in range(10):
                    character = ' - '
                    if guess == place and guess in ships:
                        character = ' X '
                        correct += 1
                    if guess == place and guess not in ships:
                        character = ' O '
                    if place in used_guesses and place in ships:
                        character = ' X '
                    if place in used_guesses and place not in ships:
                        character = ' O '
                    place += 1
                    location = location + character
                print(row, location)

            # Hit message
            if guess in ships:
                print('              hit!        ')

            # Miss message
            else:
                print('              Miss!        ')

            # Game info
            print('No. of guesses used: ', num_of_guesses)
            print('hits: ', correct)
            print('Max. Number of guesses', max_guesses)

            # Out of bounds message
            if guess < 0 or guess > 49:
                print('Thats out of bounds, try again.')
                used_guesses.remove(guess)
                num_of_guesses -= 1

            # Losing message
            if num_of_guesses == max_guesses:
                print('You lose, max number of guesses used.')
                break

            # Winning message
            if correct == 3:
                print('You Win!')
                break

        # Exception message
        except ValueError:
            print('Invalid input, try again')


game_board()
