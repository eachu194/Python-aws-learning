
# while True:
#     line = input('What time is it? ')
#     if line[0] == "5":
#         print("your line contains 5")
#         continue #this line keeps you in the loop, ie if your line starts with , the loop will continue
#     if line == "done":
#         break # this line means that if your line starts with done, it breaks out ot the loop
#     print(line)
# print('Done!')



#------------------------------------------------------------------
# num = [12, 32, 54, 232, 23]
# for n in num:
#     print(n)

#------------------------------------------------------------------
# names = ("Jude", "Sam", "google", "susan", "James")
# for name in names:
#     print(name)

#----------------------------------------------------------------------
# names = ("Jude", "Sam", "google", "susan")
# if "Ben" in names: 
#     print("Ben is in names")
# else:
#     print("Ben is not in names")

#--------------------------------------------------------------------------------------------------
# this is a tuple
# packages = ("noodles", "pear", "mesh", "milk", "vegetables", "peanut") # Define a tuple named 'packages' containing six elements
# if "peanut" in packages: # Check if the string "peanut" is an element in the tuple 'packages'
#     index = packages.index("peanut") # Get the index of the string "peanut" in the tuple 'packages'
#     print("I found peanut, peanut is at index:", index,) # Print the message with the index of "peanut"
# else:
#     print("Peanut is not in packages") # Print the message if "peanut" is not found in the tuple
#--------------------------------------------------------------------------------------------------------

# This code uses a for loop with the enumerate function to iterate over the elements of the tuple along with their indices.
# This code iterates through a tuple named packages to check if the item "paster" is present
packages = ("noodles", "Paster", "Pear", "oranges", "mango", "Apples") # Define a tuple named 'packages' containing six elements
found = False # Initialize a flag variable 'found' to False to track if "paster" is found
for index, item in enumerate(packages): # Iterate over the 'packages' tuple with both index and item using 'enumerate'
    if item == "Paster": # Check if the current item is "paster"
        print("I found paster, paster is at index:", index) # Print the message with the index of "peanut"
        found = True # Set the 'found' flag to True indicating "peanut" has been found
        break # Exit the loop as soon as "peanut" is found
if not found: # Check if the 'found' flag is still False after the loop
        print("Paster is not in packages") # Print the message indicating "peanut" was not found in the tuple
        
        

