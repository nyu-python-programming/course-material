# open a plain text file... this returns a specialized data type that represents the file
f = open('data.txt', 'r')

# read all the data from the file
poem = f.read()

# determine how many times Death occurs in the file
num = poem.lower().count("death")

print('The word, "{}", occurs {} times in the poem'.format('death', num) )
print(poem)

# close the file
f.close()
