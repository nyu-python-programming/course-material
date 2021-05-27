word1 = 'hippopotamus'
word2 = 'immolate'

print(word1 + word2, end='. ')
print(word1, word2, end='\n')
print(word1, word2, sep='')
print(word1, word2, sep='-')

phrase = word1 + word2 # this will concatenate the two words together, with no automatic space between them
print(phrase)

phrase = word1, word2 # this will not give you a space between the words!!!... this gives you a tuple, which you probably did not want at all and don't know what it is.
print(phrase)

