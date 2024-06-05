#the code below creates a dictionary and initiates a list. the for loop will check if a each name is
# in the dictionary, and if the name is not in the dict, it will palce it in the dict and count it as 1
# count but is the name is in the dict, increase the value by 1
# counts = dict()
# names = ["James", "Matt", "Jean", "Jean", "Matt"]
# for name in names: # Iterate over each name in the 'names' list
#     if name not in counts: # If the name is not already in the 'counts' dictionary
#         counts[name] = 1   # Add the name to the dictionary with a count of 1 if name not in the dictionary
#     else:
#         counts[name] = counts[name] + 1 # If the name is already in the dictionary, increment its count by 1
# # print(counts) # Print the final counts of each name in the dictionary
# another_name = counts.get("Eric", 0) # this line tries to get a value we are not sure it exist using the .get() method 
#                                      #if the name isn't there, it will assign a default value 0 (could be int or str) to the name(key)
#                                      #even if the name is in the dict, it will not use the default value
# print(counts["James"])
# print(another_name)
#--------------------------------------------------------------------------------

counts = dict()
names = ["James", "Matt", "Jean", "Jean", "Matt"]
for name in names: 
    if name not in counts:
        counts[name] = 1 
    else:
        counts[name] = counts[name] + 1
# for key in counts:
#     print(key, counts[key])
# print(counts)

#the first 2 lines below will get a list of the keys(names) in the dict
name_list = list(counts)
name_list = list(counts.keys()) # this will return a normal list of keys
name_list = counts.keys() # this will return a dict of keys
name_list = counts.values() # this return a dict of values
name_list = list(counts.items()) # this will return a tuple of the dict (keys and values)
name_list = (counts.items()) # this will return a dict of items in the dict
print(name_list)