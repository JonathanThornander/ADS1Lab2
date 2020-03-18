class Mergesort:
    name = "Merge Sort"
    
    def __init__(self):
        self.n_ops = 0

    def sort(self, arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #Finding the mid of the array 
            L = arr[:mid] # Dividing the array elements  
            R = arr[mid:] # into 2 halves 
    
            self.sort(L) # Sorting the first half 
            self.sort(R) # Sorting the second half 
    
            i = j = k = 0
           
            while i < len(L) and j < len(R): # Copy data to temp arrays L[] and R[] 
                self.n_ops += 1
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
            
            while i < len(L):  # Checking if any element was left 
                arr[k] = L[i] 
                i+=1
                k+=1
            
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
