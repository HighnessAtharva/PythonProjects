# 05-init_constructor-2.py

# We add a test in the __init__() constructor to check
# if 'value' is an int or not.


class MyNum(object):
    def __init__(self, value=0):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def increment(self):
        self.value = self.value + 1
        print(self.value)


a = MyNum()  # defaults to 0
a = MyNum("Starters")  # Try Except sets this to 0
a.increment()   # This should print 1
a.increment()   # This should print 2
a.getValue
a.setValue(49999)
a.increment()
a.getValue
