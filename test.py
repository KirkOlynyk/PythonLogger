'''
test.py
'''
from logger import Logger

class AClass:
    @Logger.trace('self', 'x')
    def __init__(self, x):
        self.x = x
    
    @Logger.trace('self', 'y')
    def add(self, y):
        return self.x + y

    @staticmethod
    @Logger.trace('x')
    def a_staticmethod(x):
        return x

    def __repr__(self):
        return "x={0}".format(self.x)

@Logger.trace('x')
def a_function(x):
    return x

@Logger.trace()
def main() -> None:
    aClass = AClass(3)
    x = AClass.a_staticmethod(2)
    print('The answer is', aClass.add(x))

if __name__ == '__main__':
    main()
