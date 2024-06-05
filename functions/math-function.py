# def maths(num_1, num_2): #maths performs all maths operations.
#     # Define a function named 'maths' that takes two parameters 'num_1' and 'num_2'
#     add = num_1 + num_2
#     # Add the two parameters and store the result in the variable 'add'
#     sub = num_1 - num_2
#     # Subtract the two parameters and store the result in the variable 'sub'
#     return add, sub
#     # Return the result of the maths

# result = maths(2, 3)
# # Call the 'maths' function with arguments 2 and 3, and store the result in the variable 'result'

# add1, sub1 = maths(23, 22)
# # Call the 'maths' function with arguments 23 and 22, and store the result in the variable 'add1 and sub1'

# print("Result:", result)
# # Print the string "Result:" followed by the value of 'result'

# print("add1:", add1)
# print("sub1:", sub1)
# # Print the string "add1 and sub1:" followed by the value of 'add1 and sub1' respectively



def computepay( hours, rate):
    if hours > 40: # from "if" till line before "else" calculates the overtime pay
        overtime_hours = hours - 40
        overtime_rate = 1.5 * rate
        overtime_pay = overtime_hours * overtime_rate
        print("Overtime: $", overtime_pay)
        regular_pay = 40 * rate
        pay = regular_pay + overtime_pay
        return pay
    else:
        pay = hours * rate
        return pay
try:
    rate = float(input("Enter the rate: "))
    hours = float(input("Enter the hours worked: "))
    pay = computepay(hours, rate)
    print(pay)
except ValueError:
    print("Error, you didn't enter a numeric value")

