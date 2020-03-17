class SelectionSort:
    name = "Selection Sort"
    
    def __init__(self):
        self.n_ops = 0

    def sort(self, array):
        for i in range(len(array)):
            min_index = i
            for j in range(i+1, len(array)):
                self.n_ops += 1
                if array[min_index] > array[j]:
                    min_index = j

            array[min_index], array[i] = array[i], array[min_index]