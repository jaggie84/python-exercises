#Getting Where To Save File
where = input('What file would you like to edit? ')

#Getting What To Write To File
text = input('What information would you like to add? ')

#Actually Writing It
file_handle = open(where, 'a')
file_handle.write(text)
file_handle.write("\n")
file_handle.close()