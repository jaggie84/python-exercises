which = input('Which file would you like to open? ')

file_handle = open(which, 'r')

counts = {}

for char in file_handle:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1
print(counts)
file_handle.close()