from random import randint

def get_user_guess():
    """
    Function to prompt the user to input their guess for a number between 1 and 100.

    Returns:
        int: The user's guess as an integer.
    """
    guess = input('Guess the number between 1 and 100: ')
    return int(guess)

def generate_random_number():
    """
    Function to generate a random number between 1 and 100.

    Returns:
        int: A randomly generated number between 1 and 100.
    """
    return randint(1, 100)

def play_game():
    """
    Function to play the guessing game. It generates a random number between 1 and 100,
    prompts the user to guess the number, and provides feedback until the correct number is guessed.

    Returns:
        None
    """
    random_number = generate_random_number()
    number_of_attempts = 0
    
    while True:
        user_guess = get_user_guess()
        number_of_attempts += 1
        
        if user_guess < random_number:
            print('Your number is too low. Try again!')
        elif user_guess > random_number:
            print('Your number is too high. Try again!')
        else:
            print(f'Great! You guessed the number {random_number} in {number_of_attempts} attempts.')
            break

play_game()