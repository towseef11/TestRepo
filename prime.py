print("Welcome")
n = int(input())
prime = True

if n < 2 :
    print("Not Prime")
else:
    for i in range(2, n):

        if(n % i == 0):
            prime = False
            break

if(prime): 
    print("Prime")
else:
    print("Not Prime")    
