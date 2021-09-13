
# Student ID: 1201200333 #
# Student Name : Seet Kok Peng #

BANANA = 1.5
GRAPE = 5.6

print("Invoice for Fruits Purchase")
print("---------------------------------\n")

banana = int(input("Enter the quantity (comb) of bananas bought: "))
grape = int(input("Enter the amount (kg) of grapes bought: "))
btotal = banana*BANANA
gtotal = grape*GRAPE
print("\nItem \t\tQty \tPrice \tTotal")
print("Banana (combs) \t{} \tRM{:.2f} \tRM{:.2f}".format(banana,BANANA,btotal))
print("Grapes (kg) \t{} \tRM{:.2f} \tRM{:.2f}".format(grape,GRAPE,gtotal))

total = (banana*BANANA) + (grape*GRAPE)

print("\nTotal: RM{:.2f}".format(total))