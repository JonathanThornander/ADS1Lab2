import random

# All classes bellow have solely static variables and methods

class SortedData:
    name = "Sorted Data"

    @staticmethod
    def data(n):
        return list(range(n))

class ReversedData:
    name = "Reversed Data"

    @staticmethod
    def data(n):
        l = list(range(n))
        l.reverse()
        return l

class UnsortedData:
    name = "Unsorted Data"

    @staticmethod
    def data(n):
        return [random.randint(1, 99) for x in range(n)]

class AlmostSortedData:
    name = "Almost Sorted Data"

    @staticmethod
    def data(n):
        # Makes every 10th item switch 2 places
        return list(map(lambda x: x if x%10 != 0 else x+2, SortedData.data(n))) 