n=[3,3,3,1,2,9,6,4,5,8,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,33,3,3,3,3,3]
f_map=dict()
for i in range(0,len(n)):
    f_map[n[i]]=f_map.get(n[i],0)+1

print(f_map[3])