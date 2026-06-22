num = [2,3,1,6,5,3,7]
maximum = 0
secmax = 0
for n in num :
    if(n>maximum):
        secmax = maximum
        maximum = n
    elif(n != maximum and n > secmax):
        secmax = n
print(secmax)        
