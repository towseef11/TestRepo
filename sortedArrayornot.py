num = [1,2,3,2,5,7]
sorted = True

for i in range(0,len(num)-1):
    if(num[i]>num[i+1]):
        sorted = False
if(sorted):
    print("Sorted")
else : 
    print("Not sorted")            