import random

too_low = 'too low'
too_high = 'too high'
correct = 'you guessed correctly!'
num_guess = 'Guesses used: '

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    guesses = 0
    while True:
        guess = get_guess()
        guesses += 1
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            print(num_guess + str(guesses))
            break


if __name__ == '__main__':
    main()
