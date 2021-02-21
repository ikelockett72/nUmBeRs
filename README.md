# nUmBeRs

To run this, you must first run `pip install inflect`

Then whenever you want, you can just run `from generate import *` and it will create every number that is currently supported as its own variable.

Then, you can finally do polymorphic maths without worrying about what types you're using! For instance, you can run `one + one` and output `(2,)`

# KNOWN ISSUES

`one + one == two` currently returns False. This is due to a type conversion error. You can get around this by doing: `(one + one)[0] == two.__value__()`

-- alternatively ensure that the value to the right of the `==` operator is an integer, as the __eq__ method currently requires this

`Four = WordNumber(four)` creates a WordNumber with no WordNumber.number attribute defined. This is the correct behaviour, and user should not write code that does this.

-- Instead, use `Four = WordNumber('four')` when creating uppercase variables

`five + six + "2"` causes a TypeError. This is because the user has failed to use parentheses, as so: `five + (six + "2")`
