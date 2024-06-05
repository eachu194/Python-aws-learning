# the code below makes a decision inside a decision. if the first if condition is false, then the second if condition will not execute
# take for example we want to list s3 buckets.
# we can make a condition if the bucket is in us-east-1, list the bucket, we can futher say if the bucket in us-east-1 
#  encrypted, list it, else drop it.
x = 40
if x > 1:
    print('greater 1')
    if x < 100:
        print('Less than 100')
print("All done!")