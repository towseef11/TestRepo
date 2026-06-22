arr = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray = 0
for i in range (len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        if(sum > maxSubArray):
            maxSubArray = sum
    print(sum)        
print(maxSubArray)            

       
