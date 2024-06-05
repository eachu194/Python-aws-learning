# cabinate = dict() # Initialize an empty dictionary named 'cabinate'
# cabinate ["Fall"] =109 # Add a key-value pair to the dictionary: key "Fall" with value 109
# cabinate ['Winter'] = 102
# cabinate["style"] = " summer"
# cabinate ["Summer"] = 105
# cabinate["Students"] = "names"
# cabinate ["Spring"] = 107
# print(cabinate) # Print the entire dictionary 'cabinate'
# print(cabinate["Fall"]) # Print the value associated with the key "Fall" in the dictionary
# cabinate["Fall"] = cabinate["Fall"] + 5 # Update the value associated with the key "Fall" by adding 5 to the current value
# print(cabinate["Fall"]) # Print the updated value associated with the key "Fall" in the dictionary
#------------------------------------------------------------------------------------ 

# this block of code (resources) will not execute
# {
#     "Results":[
#         {
#             "studentNumber": 100,
#             "tutors": 5,
#             "classes": 4,
#             "courses": 15,
#             "passed": 98,
#             "failed": 2,
#             "passedGrade":{
#                 "A grade": 25,
#                 "B grade": 35,
#                 "c grade": 38
#             },
#             "failedGrade":{
#                 "D grade": 2
#             }
#         }
#     ]
# }
# print("Resouces")
#---------------------------------------------------------------

#similar to list, when you want to change the value of a key, just call the name of that key and replace the value, see the value of age below
# Random = dict()
# Random["age"] = 44
# Random["course"] = 192
# print(Random)
# Random["age"] = 28
# print(Random)
#----------------------------------------------------------------------


# in list, is you want to change the value of any key, you have to append the new value to the key by using the index of the key. see below
lst = list()
lst.append(21)
lst.append(281)
lst[0] = 44
print(lst)
#---------------------------------------------------------------------------