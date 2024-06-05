# # This code will print "w" because 'w' has the highest Unicode (ASCII) value among all the characters in the string "hello world".
# # The max function in Python, when applied to a string, returns the maximum character based on the Unicode (ASCII) values of the characters
# big = max("hello world")
# print(type(big))
# print(big)



# def greetings(): # Define a function named 'greetings' with no argument and no parameters
#     print("greetings") # Print the string "greetings" to the console

# greetings() # Call the 'greetings' function to execute its code block


def greetings(n): # Define a function named 'greetings' with no argument and no parameters
    name = n # we can as well remove this line and replace "n" in the () which makes it a variable and it will work same.

    #print("greetings,", name + "!") # Print the string "greetings" to the console
    # usrinp = input(str("Enter your name: "))
    # print("Greetings " + usrinp + "!")

# we could uncomment the above 3 lines and comment out the next 2 lines and but we'll get an error b/c needs to be defined out of the indentation
usrinp = input(str("Enter your name: "))
print("Greetings " + usrinp + "!")
greetings(usrinp + "!") # Call the 'greetings' function to execute its code block
#in the code block above, if we don't want user input, we can uncomment usrinp and line after, and uncomment line after 'name = n'. 
#remove everything in the () on last line in the code block and run it 





