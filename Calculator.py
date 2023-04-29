# Create a function that will 3 parameters for the first number and second number and operation
def calculator(num1, num2, opp):
    # If they enter '+', then the program should add 2 numbers that were entered and return the result
    if opp == '+':
        return num1 + num2
    if opp == '-':
        return num1 - num2
    if opp == '*':
        return num1 * num2
    if opp == '/':
        return num1 / num2



# b. Ask the user what arithmetic operations they would like to perform
resume = 'y'

# d. once the result is printed, ask the user if they would like to try again
while resume == 'y':
    num1 = int(input("Enter in your first number: "))
    num2 = int(input("Enter in your second number: "))
    opp = input("Enter in which operation you would like to perform.\n + for addition \n - for substraction \n * for multiplication\n / for division\n")
    answer = calculator(num1,num2,opp)
    print("Your answer is ",answer)
    resume = input("Would you like to continue? y or n: ")
    if resume == 'n':
        print("Have a great day!2")
