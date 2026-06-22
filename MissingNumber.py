arr = [1,2,3,5,6]
max = arr[0]
for a in arr:
    if(a>max):
        max =a

overall = max*(max +1)/2
summ = 0

for a in arr:
    summ+=a

print(int(overall - summ))