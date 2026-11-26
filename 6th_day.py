# Hashing in pyhton
# BruteForce solution
# We have to find how much time a digit from n exits in the list n 


m=[4,5,6,3,2,10,3,4,3,6,6]
n=[4,66,33,7,3,6]

for i in n:
    count=0
    for j in m:
        if i==j:
            count+=1
    print(f"{i} is {count} times")

