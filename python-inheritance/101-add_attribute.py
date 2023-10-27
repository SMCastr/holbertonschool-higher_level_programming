#!/usr/bin/python3
""" 101-main """


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.
    """
    
    if not hasattr(obj, '__dict__') and not (hasattr(obj, '__slots__')
            and attr_name in obj.__slots__):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
