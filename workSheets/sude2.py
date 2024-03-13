import sys

class MyClass:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

# Creating an instance of MyClass
obj1 = MyClass('obj1')
print(f"Reference count for obj1: {sys.getrefcount(obj1) - 1}")  # Subtract 1 to exclude the getrefcount reference itself

# Creating another reference, ref_obj1, to the same object
ref_obj1 = obj1
print(f"Reference count for obj1: {sys.getrefcount(obj1) - 1}")

# Deleting one reference
del obj1
print(f"Reference count for ref_obj1: {sys.getrefcount(ref_obj1) - 1}")

# Deleting the second reference should trigger the __del__ method
del ref_obj1  # After this point, "obj1 destroyed" is printed, indicating the object is garbage collected
