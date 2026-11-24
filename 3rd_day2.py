# Print all the factors of number n
# Extreme brute force method 
n=33
result=[]
num=n
for i in range (1,num+1):
    if (num%i==0):
        result.append(i)

print(result)    

