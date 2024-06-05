while True:
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
        break
    except ValueError:
        print("Error, please a enter a numeric value to continue")
        continue