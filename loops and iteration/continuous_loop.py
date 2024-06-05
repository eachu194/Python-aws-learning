# # the code will run until the entered is 5 i.e...
# # when time is 5, break out of the loop
# while True:
#     line = input('What time is it? ')
#     if line[0] == "5":
#         print("your line contains 5")
#         continue #this line keeps you in the loop, ie if your line starts with , the loop will continue
#     if line == "done":
#         break # this line means that if your line starts with done, it breaks out ot the loop
#     print(line)
# print('Done!')

n = 5
while n > 0:
    line = input('What time is it? ')
    print(n)
    if line[0] == "5":
        print("your line contains 5")
        continue #this line keeps you in the loop, ie if your line starts with , the loop will continue
    if line == "done":
        break # this line means that if your line starts with done, it breaks out ot the loop
    print(line)
    n = n - 1 # the time will decrease by 1 if your answer don't start with 5 but
              # once it starts with 5, it will not decrease.
print('Done!')