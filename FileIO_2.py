#Getting Where To Save File
where = input('Where do you want to save your file? ')

#Getting What To Write To File
text = input('What do you want to write to your file? ')

#Actually Writing It
file_handle = open(where, 'w')
file_handle.write(text)
file_handle.write("\n")
file_handle.close()
