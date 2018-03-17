import random

guess_tried = 0
secret_number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')
while True:
    guess_left = 5 - guess_tried
    print('You have {} guess left.'.format(guess_left))
    if guess_tried == 5:
        print('You ran out of guesses!')
        break

    # Optional error handling with try and except
    while True:
        try:
            guess = int(input("What's the number? "))
            break
        except ValueError:
            print("That's not a number.")

    guess_tried = guess_tried + 1
    if guess == secret_number:
        print('Yes! You win!')
        break
    elif guess > secret_number:
        print('Too high. Try again.')

    elif guess < secret_number:
        print('Too low. Try again.')

    else:
        print('Nope, try again.')
        