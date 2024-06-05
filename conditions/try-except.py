
# number = input("Enter a number: ")
# multi = int(number) * 2
# print("Total is:", multi)

# # the code below does the same thing as that above, but it tries to prevent syntax error using try and except
# # we use "try" on the decision line in the code so that if there an input typo, "except will be executed"
# # we surround the dangerous section of the code with TRY and EXCEPT
# number = input("Enter a number: ")
# try:
#     multi = int(number) * 2
#     print("Total is:", multi)
# except:
#     print("Something went wrong!")
# print("Please try again")

# using while loop with TRY and EXCEPT
while True:
    number = input("Enter a number: ")
    try:
        multi = int(number) * 2
        print("Total is:", multi)
        break #breaks out of the loop
    except:
        print(number + " is not a number!")
        continue #makes the loop to start again
