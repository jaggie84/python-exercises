which = input('Which file would you like to open? ')

file_handle = open(which, 'r')

counts = {}

for char in file_handle:
    for letter in char:
      if char not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1
print(counts)
file_handle.close()