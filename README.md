# nUmBeRs

To run this, you must first run `pip install inflect`

Then whenever you want, you can just run `from generate import *` and it will create every number that is currently supported as its own variable.

Then, you can finally do polymorphic maths without worrying about what types you're using! For instance, you can run `one + one` and output `(2,)`

What's more is, is, you can even have uppercase numbers, like Four! All you have to do, is define it as such: `Four = WordNumber("Four")`.


# EXAMPLES

`one + one`:
> (2,)

`one + 1`
> (2,)

`one + "1"`
> 2

`one + "one"`
> 2

`one + "ONE"`
> 2

`one == 1`
> True

`one == 2`
> False

`three = WordNumber("three")`
`three`
> 3


`Three = WordNumber("Three")`
`Three`
> 3.5


`four + (five + six)`
> (15,)


# KNOWN ISSUES

`one + one == two` currently returns False. This is due to a type conversion error. You can get around this by doing: `(one + one)[0] == two.__value__()`

-- alternatively ensure that the value to the right of the `==` operator is an integer, as the __eq__ method currently requires this

`Four = WordNumber(four)` creates a WordNumber with no WordNumber.number attribute defined. This is the correct behaviour, and user should not write code that does this.

-- Instead, use `Four = WordNumber('Four')` when creating uppercase variables

`five + six + "2"` causes a TypeError. This is because the user has failed to use parentheses, as so: `five + (six + "2")`
