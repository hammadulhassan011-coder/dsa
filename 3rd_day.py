# Armstrong Number or not 

n=153
num=n
nod=len(str(n))
result=0
while num>0:
    ld=num%10
    result=result+(ld**nod)
    print(result)
    num=num//10
if result==n:
    print("Armstrong Number")
else:
    print("Not")
