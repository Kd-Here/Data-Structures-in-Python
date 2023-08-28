import sys
sys.path.append('../')

from HashMap import Dictionari


CheckingIn = []
Checker = []
with open('poem.txt','r') as file:
    for i in file:
        k = i.strip()
        c = k.split(" ")
        if "" not in c:
            CheckingIn.append(c)
            for j in c:
                Checker.append(j)
                

K = Dictionari()
for i in Checker:
    count = 0
    for j in CheckingIn:
        a = j.count(i)
        count += a 
    K[i] = count


for i in range(0,3):
    j = K.bucket[i].head
    while j is not None:
        print(f"'{j.key}' : {j.value}")
        j = j.address