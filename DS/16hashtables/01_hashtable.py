class HashTable: 
    def __init__(self,size = 7):
        self.data_map = [None]*size
    
    def __hash(self,key):
        myhash = 0
        for letter in key:
            myhash = (myhash + ord(letter)* 23 ) % len(self.data_map) # 23 is random prime number , ord gives ascii value
        
        return myhash
    
    def printTable(self):
        print("---Start---")
        for i , val in enumerate(self.data_map):
            print(i , " : ",val )
        print("--END---")

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for k,v in enumerate(self.data_map[index]):
                if v[0] == key:
                    return v[1]
            
        return None

    def get_keys(self):
        allkey = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    allkey.append(self.data_map[i][j][0])
        return allkey


    
mytable = HashTable()
mytable.printTable()
mytable.set_item('my','my')
mytable.set_item('myy','myy')
mytable.set_item('myyy','myyy')
mytable.set_item('myyyy','myyyy')
mytable.set_item('myyyyy','myyyyy')
mytable.set_item('myyyyyy','myyyyyy')
mytable.set_item('myyyyyyy','myyyyyyy')
mytable.set_item('myyyyyyyy','myyyyyyyy')
mytable.printTable()
print("found value for key : ",mytable.get_item("my"))
print(mytable.get_keys())