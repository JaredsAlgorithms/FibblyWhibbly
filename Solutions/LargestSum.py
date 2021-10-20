import math


class LargestSumSolution:
    # accepts list[int], list[float] or any integer like object container

    def solution(self, container: list[int]):  # -> list[int, int]
        """
        Largest sum
        """

        if not container:
            return [math.inf, math.inf]

        b, e, n = 0, 1, len(container)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if(sum(container[i:j]) > sum(container[b:e])):
                    b, e = i, j

        return [b, e]
