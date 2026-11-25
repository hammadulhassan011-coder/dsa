# Find the factors of a Number n 
# Better solution 
n=10
num=n
result=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)