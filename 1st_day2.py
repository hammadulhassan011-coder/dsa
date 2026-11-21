#extract the digits of a number and then count 
n=2432
num=n
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
    