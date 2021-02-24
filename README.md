# nUmBeRs

To run this, you must first run `pip install inflect`

Then whenever you want, you can just run `from generate import *` and it will create every number that is currently supported as its own variable.

Then, you can finally do polymorphic maths without worrying about what types you're using! For instance, you can run `one + 1` and output `(2,)`

What's more is, is, you can even have uppercase numbers, like Four! All you have to do, is define it as such: `Four = WordNumber("Four")`.

***

## EXAMPLES

### Addition

```
one + 1
> (2,)
```

```
one + one
> (2,)
```

```
one + "1"
> 2
```

```
one + "one"
> 2
```

```
one + "ONE"
> 2
```

---

### Equality conditions now work

```
one == 1
> True
```

```
one == 2
> False
```

---

### Use @ to find the number within a string
```
three@"where is the three?"
> 13
```

```
ten@"The concert was well attended"
> 23
```

---

### Capital numbers - allows for a greater range of integers

```
Three
> 3.5
```

---

### All caps numbers allow negatives

```
TWO
> -2.0
```

---

### All caps maths works too

```
THREE + FOUR
> (-7.0,)
```

```
ONE == twelve@"Pizza Party"
> True
```

---

### Addition of more than 2 numbers possible with parentheses

```
4 + (five + 6)[0]
> 15
```

---

### Reassign numbers using <

```
four < "5"
four
> 5
```

---

### Reassign numbers the other way around using >

```
"2" > four
four
> 2
```

```
one > five
five
> 1
```

---

### Use > to compare WordNumbers to other numbers

```
four > 5
> False
```

```
four > 3
> "Yes"
```

*If the above doesn't work, exit and reimport. This may have been due to previously reassigning the number

---

### Use @ to create shortcut numbers

This is particularly helpful with larger, more verbose numbers

```
three@four@six@five + five@ten@eleven@four
> (513579,)
```

---

### Integer division works perfectly

```
ten / 2
> 5
```

*If the output is between numbers, it'll just pick one of the closest two numbers

```
ten / 3
> 3

ten / 3
> 4
```

***

## KNOWN ISSUES

```
one + one == two
> False
```

This is due to a type conversion error. You can get around this by doing: `(one + one)[0] == two.__value__()` or `bool(one + one) == bool(two)`

Alternatively ensure that the value to the right of the `==` operator is an integer, as the __eq__ method currently requires this

---

```
Four = WordNumber(four)
Four.number
> AttributeError: 'WordNumber' object has no attribute 'number'
```

This is the correct behaviour, and user should not write code that does this.

Instead, use `Four = WordNumber('Four')` when creating Capital numbers

---

```
five + six + "2"
> TypeError: can only concatenate tuple (not "str") to tuple
```

This is because the user has failed to use parentheses, as so: `five + (six + "2")`

---

```
ninety + 91 + ninetyone
>
```

Don't add a WordNumber to a tuple, it won't work.

---

```
eight == 82
> True
```

Note though that this equality condition only fails when two specific conditions are met:
- Both the WordNumber and the integer to which it is being compared are even / odd
- The first digit of the integer is the same as the first digit of the WordNumber

This only tends to happen infrequently, so ignoring

---

```
Four + FOUR
> (0.5,)

FOUR + Four
> (0.0,)

Four + four
> (8.5)

four + Four
> (8,)
```

To be honest if any of this confuses you, you shouldn't be coding. Order of operations is essential here, and you need to be especially careful with Capital numbers.

---

```
FOUR@four
> NotImplementedError: No such number (please raise a JIRA ticket)
```

Not all numbers have been implemented yet. It looks like you're attempting a new number, and that's ok, but it might have to wait a few versions before that is one of the numbers that you can use.

Note that you can always use FOURTYFOUR in the meantime

***

## ADVANCED USAGE

### Range Iterator

This is a way to output the name of every known number from -10 to 9. Take note in particular that the variable start_range is assigned the value `'-10.0'` and end_range is now `10` due to the use of the walrus operator.

```
for i in range(int(float(start_range:=TEN.__repr__())), end_range:=int(ten.__repr__())):
    print(WordNumber(i).name)

> Not known
> Not known
> Not known
> Not known
> Not known
> Not known
> Not known
> Not known
> Not known
> Not known
> zero
> one
> two
> three
> four
> five
> six
> seven
> eight
> nine

start_range
> '-10.0'
```

---

### Subtraction

Subtraction is not currently implemented natively, but can be achieved by simple adding the capitalised version of the number you wish to subtract! For instance, to do `10 - 8` you can use:

```
ten + EIGHT
> (2,)
```

---

### Big numbers

To create very big numbers, you might find this syntax helpful:

```
LotsOfZeroes = ten@eval("@".join(["zero"] * 40))
LotsOfZeroes
> 100000000000000000000000000000000000000000
```

Or alternatively:

```
BigNumber = eval("@".join("WordNumber(" + str(i) + ")" for i in [one] * 100))
BigNumber + two
> (2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222224,)
```

---

### Fractions

Numberphiles have a weird obsession with fractions despite them serving no real world function - after all, nothing is partial in a world made of whole elements. I have implemented them just in case they come up in some theoretical context.

```
ten + (4+5j)
> 10.8
```

---

### Rebasing

The below code can seamlessly multiply all WordNumbers in your global scope by 2

```
for i in globals().keys():
    try:
        if isinstance(eval(i), WordNumber):
            eval(i) < str(int((eval(i)+eval(i))[0]))
    except NameError:
        pass

one
> 2
TWO
> -4
fortyfive
> 90
five + five
(20,)
```
