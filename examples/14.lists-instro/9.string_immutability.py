my_string_1 = 'twas brillig and the slithy toves'
my_string_2 = my_string_1 # an alias

# my_string_1[3] = 'z' # crash!  strings are immutable!

my_string_1 = 'twaz brillig and the slithy toves' # fine!  that's variable reassignment.

print(my_string_2)

