word = input("Give me a word with double vowels: ")

word = word.replace('ee', 'eeee')
word = word.replace('oo', 'oooo')
word = word.replace('ii', 'iiii')
word = word.replace('aa', 'aaaa')
word = word.replace('uu', 'uuuu')

print(word)
