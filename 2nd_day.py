# Check palindrome or not 

n=int(input("Enter a Number:"))
num=n
result=0
while num>0:
    last_digit=num%10
    print(last_digit)
    result=(result*10)+last_digit
    num=num//10
if result==n:
    print("Palindrome")
else:
    print("Not Palindrome")
