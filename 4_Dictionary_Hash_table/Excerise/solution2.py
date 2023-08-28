import csv
import sys
sys.path.append('../')

from HashMap import Dictionari,LinkedList,Node

K = Dictionari()
with open('nyc_weather.csv' ,'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row

        for i in csv_reader:
                K[i[0]] = i[1]

placeholde = f"Jan "
avg = sum(int(K[placeholde+str(i)]) for i in range(1,8))
print(avg/7)

maximum = max(int(K[placeholde+str(i)]) for i in range(1,11))
print(maximum)

print(K['Jan 9'])
print(K['Jan 4'])