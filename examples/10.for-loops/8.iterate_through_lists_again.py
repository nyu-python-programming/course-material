shopping_list = ['asparagus', 'electrolyte', 'hippopotamus', 'platypus']

vowels = ['a', 'e', 'i', 'o', 'u']

print("\nFirst version\n")
for thing in shopping_list:
    if thing.startswith('a') or thing.startswith('e') or thing.startswith('i') or thing.startswith('o') or thing.startswith('u'):
        article = "an"
    else:
        article = "a"
    print("You need to buy {} {}.".format(article, thing))


print("\nSecond version\n")
for thing in shopping_list:
    if thing[0] in vowels:
        article = "an"
    else:
        article = "a"
    print("You need to buy {} {}.".format(article, thing))