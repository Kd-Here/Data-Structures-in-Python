class HashMapLinearProbing:
    def __init__(self) -> None:
        self.Max = 10
        self.bucket = [None for i in range(1,11)]

    def hashvalue(self,input):
        a = sum (ord(i) for i in input)
        bucketindex = (a%3)
        return bucketindex
    
    def __setitem__(self,index,value):
        bucketindex = self.hashvalue(index)
        if self.bucket[bucketindex] is None:
            self.bucket[bucketindex] = (index,value)
        else:
            for i in range(len(self.bucket)):
                if self.bucket[i] is None:
                    self.bucket[i] = (index,value)
                    break

    def __getitem__(self,index):
        bucketindex = self.hashvalue(index)
        if index == self.bucket[bucketindex][0]:
            return self.bucket[bucketindex][1]
        else:
            for i in range(len(self.bucket)):
                if self.bucket[i][0] == index:
                    return self.bucket[i][1] 
        # return self.bucket[bucketindex]
        


K = HashMapLinearProbing()



K['march 3'] = 120
K['march 9'] = 123
print(K.bucket)