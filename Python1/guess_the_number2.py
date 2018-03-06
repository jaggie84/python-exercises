secret_number = 5
print('I am thinking of a number between 1 and 10.')
while True:
    guess = int(input("What's the number? "))
    if guess == secret_number:
        print('Yes! You win!')
        break
    elif guess > secret_number:
        print('Too high. Try again.')
    elif guess < secret_number:
        print('Too low. Try again.')
    else:
        print('Nope, try again.')