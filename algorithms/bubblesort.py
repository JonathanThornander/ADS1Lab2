class Bubblesort:
    name = "BubbleSort"
    
    def __init__(self):
        self.n_ops = 0

    def sort(self, array):
        n = len(array) 

        for i in range(n): 
    
            for j in range(0, n-i-1): 
                
                self.n_ops += 1
                if array[j] > array[j+1] : 
                    array[j], array[j+1] = array[j+1], array[j] 