#!/usr/bin/python3

def lookup(obj):
    """
    This function takes an object 'obj' as input and returns a list of its available attributes and methods.
    
    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        A list of attribute and method names as strings.

    """
    return dir(obj)


# Example usage

if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
