# While loops

Unlike [for loops](For_loops "wikilink"), which are used mostly to
repeat a block of code a finite number of times, while loops are most
often used to execute a block of code an indefinite number of times.
Each repetition is called an iteration.

## Iterating through a series of numbers

The following examples all repeat a print statement 6 times in order to
print the numbers from 5 to 10, inclusive. The algorithm is as follows:

- start off a counter at the desired starting value
- enter a loop and keep looping until the counter reaches the desired
  ending number
- within each iteration of the loop:
  - print out the current value of the counter
  - increment the counter by one

### Python example

```
i = 5
while i <= 10:
    print(i)
    i += 1;
```

### Java example

```
int i = 5;
while (i <= 10) {
    System.out.println(i);
    i++;
}
```

### Javascript example

```
var i = 5;
while (i <= 10) {
    console.log(i);
    i++;
}
```

### PHP example

```
$i = 0;
while ($i <= 10) {
    print($i);
    $i++;
}
```

## Iterating through a characters in a string

The following examples all repeat a print statement 9 times in order to
print the characters in the string, \'asparagus\'. The algorithm is as
follows:

- start a counter at the value zero
- keep looping until the counter reaches the number of characters in
  the string
- within each iteration of the loop:
  - get the character at the index position indicated by the counter
  - print that character out
  - increment the counter by one

### Python example

```
s = "asparagus"
i = 0
while i < len(s):
    c = s[i]
    print(c)
    i += 1
```

### Java example

```
String s = "asparagus";
int i = 0;
while (i < s.length()) {
    char c = s.charAt(i);
    System.out.println(c);
    i++;
}
```

### Javascript example

```
var s = "asparagus";
var i = 0;
while (i < s.length) {
    var c = s.charAt(i);
    console.log(c);
    i++;
}
```

### PHP example

```
$s = "asparagus";
$i = 0;
while ($i < strlen($s)) {
    $c = $s{$i};
    print($c);
    $i++;
}
```

## Iterating through a values in a list or array

The following examples all repeat a print statement 5 times in order to
output each of the following values: \'they\', \'sailed\', \'away\',
\'in\', \'a\', \'sieve\', \'they\', \'did\' - these words are from the
first line of [The Jumblies](The_Jumblies "wikilink"), by Edward Lear.
The algorithm is as follows:

- start a counter at the value zero
- enter a loop, and keep looping until the counter reaches the number
  of values in the list
- with each iteration of the loop:
  - get the value in the list at the index position represented by
    the counter
  - print that value out
  - increment the counter by one

### Python example

```
list_of_values = [ 'they', 'sailed', 'away', 'in', 'a', 'sieve', 'they', 'did' ]
i = 0
while i < len(list_of_values):
    val = list_of_values[i]
    print(val)
    i += 1
```

### Java example

```
String[] list_of_values = { "they", "sailed", "away", "in", "a", "sieve", "they", "did" };
int i = 0;
while (i < list_of_values.length) {
    String val = list_of_values[i];
    System.out.println(val);
    i++;
}
```

### Javascript example

```
var list_of_values = [ 'they', 'sailed', 'away', 'in', 'a', 'sieve', 'they', 'did' ];
var i = 0;
while (i < list_of_values.length) {
    var val = list_of_values[i];
    console.log(val);
    i++;
}
```

### PHP example

```
$list_of_values = array( 'they', 'sailed', 'away', 'in', 'a', 'sieve', 'they', 'did' );
$i = 0;
while ($i < sizeof($list_of_values)) {
    $val = $list_of_values[$i];
    print($val);
    $i++;
}
```

## Validating user input

The following examples use a while loop to ask the user the question,
\"What\'s the magic word\"? The program repeats asking this question
over-and-over until the user enters the valid response, \"please\". The
algorithm is as follows:

- define the correct response
- define the user\'s response as blank to begin with
- keep looping until the user\'s response and the correct response are
  the same
- with each iteration of the loop:
  - output to the user that they should enter a response
  - overwrite the previous user\'s response with the new response
    they enter

### Python example

```
correct_response = "please"
users_response = ""
while users_response != correct_response:
    users_response = input("What's the magic word? ")
```

### Java example

```
Scanner scn = new Scanner(System.in);
String correct_response = "please";
String users_response = "";
while (!users_response.equals(correct_response)) {
    System.out.println("What's the magic word? ");
    users_response = scn.nextLine();
}
```

### Javascript example

```
var correct_response = "please";
var users_response = "";
while (users_response != correct_response) {
    users_response = input("What's the magic word?");
}
```

### PHP example

```
$scn = fopen("php://stdin","r");
$correct_response = "please";
$users_response = "";
while ($users_response != $correct_response) {
    print("What's the magic word?");
    users_response = fgets($scn);
}
```

## Calculating a running total

The following examples ask the user to enter in numbers one at a time.
Each new number is added to a [running
total](wikipedia:Running_total "wikilink"), which is the sum of all
numbers entered so far. The program keeps asking for numbers until the
user types \'stop\'. The algorithm is as follows:

- start the total at zero
- define the user\'s response as blank
- keep looping until the user types the word, \'stop\'
- with each iteration of the loop:
  - output to the user that they should enter a new number or the
    word, \'stop\'
  - if the user entered a number
    - increment the total by the number the user entered
  - otherwise
    - stop iterating the loop

### Python example

```
total = 0
stop_response = "stop"
users_response = ""
while users_response != stop_response:
    users_response = input("Enter a number: ")
    try:
        val = int(users_response)
        total = total + val
    except:
        print("Sorry, that's not a valid number")
print("The total is " + str(total))
```

### Java example

```
Scanner scn = new Scanner(System.in);
int total = 0;
String stop_response = "stop";
String users_response = "";
while (!users_response.equals(stop_response)) {
    System.out.println("Enter a number: ");
    users_response = scn.nextLine();
    try {
        int val = Integer.parseInt(users_response);
        total = total + val;
    }
    catch (Exception e) {
        System.out.println("Sorry, that's not a valid number");
    }
}
System.out.println("The total is " + total);
```

### Javascript example

```
var total = 0;
var stop_response = "stop";
var users_response = "";
while (users_response != stop_response) {
    users_response = input("Enter a number: ");
    try {
        var val = parseInt(users_response);
        total = total + val;
    }
    catch (exception) {
        console.log("Sorry, that's not a valid number");
    }
}
System.out.println("The total is " + total);
```

### PHP example

```
$scn = fopen("php://stdin","r");
$total = 0;
$stop_response = "stop";
$users_response = "";
while ($users_response != $stop_response) {
    print("Enter a number: ");
    $users_response = fgets($scn);
    try {
        $val = (int) $users_response;
        $total = $total + $val;
    }
    catch (Exception $e) {
        print("Sorry, that's not a valid number");
    }
}
print("The total is " + $total);
```

## Accumulator pattern

Any loop where a variable is increasing in value with each iteration.

- very common in practice

## Infinite loop

A loop that never stops iterating.
