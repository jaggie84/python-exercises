count = 0

while count < 10:
  count += 1
  print("The Count is", count)
  
print("Done")  

while True:
  answer = input('Say when: ')
  if answer.lower() == 'when':
    break

print("Cheese")