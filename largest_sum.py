#!/usr/bin/env python3.9

import math
import unittest


class LargestSumSolution:
    def __init__(self):
        pass

    def solution(self, container: list[int]) -> list[int]:
        if not container:
            return [math.inf, math.inf]

        b, e, n = 0, 1, len(container)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if(sum(container[i:j]) > sum(container[b:e])):
                    b, e = i, j

        return [b, e]


solution = LargestSumSolution()


class ExampleTester(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(solution.solution([]) == [math.inf, math.inf])

    def test_sample_data(self):
        input_data = [
            [-3, -5, 5, -1, -3, 1, 5, -6],
            [10, 2, -5, 1, 9, 0, -4, 2, -2],
            [-7, 1, 8, 2, -3, 1],
            [9, 7, 2, 16, -22, 11],
            [6, 1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4]
        ]
        validated_data = [
            [5, -1, -3, 1, 5],
            [10, 2, -5, 1, 9],
            [1, 8, 2],
            [9, 7, 2, 16],
            [7, 2, 9, 1, -3, 8, -2, 9, 12]
        ]

        for (candidate, correct_solution) in zip(input_data, validated_data):
            i, j = solution.solution(candidate)
            self.assertTrue(candidate[i:j] == correct_solution)


unittest.main()
