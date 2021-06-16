# open a file in append mode... this will create a new file by this name if none already exists
f = open('my_data.txt', 'a')

# append lines to the file... you must manually specify line breaks if you want them
f.write('welcome!\n')
f.write('unwelcome!\n')

# close the file... this is important!!!
f.close()
