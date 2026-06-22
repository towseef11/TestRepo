num = [2,5,2,11,66,3]
maximum = num[0]
minimum = num[0]
for n in num :
    if(n > maximum):
        maximum = n
    if(n < minimum):
        minimum = n
print(f"Maximum : {maximum}")   
print(f"Minimum : {minimum}")      
