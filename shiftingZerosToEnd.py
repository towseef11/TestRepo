arr = [1,0,2,0,3]
pos = 0
for i in range(0,len(arr)):
    if(arr[i] != 0 ):
        arr[pos] = arr[i]
        pos+=1
    
while(pos<len(arr)):
        arr[pos] = 0
        pos+=1    
print(arr)            