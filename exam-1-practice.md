# Exam 1 practice

## Evaluate expressions

Evaluate the following expressions and note the data type of the result:

---

**_Expression_** **_Evaluates To_** **_Data Type_**
5 \* 2  
 5 \*\* 2  
 \'5\' + \'2\'  
 \'5\' \* 2  
 5 / 2  
 5 // 2  
 5 % 2  
 5 + 2.0  
 5.0 \* 2.0  
 10 \> 2  
 2 \< 1  
 2 != 4  
 4 == 2\*\*2  
 \'cat\' \< \'dog\'  
 \'Cat\' \< \'dog\'  
 5 \> 2 and 10 \> 11  
 5 \> 2 or 10 \> 11  
 5 \> 2 and not (10 \> 11)  
 str.lower(\'HeLLo\')  
 str.upper(\'HeLLo\')  
 format(5.1, \'.2f\')  
 format(5.1, \'\>10.2f\')  
 random.randint(1,5)  
 len(\'cat\')  
 len(\'cat\' + \'dog\')  
 not (5\>2 and 5 \< 4)

---

## Input/Output

What is the exact output of each of the following programs? - Try and
determine this by reading only, without running the programs.

### Program \#1

`a = 10`\
`b = 20`\
`c = 30`\
\
`if c > b + a:`\
` print ("N\nY\nU\n")`\
\
`else:`\
` if b + a >= c:`\
` print ("C\nO\nU\nR\nA\nN\nT\n")`\
` else:`\
` print ("S\nT\nE\nR\nN\n")`\
\
`print (a,b,c)`

### Program \#2

`x = 'cupid'`\
`z = 'arrow'`\
\
`if x < z:`\
` t = x`\
` x = z`\
` z = t`\
\
`v = x + " <--> " + z`\
\
`if ( ( (5 + 2 >= 6.0) and (1.0 < 0.5) ) or True):`\
` print (x,z,v, sep='\t')`\
`else:`\
` print (v,z,x, sep='\n')`

### Program \#3

`a = 5`\
`b = 6`\
`c = 20`\
`d = 24`\
\
`if a < b and b * 2 < c:`\
\
` print ("Python Case 1")`\
` print ("A", '\t', "B", '\t', "C")`\
` `\
` if a * 2 == c:`\
` print (a*2, '\t', a*2, '\t', a*2)`\
` elif a * 3 == c:`\
` print (a*3, '\t', a*3, '\t', a*3)`\
` elif a * 4 == c:`\
` print (a*4, '\t', a*4, '\t', a*4)`\
` else:`\
` print ('?', '\t', '?', '\t', '?')`\
` `\
`else:`\
\
` print ("Python Case 2")`\
` print ("a", '\t', "b", '\t', "c")`\
` `\
` if b * 2 == d:`\
` print (b*2, '\t', b*2, '\t', b*2)`\
` elif b * 3 == d:`\
` print (b*3, '\t', b*3, '\t', b*3)`\
` elif b * 4 == d:`\
` print (b*4, '\t', b*4, '\t', b*4)`\
` else:`\
` print ('?', '\t', '?', '\t', '?')`

### Program \#4

`def fun1():`\
` print ("hi!")`\
\
`def fun2():`\
` print ("bye!")`\
\
`if 10 < 5 or 5 > 6:`\
` fun1()`\
` fun2()`\
`else:`\
` fun2()`\
` fun1()`

## Write programs from scratch

Use your programming skills to solve the following programming
challenges:

1.  Write a program that asks the user to supply two words. Sort the
    words in alphabetical order and print them back to the user.
2.  Write a program that asks the user to supply two words. Sort the
    words in size order and print them back to the user.
3.  Write a program that has the computer virtually roll two 6 sided
    dice. Output the result as follows: \"Virtual dice roll: 3 and 5\"
4.  Write a program that asks the user to enter in number. Then have the
    computer generate a random number and compare the result. If the
    numbers are the same print out a \"You Win!\" message. If not, print
    out a \"Try Again\" message.
5.  Write a program that qualfies the user for a particular credit card.
    Users must meet the following criteria:
    - Make at least \$30,000 per year
    - Their rent payment must not be more than 5% of their total
      salary per month (i.e. 1,500 is the max rent that they can pay
      while making 30,000 per year)
    - However, if they own their home you do not need to take their
      monthly house payment into accountHere is a sample running of
      the program:

`Credit card qualifier`\
`How much do you make per year? 30000`\
`Do you own your home? (y/n) y`\
`You qualify!`\
\
\
\
`Credit card qualifier`\
`How much do you make per year? 35000`\
`Do you own your home? (y/n) n`\
`How much do you pay in rent per month? 1000`\
`You qualify!`\
\
\
\
`Credit card qualifier`\
`How much do you make per year? 50000`\
`Do you own your home? (y/n) n`\
`How much do you pay in rent per month? 5000`\
`Sorry, you don't qualify. Your rent is too high`

1.  Write a program to ask a user to enter in 3 test scores (0-100) and
    1 homework score (0-100). Then calculate the user\'s grade using the
    following formula - Tests: 50%, Homework: 50%. You can assume the
    user will enter integer values. Print out the grade as a number
    (i.e. 78.56%) along with its letter equivalent (i.e. \'C\'). For the
    purposes of this program you can assume that A = 90-100, B =
    80-89.99, C = 70-79.99, D = 65-69.99 and F is less than 65
2.  A company has determined that its annual profit is typically 23
    percent of total sales. Write a program that asks the user to enter
    in the projected amount of total sales and then displays the profit
    that will be made from that amount.
3.  One acre of land is equivalent to 43,560 square feet. Write a
    program that asks the user to enter the total square feet in a tract
    of land and calculate the number of acres in that tract.
4.  A customer in a store is purchasing 5 items. Write a program that
    asks for the price of each item, and then displays the subtotal of
    the sale, the amount of sales tax, and the total. Assume the sales
    tax is 6 percent.
5.  Write a program to input a 2 digit integer, call it x, where the
    rightmost digit is nonzero. Compute the integer y which has the same
    digits as x, but in reverse order. Print out x, y and x+y. For
    example:

`Please enter a two digit integer: 23 `\
`23 reversed is: 32 `\
`23 + 32 is 55`

1.  Analyze the code below and identify any problems or issues that
    might exist. Offer suggestions on how to re-engineer the code to
    prevent these errors from occurring and/or rewrite the code so that
    it functions correctly. rate = str(input(\"How much do you make per
    hour? \'))

`hours = input("How many hours did you work this week? ")`\
\
`if hours < 40:`\
` pay = rate * hours`\
`if hours > 40`\
` pay = rate * 40`\
` ot_pay = (hours-40) ** (rate*1.5)`\
\
`print ("Your total pay is, pay + ot_pay")`

1.  Write a program that lets the user figure out how many items they
    can purchase at a local coffee shop. Begin by asking the user to
    enter in amount of money as a float. Then ask the user to select a
    product from a pre-determined list. Figure out how many items the
    user can purchase, noting that the coffee shop does not sell
    fractional amounts (i.e. you can\'t buy half a donut)

`How much money do you have?: 10.00`\
\
`What would you like to buy?`\
`Donut (d) - $1.50`\
`Coffee (c) - $1.00`\
`Bagel (b) - $2.50`\
`Scone (s) - $2.75`\
\
`Enter your choice (d/c/b/s): d`\
\
`You can purchase 6 donuts with $ 10.0 Note that you cannot assume that the user will enter a valid product (i.e. they could type in the string "donut" instead of the string "d"). In this case you will need to present the user with some kind of error (i.e. "Sorry, that's not a valid product") ' you do not need to re-prompt them (you can just end the program). Also, you can assume that the user will input valid floating-point numbers when prompted.`

1.  Write a \"calculator\" program that asks the user for two numbers as
    well as an \"operation code\" (\"a\" for add, \"s\" for subtract,
    \"d\" for divide or \"m\" for multiply). Using the information
    provided perform the specified operation and print the result. Note
    that you cannot assume that the user will enter a valid operation
    code (i.e. they could type in the string \"multiply\" instead of the
    string \"m\"). In this case you will need to present the user with
    some kind of error (i.e. \"Sorry, that\'s not a valid operation
    code\") and exit the program. However, you can assume that the user
    will input valid floating-point numbers when prompted. Also note
    that dividing a number by 0 will result in a runtime error. Prevent
    this from happening in your program by providing special output in
    this case (i.e. 5.0 / 0.0 = undefined). Here is a sample running of
    the program:

`Number 1: 2.0`\
`Number 2: 3.0`\
`Operation (a/s/d/m): add`\
`Invalid operation! Try again.`\
`Operation (a/s/d/m): a`\
`2.0 + 3.0 = 5.0`

1.  A small college has asked you to write a program for their
    admissions department to help them determine if a student should be
    accepted into their school. Write a program that uses the following
    criteria to determine whether a given applicant should be admitted:
    - Combined SAT score of 1600 or more
    - A high school GPA of 3.0 or higher
    - At least 3 extracurricular activities. This particular school
      places a heavy emphasis on extracurricular activities, so
      students with 5 or more activities only need a 1400 combined
      score on their SAT and a GPA of 2.8. Comment your code as
      necessary. You can assume that the user will enter
      floating-point values. Here is a sample running of your program.

`Student name: Craig`\
`Combined SAT Score: 1800`\
`High school GPA: 3.2`\
`# of extracurricular activities: 3`\
`Craig should be admitted!`\
\
`Student name: John`\
`Combined SAT Score: 1500`\
`High school GPA: 3.1`\
`# of extracurricular activities: 7`\
`John should be admitted!`\
\
`Student name: Chris`\
`Combined SAT Score: 1300`\
`High school GPA: 2.9`\
`# of extracurricular activities: 8`\
`Chris should not be admitted.`

Functions practice:

1.  Create a function that can accept two arguments: name and age, and
    print out their value in the format, \"Bob: 22 years old\"
2.  Write a function calculation() such that it can accept two numeric
    values as arguments and calculate the sum and difference of those
    values. It returns either the sum or difference, depending on the
    value of a fourth argument which is assumed to be either the string
    \"sum\" or \"difference\".
3.  Write a Python function to check whether a given number is in a
    given range - where the number, and range are supplied as arguments
    to the function and the function returns True or False
4.  Write a Python function that takes a number as a parameter and check
    the number is prime or not.
