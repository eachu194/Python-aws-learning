# while True:
#     hours_worked = float(input("Enter the hours worked: "))
#     rate = float(input("Enter the rate per hour: "))
#     try:
#         if hours_worked > 40:
#             overtime_hours = hours_worked - 40
#             overtime_rate = 1.5 * rate
#             overtime_pay = overtime_hours * overtime_rate
#             print("Overtime pay $", overtime_pay)
#             regular_pay = 40 * rate
#             pay = regular_pay + overtime_pay
#             print("Pay: $"+str(pay) )# str converts pay variable to a string. concatenation of strings with non-string types directly would raise an error
#         else:
#             pay = hours_worked * rate
#             print("Pay: $"+str(pay))
#             break
#     except:
#         print(hours_worked + "is not a number")
#         continue



while True: # creates a loop that runs indefinitely
    try:
        hours_worked = float(input("Enter the hours worked: "))
        rate = float(input("Enter the rate per hour: "))
    
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            overtime_rate = 1.5 * rate # Calculate the overtime rate as 1.5 times the regular rate
            overtime_pay = overtime_hours * overtime_rate
            print("Overtime pay $", overtime_pay)
            regular_pay = 40 * rate
            pay = regular_pay + overtime_pay
            print("Pay: $" + str(pay) )# str converts pay variable to a string. concatenation of strings with non-string types directly would raise an error
        else:
            pay = hours_worked * rate
            pay = round(pay, 2) # Round the total pay to 2 decimal places
            print("Pay: $" + str(pay))
            break # Exit the loop after successful calculation
    except ValueError:
        print("Invalid input, plaese enter numeric values.") # Handle invalid input (non-numeric values)
        continue

