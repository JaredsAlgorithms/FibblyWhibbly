#!/usr/bin/env python3.9

import math
import unittest


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


Solution = FibbonacciSolution()


class ExampleTest(unittest.TestCase):
    @unittest.skip("slowbro")
    def test_recursion(self):
        """
        This test will be slow because recursion sucks..most of the time
        """

        values = [0, 1, 1, 2, 3, 5, 8, 13, 21,
                  34, 55, 89, 144, 233, 377, 610, 987]
        for x, element in enumerate(values):
            solution = Solution.recursive(x)
            self.assertTrue(solution == element)

    @unittest.skip("solution working for polynomial efficiency")
    def test_iterative(self):
        values = [0, 1, 1, 2, 3, 5, 8, 13, 21,
                  34, 55, 89, 144, 233, 377, 610]
        self.assertTrue(values == Solution.polynomial_fib(16))

    # @unittest.skip("solution sort of working")
    def test_prev(self):
        values = ', '.join([str(Solution.previous_fib(x+1, x))
                            for x in range(0, 21)])
        print(values)

    def test_next(self):
        values = ', '.join([str(Solution.next_fib(x))
                            for x in range(0, 21)])
        print(values)

    def test_demonstrate_prev(self):
        n = 20
        value_of_p = int(input("[INPUT] Value of p: "))
        print(Solution.previous_fib(n, value_of_p))


unittest.main()
