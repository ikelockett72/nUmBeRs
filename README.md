# nUmBeRs

To run this, you must first run `pip install inflect`

Then whenever you want, you can just run `from generate import *` and it will create every number that is currently supported as its own variable.

Then, you can finally do polymorphic maths without worrying about what types you're using! For instance, you can run `one + one` and output `(2,)`

What's more is, is, you can even have uppercase numbers, like Four! All you have to do, is define it as such: `Four = WordNumber("Four")`.


# EXAMPLES

*Addition*

```
one + one
```
> (2,)

```
one + 1
```
> (2,)

```
one + "1"
```
> 2

```
one + "one"
```
> 2

```
one + "ONE"
```
> 2

*Equality conditions now work*

```
one == 1
```
> True

```
one == 2
```
> False

*Use @ to find the number within a string*
```
three@"where is the three?"
```
> 13

```
ten@"The concert was well attended"
```
> 23

*Capital numbers - allows for a greater range of integers*

```
Three = WordNumber("Three")
Three
```
> 3.5

*All caps numbers allow negatives*

```
TWO = WordNumber("TWO")
TWO
```
> -2

*All caps maths works too*

```
THREE = WordNumber("THREE")
FOUR = WordNumber("FOUR")
(THREE + FOUR)[0] + 3
```
> -4

```
ONE = WordNumber("ONE")
ONE == twelve@"Pizza Party"
```
> True

*Addition of more than 2 numbers possible with parentheses*

```
four + (five + six)
```
> (15,)

*Reassign numbers using <*

```
four < "5"
four
```
> 5

*Reassign numbers the other way around using >*
```
"2" > four
four
```
> 2

```
one > five
five
```
> 1

*Use > to compare WordNumbers to other numbers*

```
four > 5
```
> False

```
four > 3
```
> "Yes"

*Use @ to create shortcut numbers*

This is particularly helpful with larger, more verbose numbers

```
three@four@six@five + five@ten@eleven@four
```
> (513579,)

*Integer division works perfectly*

```
ten / 2
> 5
```

If the output is between numbers, it'll just pick one of the closest two numbers

```
ten / 3
> 3

ten / 3
> 4
```


# KNOWN ISSUES

```
one + one == two
```
> False

This is due to a type conversion error. You can get around this by doing: `(one + one)[0] == two.__value__()`

Alternatively ensure that the value to the right of the `==` operator is an integer, as the __eq__ method currently requires this

```
Four = WordNumber(four)
Four.number
```
> AttributeError: 'WordNumber' object has no attribute 'number'

This is the correct behaviour, and user should not write code that does this.

Instead, use `Four = WordNumber('Four')` when creating Capital numbers

```
five + six + "2"
```
> TypeError: can only concatenate tuple (not "str") to tuple

This is because the user has failed to use parentheses, as so: `five + (six + "2")`

```
ninety + 91 + ninetyone
```
>

Don't add a WordNumber to a tuple, it won't work.

```
eight == 82
```
> True

Note though that this equality condition only fails when two specific conditions are met:
- Both the WordNumber and the integer to which it is being compared are even / odd
- The first digit of the integer is the same as the first digit of the WordNumber

This is unlikely to occur frequently, so treating as low priority.

```
Four + four
> (8.5,)

four + Four
> (8,)
```
To be honest if this confuses you, you shouldn't be coding. Order of operations is essential here, and you need to be especially careful with Capital numbers.
