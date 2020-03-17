class Insertionsort:
    name = "Insertion-Sort"

    def __init__(self):
        self.n_ops = 0

    def sort(self, array):
        for i in range(1, len(array)):
            for j in range(0, i):
                self.n_ops += 1
                if array[i] > array[j]:
                    array.insert(j, array.pop(i))
                    break