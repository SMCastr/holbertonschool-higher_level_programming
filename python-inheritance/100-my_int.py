#!/usr/bin/python3
""" 100-main """


class MyInt(int):
    """ MyInt class"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
