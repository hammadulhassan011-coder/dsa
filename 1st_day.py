#Finding the number of the digits 
#This is the code which I wrote with my own brain stroming before watching the video on the youtube It is written just from watching tittle 
n=9834580853408
i=10
count=0
while True:
    reminder=n%i
    i=i*10
    count+=1
    if reminder==n:
        break
print(f"the number of digits is {count}")