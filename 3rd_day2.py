# Print all the factorial of number n
n=33
result=[]
num=n
for i in range (1,num+1):
    if (num%i==0):
        result.append(i)

print(result)    

