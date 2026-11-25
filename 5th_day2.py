# Count freequncy distribution in the list and store in the dictionary 
l=[2,3,4,2,3,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
f={}
for i in range(0,len(l)):
    if l[i] in f:
        f[l[i]]+=1
    else:
        f[l[i]]=1
