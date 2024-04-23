#Hash Map

class HashMap:
    def __init__(self):
        self.name = ''
        self.size = 64
        self.map = [None] * self.size

    #Create a hash key using the input key
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    #Adds key and value to the Hash map
    def setName(self, name):
        self.name = name

    def add(self, key, value):
        keyHash = self._get_hash(key)
        keyValue = [key, value]

        #If the hash key doesn't exist in the array, add the key value pair to the hashmap with the hash key
        if self.map[keyHash] == None:
            self.map[keyHash] = list([keyValue])
            return True
        
        #If the hash key already exists in the array
        else:
            #Check all pairs in the hash key, if one of them equal the key, set the new value as the key pair
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                
            #If no keys match, append the new key value pair into the hash key array
            self.map[keyHash].append(keyValue)
            return True
        
    def get(self, key): 
        keyHash = self._get_hash(key)

        #If hash key exists
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]: 
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        keyHash = self._get_hash(key)

        if self.map[keyHash] is None: 
            return False
        
        #for loop to look through every pair in key hash
        for i in range(0, len(self.map[keyHash])):
            
            #if key matches the input key, pop the pair at that index
            if self.map[keyHash][i][0] == key:
                self.map[keyHash].pop(i)
                return True
            
    def print(self):
        print('----' + self.name + '----')
        for item in self.map:
            if item is not None:
                print(str(item))
