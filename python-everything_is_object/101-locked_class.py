#!/usr/bin/python3
""" Module that creates a locked class"""
class LockedClass:
    """ Class that prevents the user from
    dynamically creating new instance"""
    __slots__ = ['first_name']
