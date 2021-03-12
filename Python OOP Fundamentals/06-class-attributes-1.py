# 06-class-attributes-1.py

# Here we define an attribute under the class `YourClass`
# as well as an attribute within the function.

# The attribute defined in the class is called `class attributes`
# and the attribute defined in the function is called `instance attributes`.
class YourClass(object):
    # This is a class attribute
    classy = 10

    def set_val(self,):
        # This is an instance attribute
        self.insty = 100


dd = YourClass()
print(dd.classy)   # This will fetch the class attribute 10.
# If set_val() function is not called the dd.insty value will not be instantiated and therefore, won't be printed
dd.set_val()
print(dd.insty)    # This will fetch the instance attribute 100.

# Once `dd` is instantiated, we can access both the class and instance
# attributes, ie.. dd.classy and dd.insty.
