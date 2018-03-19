file_handle = open('test.py', 'r')
while True:
  char = file_handle.read()
  if not char:
    break
  else:
    print(char)
file_handle.close()
