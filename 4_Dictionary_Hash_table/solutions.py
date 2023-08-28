# Hash Table Collision Handling Using Chaining here implemented using 2d list

class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.bucket = [ [None] for i in range(self.size)]
        # Here created bucket of size 100 i.e 100 places to store index,
        # In them each is list 

    def hashed_value_by_modulus(self,index):
        total_asci = sum(ord(i) for i in index)
        bucket_index = total_asci % 10
        return bucket_index


    # def append()
    def __setitem__(self,index,value):
        bucket_index = self.hashed_value_by_modulus(index)

        for i in range(len(self.bucket)):

            # To check if index of bucket match the hashed modulus output
            
            if bucket_index == i:
                # If bucket is empty add first element
                if self.bucket[i] == [None]:
                    self.bucket[i][0] = [index,value]

                # This to check duplicate if yes change the value
                for j in range(len(self.bucket[i])):
                    if self.bucket[i][j][0] == index:
                        self.bucket[i][j][1] = value
                        break
                        

                # This to append new list in existing index
                else:
                    self.bucket[i].append([index,value])

    def __getitem__(self,index):
        bucketindex = self.hashed_value_by_modulus(index)
        for i in range(len(self.bucket)):
            if bucketindex == i:
                for j in self.bucket[i]:
                    if j[0] == index:
                        return j[1]


    def __delitem__(self,index):
        bucketindex = self.hashed_value_by_modulus(index)
        for i in range(len(self.bucket[bucketindex])):
            if self.bucket[bucketindex][i][0] == index:
                 del self.bucket[bucketindex][i]
                 break

K = HashTable()
K['march 1'] = 123
K['march 2'] = 456
K['march 3'] = 789
K['march 4'] = 234
K['march 5'] = 567
K['march 6'] = 890
K['march 7'] = 321
K['march 8'] = 654
K['march 9'] = 987

del K['march 1']
print(K.bucket)
