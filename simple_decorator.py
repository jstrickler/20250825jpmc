from functools import wraps
import logging
logging.basicConfig(
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
    datefmt="%x-%X",
    filename="functions.log",
    level=logging.INFO
)

def logtimestamp(func):

    @wraps(func)
    def _wrapper(*args, **kwargs):
        logging.info(func.__name__) # purpose of this decorator
        return func(*args, **kwargs)
    
    return _wrapper

@logtimestamp
def spam(x):
    print("spam spam spam")
    return 8 * x
# spam = mydeco(spam)
@logtimestamp
def ham():
    print("ham")

x = spam(1)
y = spam(22)
print(x, y)
print(spam)
print(ham)
spam(5)
spam(10)
ham()

registry = {}

def register_func(func):
    registry[func.__name__] = func
    return func

@register_func
def foo():
    print("foo!")
@register_func
def bar():
    print("bar!")

print(f"{registry = }")
registry['foo']()