# Find the factors of the Number n 
# Optimal solution
from math import sqrt
n=36
num=n
result=[]
for i in range(1,int(sqrt(num))):
    if num%i==0:
        result.append(i)
        result.append(int(num//i))
result.sort()
print(result)