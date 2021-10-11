
# Student ID: 1201200333
# Student Name : Seet Kok Peng

def get_bonus(unit,salary):
    
    if(unit>1000):
        bonus=salary*0.2
    elif(unit<1000 and unit>500):
        bonus=salary*0.1
    else:
        bonus=0
    
    return bonus

def get_nett_salary(bonus,salary):
    nettsalary=bonus+salary
    return nettsalary

def display(id,salary,unit,bonus,netsalary):
    print("\nStaff ID          : ",id)
    print("Staff salary      : RM {:.2f}".format(salary))
    print("Units sold        : ",unit)
    print("Bonus             : RM {:.2f}".format(bonus))
    print("Nett Salary       : RM {:.2f}".format(netsalary))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  DATA ENTRY                ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
id=int(input("Enter staff id       : "))
salary=float(input("Enter staff salary  : RM "))
unit=int(input("Enter total units sold : "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  SALARY SLIP               ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
bonus=get_bonus(unit,salary)
netsalary=get_nett_salary(salary,bonus)
display(id,salary,unit,bonus,netsalary)