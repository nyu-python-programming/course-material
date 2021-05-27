def main():
    """
    Some examples of modifying the default separator and ending settings of the print() function.
    """
    
    word1 = 'hippopotamus'
    word2 = 'immolate'

    print(word1 + word2, end='. ') # replace the default line break with a '. ' at the end of the printed text
    print(word1, word2, end='\n') # explicitly add a line break at the end of the printed text
    print(word1, word2, sep='') # replace the default separator used between the arguments to print with a blank string
    print(word1, word2, sep='-') # replace the default separator used between the arguments to print with a dash '-'

    phrase = word1 + word2 # this will concatenate the two words together, with no automatic space between them
    print(phrase)

    phrase = word1, word2 # this will not give you a space between the words!!!... this gives you a tuple, which you probably did not want at all and don't know what it is. Avoid!
    print(phrase)

# run the code called main
main()
