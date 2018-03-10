file_handle = open('hello.txt', 'r')
while True:
  char = file_handle.read(1)
  if not char:
    break
  else:
    print(char)
file_handle.close()
