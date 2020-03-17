from itertools import permutations

class Bogosort:
    name = "Bogo-sort"

    def __init__(self):
        self.n_ops = 0

    def sort(self, arr):
        for k in permutations(arr):
            for m in range(len(k)-1):
                self.n_ops += 1
                if k[m]<=k[m+1]:
                    pass
                else:
                    break
            else:    
                return k
