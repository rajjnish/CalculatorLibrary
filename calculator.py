"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(number, divider):
    return number // divider


def even_no_check(num):
    if num % 2 == 0:
        return True
    else:
        return False
