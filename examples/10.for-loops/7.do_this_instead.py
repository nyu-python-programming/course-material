word = "asparagus"

# # iterate through every character of a string the old-fashioned way
for i in range( len(word) ):
    print(word[i])

# # iterate through every character of a string the fancy way
for c in word:
    print(c)

# iterate through every character of a string the old-fashioned way
for i in range( len(word) - 1, -1, -1):
    print(word[i])

# iterate through every character of a string the old-fashioned way using negative indices
for i in range(-1, -10, -1):
    print(word[i])

# iterate through every character of a string the fancy way
for c in word[::-1]:
    print(c)
