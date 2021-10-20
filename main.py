#!/usr/bin/env python3

from AllUnitTests.Fib import FibbonaciUnitTests
from AllUnitTests.Sum import LargestSumUnitTests

import os

fibboanci = FibbonaciUnitTests()
largest_sum = LargestSumUnitTests()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


tickets = {
    "1": fibboanci.test_recursion,
    "2": fibboanci.test_iterative,
    "3": fibboanci.test_prev,
    "4": fibboanci.test_next,
    "5": fibboanci.test_compare,
    "6": largest_sum.test_empty,
    "7": largest_sum.test_sample_data
}

options = [
    "Test recursive Fibbonaci",
    "Test iterative Fibbonaci",
    "Test previous relationship (equation #2)",
    "Test next relationship (equation #3)",
    "Compare equation #2 and #3 with `n` of 33",
    "Test largest sum with empty container",
    "Test largest sum with provided data"
]

_exit_condition = True

while _exit_condition:
    for x, option in enumerate(options):
        print(f'[{x+1}]: {option}')

    try:
        _option = input("[INPUT] Select option: ")
    except EOFError:
        break
    _current_ticket = tickets.get(_option)

    clear()

    if not _current_ticket:
        print("[ERROR]: Invalid selection, please try again")
    else:
        # func_name = _current_ticket.func.__func__.__name__
        print(f'[INFO] Running {_current_ticket.__name__}')
        _current_ticket()
