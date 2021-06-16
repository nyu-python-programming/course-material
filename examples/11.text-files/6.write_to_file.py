# open a file in write mode... this will create a new file by this name if none already exists
f = open('my_data.txt', 'w')

# write a line to the file... you must manually specify line breaks if you want them
f.write('hello!\n')
f.write('goodbye!\n')

# close the file... this is important!!!
f.close()
