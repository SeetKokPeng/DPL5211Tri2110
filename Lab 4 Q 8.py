
#lab4.8.py given an array of 3,6,9,12,23 create array containing the squared number of each num
#from the first array
num=[3,6,9,12,23]
for i in num:
     print(i**2)

array = [3,6,9,12,23]
square=[]

for i in range(0,5) :
  square.append(array[i]*array[i])
  print(square[i])