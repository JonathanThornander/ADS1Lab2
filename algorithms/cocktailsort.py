# Works in the same way as bubblesort, with the addition of moving elements both up the index aswell as down. 
# This makes it the same complexity as bubblesort, but slightly faster on average. It is built in the same way as
# bubblesort, but has more checks on what parts of the list that is already sorted.

class Cocktailsort:
    name = "Coctail-Sort"

    def __init__(self):
        self.n_ops = 0

    def sort(self, array): 
        n = len(array) 
        swapped = True
        start = 0
        end = n-1
        while (swapped==True): 
   
            swapped = False
     
            for i in range (start, end): 
                self.n_ops += 1
                if (array[i] > array[i+1]) : 
                    array[i], array[i+1]= array[i+1], array[i] 
                    swapped=True
    
            if (swapped==False): 
                break
    
            swapped = False
    
            end = end-1
    
            self.n_ops += 1
            for i in range(end-1, start-1,-1): 
                if (array[i] > array[i+1]): 
                    array[i], array[i+1] = array[i+1], array[i] 
                    swapped = True
    
            start = start+1
