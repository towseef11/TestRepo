arr = [1,1,2,2,2,3,4,4,5]
pos = 1
for i in range (1,len(arr)):
    if(arr[i] != arr[i-1]):
        arr[pos] = arr[i]
        pos+=1
print(arr[0:pos])        