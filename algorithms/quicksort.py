import random

class QuickSort:
    name = "Quicksort"

    def __init__(self):
        self.n_ops = 0

    def sort(self, arr):
        self.inPlaceQuickSort(arr, 0, len(arr)-1)

    def inPlaceQuickSort(self, A,start,end):
        if start<end:
            pivot=random.randint(start,end)
            # temp=A[end]
            # A[end]=A[pivot]
            # A[pivot]=temp

            A[end], A[pivot] = A[pivot], A[end]
            
            p=self.inPlacePartition(A,start,end)
            self.inPlaceQuickSort(A,start,p-1)
            self.inPlaceQuickSort(A,p+1,end)


    def inPlacePartition(self, A,start,end):
        pivot=random.randint(start,end)
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        newPivotIndex=start-1
        for index in range(start,end):
            self.n_ops += 1
            if A[index]<A[end]:#check if current val is less than pivot value
                newPivotIndex=newPivotIndex+1
                temp=A[newPivotIndex]
                A[newPivotIndex]=A[index]
                A[index]=temp
        temp=A[newPivotIndex+1]
        A[newPivotIndex+1]=A[end]
        A[end]=temp
        return newPivotIndex+1