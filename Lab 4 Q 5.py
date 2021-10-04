
# Student ID: 1201200333
# Student Name : Seet Kok Peng

#lab4.5 get input for a number from 1 until 12 using the fot loop display the multiplication tables

num = (input("Enter a number from (1 to 12)"))

for num in range(1, 12, 2):
    print("Number is :", num)

num=int(input("Enter the number from 1 to 10 : "))
#
for i in range(1,11):
    print(num*i)
#
num=int(input("enter the number you wanna do mutliplication(1-10):"))
i=0
for i in range(1,13):
    print(num,"*",i,"=",num*i)
#
num=int(input("enter the number you wanna do mutliplication(1-10):"))
i=0
for i in range(1,13):
    print(num,"*",i,"=",num*i)
#
number=int(input("Enter the number you want(1-10) : "))
for i in range(1,11):
    print(number,"x",i,"=",number*i)