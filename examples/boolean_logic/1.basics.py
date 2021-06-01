# define a function named 'main'
def main():
    #### - AND - ####
    print('\n -- AND -- ')

    # the 'and' operator evaluates an expression to true if both operands are true
    result = True and True
    print("True and True evaluates to {}".format(result))

    result = True and False
    print("True and False evaluates to {}".format(result))

    result = False and True
    print("False and True evaluates to {}".format(result))

    result = False and False
    print("False and False evaluates to {}".format(result))

    #### - OR - ####
    print('\n -- OR -- ')

    # the 'or' operator evaluates an expression to true if either operand is true
    result = True or True
    print("True or True evaluates to {}".format(result))

    result = True or False
    print("True or False evaluates to {}".format(result))

    result = False or True
    print("False or True evaluates to {}".format(result))

    result = False or False
    print("False or False evaluates to {}".format(result))

    #### - NOT - ####
    print('\n -- NOT -- ')

    result = not True
    print("not True evaluates to {}".format(result))

    result = not False
    print("not False evaluates to {}".format(result))

 
# call the function
main()
