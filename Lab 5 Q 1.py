
# Student ID: 1201200333
# Student Name : Seet Kok Peng

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Please enter a value for centimeter :"))
    m= cm_to_meter (cm)
    print("{:.2f} cm is {:.2f} meter ". format(cm, m))

get_cm()