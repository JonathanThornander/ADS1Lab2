import random
import numpy as np

class RandomData:
    name = "Random Data"

    @staticmethod
    def data(n):
        l = list(np.random.permutation(n))
        for i in range(len(l)):
            l[i] = [l[i], "Val"]
        return l

class SortedData:
    name = "Sorted Data"

    @staticmethod
    def data(n):
        return [[x, "Val"] for x in range(n)]