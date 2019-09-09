class Logger:
    level = 0
    indent = '|   '
    @staticmethod
    def trace(*argnames):
        '''
        This is a static Logger method indented to decorate functions and
        class methods. The arguments to trace are comma separated strings
        representing the arguments to the function/method to be traced
        for example, to trace the function f(x) you would decorate
        it by specifying a string to represent its argument when
        the trace is printed

            @Logger.trace('x')
            def f(x):
                return  x

        Then when f(x) is called, for example

        f(5)

        I have written this logger to print to stdout. It can be easily
        modified to print to any output stream including files. I use
        static functions to be trace but you could have different logger
        instantiations that used methods to print to different output
        streams. I leave it to the user to make such extensions.
        
        '''
        def function(f):
            def new_f(*args, **kwds):
                indent = Logger.indent * Logger.level
                print('{0}Entering {1}'.format(indent, f.__qualname__))
                Logger.level += 1
                for i, arg_name in enumerate(argnames):
                    Logger.log('{0}: {1}'.format(arg_name, args[i]))
                ans = f(*args, **kwds)
                Logger.level -= 1
                print('{0}Exiting {1} -> {2}'.format(indent, f.__qualname__, ans))
                return ans
            new_f.__qualname__ = f.__qualname__
            return new_f
        return function

    @staticmethod
    def log(msgs):
        prequel = Logger.indent * Logger.level
        for msg in msgs.split('\n'):
            print("{0}{1}".format(prequel, msg))

if __name__ == '__main__':
    class some_class:
        @Logger.trace('self','x')
        def __init__(self, x):
            self.x = x

        @Logger.trace('self', 'y')
        def add(self, y):
            return self.x + y

    @Logger.trace('i')
    def g(i):
        return 3 * i

    @Logger.trace('i', 'j')
    def f(i, j):
        Logger.log("I am about to instantiate some_class {0} time".format(1))
        a_class = some_class(g(i))
        return a_class.add(g(j))

    print("The answer is", f(3,4))
