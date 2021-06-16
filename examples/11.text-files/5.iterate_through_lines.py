# open a plain text file... this returns a specialized data type that represents the file
f = open('data.txt', 'r')

num = 0

# iterate through all the lines of the file
for line in f:
    line = line.strip()
    num = num + line.lower().count("life")
    print(line)

print('The word {} occurs {} times in this poem.'.format('life', num))

