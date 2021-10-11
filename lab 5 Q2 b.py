
# Student ID: 1201200333
# Student Name : Seet Kok Peng

def rectangle(rec,l):
    main = rec * l
    return main

def triangle(tri,l):
    main = tri * l / 2
    return main

i = 0
while(i<2):
    wid = float(input("Enter width   : "))
    leng = float(input("Enter length  : "))

    area_rec = rectangle(wid,leng)
    area_tri = triangle(wid,leng)

    print("Rectangle area : {:.2f}".format(area_rec))
    print("Triangle area  : {:.2f}".format(area_tri))
    i += 1