day = int(input('Day (0-6)? '))
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if day <= 5 and day >= 1:
  print("Go to Work.")

elif day == 0 or day == 6:
    print("Sleep in!")

else: 
    print("Not a valid Day")