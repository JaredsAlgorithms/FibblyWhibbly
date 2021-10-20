from Solutions.LargestSum import LargestSumSolution

import math


class LargestSumUnitTests:
    def __init__(self):
        self.solution = LargestSumSolution()

    def test_empty(self):
        assert(self.solution.solution([]) == [math.inf, math.inf])
        print("[SUCCESS] All assertions passed for `test_empty`!")

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
            i, j = self.solution.solution(candidate)
            assert(candidate[i:j] == correct_solution)

        print("[SUCCESS] All assertions passed for `test_sample_data`!")
