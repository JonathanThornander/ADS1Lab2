class Map:
    name = "Hashtable"
    def __init__(self, size):
        self.size = size // 2
        self.table = list([None]*self.size)

    def put(self, key, val):
        idx = self.hashfunction(key)

        if self.table[idx] == None:
            self.table[idx] = [[key, val]]
        else:
            # Begin linear search
            l = self.table[idx]
            for kv_pair in l:
                if kv_pair[0] == key:
                    kv_pair[1] = val
                    return
            l.append([key, val])

    def get(self, key):
        idx = self.hashfunction(key)
        if self.table[idx] == None:
            return None
        else:
            l = self.table[idx]
            for kv_pair in l:
                if kv_pair[0] == key:
                    return kv_pair[1]
            return None

        
    def delete(self, key):
        idx = self.hashfunction(key)
        if self.table[idx] == None:
            print("1 not found")
            return
        else:
            l = self.table[idx]
            for kv_pair in l:
                if kv_pair[0] == key:
                    l.remove(kv_pair)
                    return
            print("2 not found")

    def length(self):
        count = 0
        for l in self.table:
            if l:
                for _ in l:
                    count += 1
        return count

    def contains(self, key):
        idx = self.hashfunction(key)
        if self.table[idx] == None:
            return False
        else:
            l = self.table[idx]
            for kv_pair in l:
                if kv_pair[0] == key:
                    return True
            return False

    def hashfunction(self, key):
        return key % self.size