def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")


def call_exceptor():
    print("call_exceptor starts here...")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")


try:
    no_return()
except:
    print("I caught an exception")
print("executed after the exception")
