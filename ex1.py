age = input("Enter age: ")
age = int(age)

if age >= 21:
    print("Here's your beer.")
elif age <= 18:
    print("You need to leave immediately!")
else:
    print("Sorry!")