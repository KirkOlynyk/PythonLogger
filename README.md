# PythonLogger
Log python scripts using decorators

This repository contains an example of how to trace Python code by
using two logging decorators, Logger.trace and Logger.log.
Logger.log simple prints a string at the current indent level. Logger.trace
prints the name of the function/method along with its arguments
and prints the return value upon exit. To trace a function/method
you must decorated it with then names of the arguments. In the case
of a class method, the first argument is always a reference to the
class.

## Example

```
  from logger import Logger
  
    class some_class:
        # decorate the constructor, one string for each argument!
        @Logger.trace('self','x')
        def __init__(self, x):
            self.x = x

        # decorarate a method
        @Logger.trace('self', 'y')
        def add(self, y):
            return self.x + y

    # decorate a function
    @Logger.trace('i')
    def g(i):
        return 3 * i

    @Logger.trace('i', 'j')
    def f(i, j):
        Logger.log("I am about to instantiate some_class {0} time".format(1))
        a_class = some_class(g(i))
        return a_class.add(g(j))

    print("The answer is", f(3,4))

```
