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
    
            # reset the swapped flag on entering the loop, 
            # because it might be true from a previous 
            # iteration. 
            swapped = False
    
            # loop from left to right same as the bubble 
            # sort 
            for i in range (start, end): 
                self.n_ops += 1
                if (array[i] > array[i+1]) : 
                    array[i], array[i+1]= array[i+1], array[i] 
                    swapped=True
    
            # if nothing moved, then array is sorted. 
            if (swapped==False): 
                break
    
            # otherwise, reset the swapped flag so that it 
            # can be used in the next stage 
            swapped = False
    
            # move the end point back by one, because 
            # item at the end is in its rightful spot 
            end = end-1
    
            # from right to left, doing the same 
            # comparison as in the previous stage
            self.n_ops += 1
            for i in range(end-1, start-1,-1): 
                if (array[i] > array[i+1]): 
                    array[i], array[i+1] = array[i+1], array[i] 
                    swapped = True
    
            # increase the starting point, because 
            # the last stage would have moved the next 
            # smallest number to its rightful spot. 
            start = start+1