import random

secret_number = random.randint(1, 10)
count = 4
print("I am thinking of a number between 1 and 10.")
print("You have 5 guesses left.")

while count >= 0:
   while True:
       try:
           guess = int(input("What's the number? "))
           break
       except ValueError:
           print("That's not a number, try again.")

   if guess == secret_number:
       print("Yes! You win!")
       play_again = (input("Do you want to play again (Y or N)? ")).upper()
       if play_again == "Y":
           secret_number = random.randint(1, 10)
           count = 4
       else:
           count = -1
           print("Bye!")

   elif count == 0:
       print("You ran out of guesses! The secret number was {}".format(secret_number))
       play_again = (input("Do you want to play again (Y or N)? ")).upper()
       if play_again == "Y":
           secret_number = random.randint(1, 10)
           count = 4
       else:
           count = -1
           print("Bye!")

   elif guess > secret_number:
       print("{} is too high.".format(guess))
       print("You have {} guesses left.".format(count))
       count -= 1
