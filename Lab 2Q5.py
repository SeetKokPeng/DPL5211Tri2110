
# Student ID:1201200333 #
# Student Name: Seet Kok Peng #

LITRE = 0.15
print("Natural Mineral Water Dispenser")
print("---------------------------------\n")

litre = int(input("Enter amount of litres: "))
print("\nPrice per litre    = RM {}".format(LITRE))
print("Number per liters  = {}".format(litre))

total = litre * LITRE
print("Total: RM {:.2f}".format(total))