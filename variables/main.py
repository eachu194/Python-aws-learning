# line 3 below converts the string value "123" in line one to an integer 
# stud = '123'
# dents = int(stud) + 1
# print(dents)

# line 8 below converts the integer value 44 in line 7 to a string
# dems = 44
# repu = str(dems) + " " "are years old"
# print(repu)

# the code below uses the input function
# nam = input("who are you? ")
# print("welcome", nam + "!")

#converting user input
# inp = input("rent apart?")
# usri = int(inp) + 1
# print("rent home", usri)

# inp = input('European floor?')
# usf = int(inp) + 1
# print('US floor', usf)

# # the code below uses the input function
# hour_worked = input("Enter hours work: ")
# pay_rate = input("Enter the rate per hour: ")
# pay = int(hour_worked) * float(pay_rate)
# print("Your gross pay is", pay)

# # line 31 to 34 does the same thing as line 25 to 29, but it's more efficient b/c if user enter wrong data type, the code breaks right on that line.
# hour = float(input("Enter hours work: "))
# rate = float(input("Enter the rate per hour: "))
# pay = (hour) * (rate)
# print("Your gross pay is", pay)

# line 37 to 42 does the same thing as line 31 to 34
hour = input("Enter hours work: ")
hour = float(hour)
rate = input("Enter the rate per hour: ")
rate = float(rate)
pay = hour * rate
print(type(pay))
print("Your gross pay is", pay)