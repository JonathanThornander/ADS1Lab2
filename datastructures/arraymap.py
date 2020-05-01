import random

class Map:
    name = "Array Map"
    def __init__(self, size):
        self.items = []
        
    def put(self, key, val):
        if len(self.items) == 0:
            self.items.append([key, val])
        else:
            l = 0
            r = len(self.items) - 1

            while l <= r:
                mid = l + (r - l) // 2
                
                if self.items[mid][0] == key: 
                    self.items[mid][1] = val
                    return
                
                if mid == l == r:
                    if key > self.items[mid][0]:
                        self.items.insert(mid + 1, [key, val])
                    else:
                        self.items.insert(mid, [key, val])
                    return
        
                elif self.items[mid][0] < key: 
                    l = mid + 1
                else: 
                    r = mid - 1

            self.items.insert(mid, [key, val])
            return
        
                
    def get(self, key):
        l = 0
        r = len(self.items) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            if self.items[mid][0] == key: 
                return self.items[mid][1] 
    
            elif self.items[mid][0] < key: 
                l = mid + 1
    
            else: 
                r = mid - 1
      
        return None

    def delete(self, key):
        l = 0
        r = len(self.items) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            if self.items[mid][0] == key: 
                self.items.remove(self.items[mid])
                return
    
            elif self.items[mid][0] < key: 
                l = mid + 1
    
            else: 
                r = mid - 1
    
    def length(self):
        return len(self.items)

    def contains(self, key):
        l = 0
        r = len(self.items) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            if self.items[mid][0] == key: 
                return True
    
            elif self.items[mid][0] < key: 
                l = mid + 1
    
            else: 
                r = mid - 1
      
        return False