# Hash Maping 
# compare these two lists and find how many times the elements from the m extist in the n list 

n=[3,2,2,3,2,1,1,2,5,3,4,8,6,5,6,10]
m=[3,1,2,5,77,8,90]
hash_map=dict()
for i in n:
    hash_map[i]=hash_map.get(i,0)+1
for j in m:
    print(f"{j} is {hash_map.get(j,0)} times in n")
