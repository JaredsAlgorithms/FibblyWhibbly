from Solutions.Fibbonacci import FibbonacciSolution

import re
import tabulate


def gather_tests(class_object):  # -> list[str]
    return [test for test in dir(class_object) if re.match(
        "test_[a-zA-Z0-9]+", test) and (test != "test_all")]


class FibbonaciUnitTests:
    def __init__(self):
        self.Solution = FibbonacciSolution()

    def test_recursion(self):
        """
        Test recursive Fibbonaci sequence
        """

        values = [0, 1, 1, 2, 3, 5, 8, 13, 21,
                  34, 55, 89, 144, 233, 377, 610, 987]
        for x, element in enumerate(values):
            solution = self.Solution.recursive(x)
            assert(solution == element)
        print("[SUCCESS] All assertions passed for test_recursion!")

    def test_iterative(self):
        """
        Test Fibbonaci Sequence in linear time
        """

        values = [0, 1, 1, 2, 3, 5, 8, 13, 21,
                  34, 55, 89, 144, 233, 377, 610]
        assert(values == self.Solution.polynomial_fib(16))

        print("[SUCCESS] All assertions passed for test_iterative!")

    def test_prev(self):
        """
        Test Fibbonaci relationship with previous element
        """

        print(
            "[INFO] Printing the first 20 digits of the Fibbonaci sequence using Equation #2.......")

        information = {
            "Index": [_ for _ in range(1, 22)],
            "Values": [self.Solution.previous_fib(x+1, x) for x in range(1, 22)]
        }
        print(tabulate.tabulate(information, headers='keys', tablefmt='fancy_grid'))

    def test_next(self):
        """
        Test Fibbonaci relationship with next element
        """

        print(
            "[INFO] Printing the first 20 digits of the Fibbonaci sequence using Equation #3.......")
        information = {
            "Index": [_ for _ in range(0, 21)],
            "Values": [self.Solution.next_fib(x) for x in range(0, 21)]
        }
        print(tabulate.tabulate(information, headers='keys', tablefmt='fancy_grid'))

    def test_demonstrate_prev(self):
        """
        Show relationship when `p` diverges from `n` in any given direction
        """

        self.Solution.user_fib(20)

    def test_compare(self):
        """
        Where `p` is fixed at the same length as `n+1`
        """

        n = 33
        next_container, current, previous_container = [], [], []
        for x in range(1, n+1):
            _prev, _next = self.Solution.compare_equations(x, x-1)
            previous_container.append(_prev)
            current.append(self.Solution.current_fib_index(x))
            next_container.append(_next)

        information = {
            "Index": [_ for _ in range(1, n+1)],
            "Previous": previous_container,
            "Current": current,
            "Next": next_container,
            # there seems to be an extraneous `1` here, not sure why
            "Ratio": [(float(b) / float(a)) - 1 if a > 0 else 0 for (a, b) in zip(previous_container, next_container)]
        }

        print(tabulate.tabulate(information, headers='keys', tablefmt='fancy_grid'))

    def test_all(self):
        for test in gather_tests(self):
            function = getattr(self, test)
            function()
