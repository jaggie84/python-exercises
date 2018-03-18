f = input("Hello, Please enter the file name you'd like to open: ")
file_handle = open(f, 'r') 
while True:
  char = file_handle.read()
  if not char:
    break
  else:
    print(char)
file_handle.close()
