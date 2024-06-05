# x = input(("Enter a number: "))
# x = float(x)
# if x < 10:
#     print("smaller")
# if x > 10:
#     print("Bigger")
# print('Finis')

# # in the code form line 14 to 22, x is defined at a global scope and you print x from within the "if" scope or global scope but
# # y is define at the "if"(local) scope, that why when you print y outside the indentation you'll get a NameError message.
# # however, if the value assigned to x is equal to or greater than then "if" condition (local scope), then why will print outside the condition

# #Global scope
# x = 8
# y = 10
# if x > 10 :
#     y = 8
#     print('X is greater than 9')
#     print(x)
#     print('the value of y is: ', y)
# print(x)
# print(y)

x = 5
if x > 2:
    print("X is greater than 2")
for number in range(5):
    print(number)
    if number > 2:
        print(str(number) + " is greater than 2") # we use str to elevate number to string and perform conatination
print("All done!")