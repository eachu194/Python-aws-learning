# this is comparing stings, don't use in production
word = 'banana'
if word == "bananas":
    print("All right, bananas.")

if word < 'banana':
    print("Your word," + word + ', comes before banana.')
elif word > 'banana':
    print("Your word," + word + ', comes after banana.')
else:
    print("All bananas.")