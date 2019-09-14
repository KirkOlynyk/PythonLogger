'''
logger.py

For logging functions/methods
'''
# pylint: disable=invalid-name, too-few-public-methods

import inspect

def isinit(a_function):
    'determines if a function object is an __init__ for a class'
    if hasattr(a_function, '__name__'):
        if a_function.__name__ == '__init__':
            if inspect.isfunction(a_function):
                return True
    return False

class Logger:
    'Used to log functions/methods'
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
            'wrapper function to be used to overwrite the original function/method'
            def new_f(*args, **kwds):
                indent = Logger.indent * Logger.level
                print('{0}Entering {1}'.format(indent, f.__qualname__))
                Logger.level += 1
                is_init = isinit(f)
                for i, arg_name in enumerate(argnames):
                    if i == 0 and is_init:
                        Logger.log('{0} at 0x{1:016X}'.format(arg_name, id(args[i])))
                    else:
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
        'For printing an arbitrary message'
        prequel = Logger.indent * Logger.level
        for msg in msgs.split('\n'):
            print("{0}{1}".format(prequel, msg))
