n = int(input())
rev = 0
temp = n
while(n>0):
    rem = n % 10
    rev = rev*10 + rem 
    n = n//10
if(rev == temp):
    print("Palindrome")
else : 
    print("Not palindrome")        