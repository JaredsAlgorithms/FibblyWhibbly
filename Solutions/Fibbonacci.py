#!/usr/bin/env python3.9

import math
import unittest

import tabulate


class FibbonacciSolution:
    def __init__(self):
        self.GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

    def recursive(self, n: int) -> int:
        """
        Fibbonaci sequence using recursion
        """

        if(n <= 1):
            return n
        return self.recursive(n-1) + self.recursive(n-2)

    def printer(self, function, n) -> None:
        """
        Print the Fibbonaci sequence of n elements
        """

        for x in range(0, n):
            print(function(x))

    def current_fib_index(self, n: int) -> int:
        numerator = (1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n
        denominator = (2 ** n) * math.sqrt(5)

        return int(numerator / denominator)

    def polynomial_fib(self, n: int) -> list[int]:
        return [self.current_fib_index(x) for x in range(0, n)]

    def previous_fib(self, n: int, p: int) -> float:
        return self.current_fib_index(p) * (math.pow(self.GOLDEN_RATIO, n - p))

    def next_fib(self, n: int) -> float:
        return self.current_fib_index(n+1) * self.GOLDEN_RATIO

    def user_fib(self, n: int):
        # I really hate the way try except blocks look in Python
        print(f"[INFO] Value of `n` is {n}")
        _exit_condition = False
        p = math.inf

        while not _exit_condition:
            try:
                captured = input("[INPUT] Value of p: ")
                p = int(captured)
            except ValueError:
                print(
                    f'[ERROR] Malformed expression, cannot convert `{captured}` into an integer like object!')
                continue
            _exit_condition = True
        estimated = [self.previous_fib(n, p)]
        actual = [self.current_fib_index(n)]
        information = {
            "n": [n],
            "p": [p],
            "estimated value": estimated,
            "actual value": actual,
            "divergence": [abs(a - b) for (a, b) in zip(estimated, actual)]
        }

        print(tabulate.tabulate(information, headers='keys', tablefmt='fancy_grid'))

    def compare_equations(self, n: int, p: int):
        # equation 2 (previous)
        _previous = self.previous_fib(n, p)
        _next = self.next_fib(n)

        return [_previous, _next]


Solution = FibbonacciSolution()
