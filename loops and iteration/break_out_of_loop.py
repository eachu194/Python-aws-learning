# the code will run until the entered is 12:00 i.e...
# when time is 12:00, break out of the loop
while True:
    line = input('What time is it? ')
    if line == "12:00":
        break
    print(line)
print('Done!')