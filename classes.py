#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:57:57 2021

@author: Ike Lockett
"""

class WordNumber():
    _num_convert = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        "ten": '10'
        "eleven": '11'
        }
    def __init__(self, number):
        if isinstance(number, int):
            self.number = str(number)
        elif isinstance(number, str):
            try:
                int(number)
                self.number = number
            except ValueError:
                try:
                    int(self._num_convert[number.lower()])
                    self.number = self._num_convert[number.lower()]
                except ValueError:
                    raise NotImplementedError("No such number (please raise a JIRA ticket)")

    def __repr__(self):
        return self.number

    def __str__(self):
        return self.__repr__() # TODO change to just return self.number for efficiency

    def __value__(self):
        return int(self.__str__())

    def __add__(self, other_num):
        _outcomes = """WordNumber: self.__value__() + int(other_num.__value__()),
            int: self.__value__() + other_num,
            str: self.__value__() + int(other_num)"""

        try:
            other_num = other_num.lower()
            int(other_num)
        except SyntaxError:
            other_num = other_num
        except AttributeError:
            pass
        except ValueError:
            try:
                other_num = self._num_convert[other_num]
            except KeyError:
                raise NotImplementedError(f"Cannot add this number to {self.__repr__()} yet")

        return self._execute_function(_outcomes, other_num)

    def __radd__(self, different_number):
        return self.__add__(different_number)

    def _execute_function(self, outcomes, other_num):
        for i in range(len(outcomes.split("\n"))):
            _cls = outcomes.split("\n")[i].split(":")[0]
            _func = outcomes.split("\n")[i].split(":")[1]
            if eval(_cls) == type(other_num):
                return eval(_func)
