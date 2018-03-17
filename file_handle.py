file_handle = open('family_tree.txt', 'r')
while True:
  char = file_handle.read()
  if not char:
    break
  else:
    print(char)
file_handle.close()
