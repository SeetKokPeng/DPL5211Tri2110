
# Student ID: 1201200333
# Student Name : Seet Kok Peng

def rectangle(rec,l):
    main = rec * l
    return main

def triangle(tri,l):
    main = tri * l / 2
    return main

width = float(input("Enter the width   : "))
length = float(input("Enter the length  : "))

area_rec = rectangle(width,length)
area_tri = triangle(width,length)

print("Rectangle area : {:.2f}".format(area_rec))
print("Triangle area  : {:.2f}".format(area_tri))
