#count the number of digits using the loop approch 
n=67868
num=n
count=0
while num>0:
    num=num//10
    count=count+1
print(f"The number of  digits are {count}")

