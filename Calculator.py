#use case - This code is used to perform various calculations like addition, division, etc. and gives us the result for the chosen operator 
print("Welcome to Calculator!") 

def calculations():
    print("1. Addition(+), 2. Subtraction(-), 3.Multiplication(*), 4.Division(/) ") #Options that are available in this calculator
    Operation = int(input("Enter the number of the operation that you want to perform(1/2/3/4): "))

    n1 = int(input("Enter a number: ")) #variable to store the first number for calculations
    n2 = int(input("Enter another number:")) #variable to store the second number for calculations
    if Operation == 1:
        result = n1 + n2
        print(result)
    elif Operation == 2:
        result = n1 - n2
        print(result)
    elif Operation == 3:
        result = n1 * n2
        print(result)
    elif Operation == 4:
        result = n1/n2
        print(result)
    else:
        print("Please enter a valid number according to the list offered.")     

#This part of the code is used to ask the user if they want to perform more calculations.
def go_again():
    while True:
        again = input("Do you want to calculate once more? (yes/no):").lower()
        if again == 'yes':
            calculations()
        else:
            break  

calculations()     
go_again()  
