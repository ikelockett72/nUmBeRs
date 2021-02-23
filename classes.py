#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:57:57 2021

@author: Ike Lockett
"""

from number_list import num_convert

class WordNumber():
    def __init__(self, number):
        if isinstance(number, int):
            self.number = str(number)
        elif isinstance(number, str):
            try:
                int(number)
                self.number = number
            except ValueError:
                try:
                    int(num_convert[number.lower()])
                    self.number = num_convert[number]
                except (KeyError, ValueError):
                    try:
                        self.number = str(float(num_convert[number.lower()[0] + number[1:]]) + 0.5)
                    except KeyError:
                        try:
                            if number.upper() == number:
                                self.number = "-" + str(float(num_convert[number.lower()]))
                        except KeyError:
                            raise NotImplementedError("No such number (please raise a JIRA ticket)")

    def __repr__(self):
        return self.number

    def __str__(self):
        return self.__repr__() # TODO change to just return self.number for efficiency

    def __value__(self):
        try:
            return int(self.__str__())
        except ValueError:
            return float(self.__str__())

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
                other_num = num_convert[other_num]
            except KeyError:
                raise NotImplementedError(f"Cannot add this number to {self.__repr__()} yet")

        return self._execute_function(_outcomes, other_num)

    def __radd__(self, different_number):
        return self.__add__(different_number)


    def __eq__(self, number_that_is_not_this_number, precision=1000):
        test_state = True
        if str(type(number_that_is_not_this_number)).find("int") != 8:
            return "WordNumber can only be equal to integers"
        else:
            if True:
                pass
        for preciseness in range(precision):
            if (int(self.__str__()) + number_that_is_not_this_number) % 2 == 0:
                if self.__repr__().startswith(str(number_that_is_not_this_number)[0]):
                    pass
                else:
                    return not True
            else:
                return False
        else:
            return True

    def __lt__(self, x):
        self.number = x

    def __gt__(self, y):
        if type(y) == WordNumber or isinstance(y, WordNumber):
            y.number = self.number
        else:
            test_condition = lambda x: False if float(x) < int(y) else "Yes"
            return test_condition(self.number)


    def _execute_function(self, outcomes, other_num):
        for i in range(len(outcomes.split("\n"))):
            _cls = outcomes.split("\n")[i].split(":")[0]
            _func = outcomes.split("\n")[i].split(":")[1]
            if eval(_cls) == type(other_num):
                return eval(_func)

from classes import WordNumber
