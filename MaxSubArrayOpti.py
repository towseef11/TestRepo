arr = [3,-4,5,4,-1,7,-8]

curmax = 0
MaxSubArray = 0

for a in arr:
    curmax += a
    MaxSubArray = max(curmax,MaxSubArray)
    if(curmax < 0):
        curmax = 0
print(MaxSubArray)        