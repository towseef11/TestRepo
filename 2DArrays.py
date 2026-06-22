arr  = [[10,20,30]
       ,[40,50,60]
       ,[70,80,90]]
print(arr[1][1])
print(arr[2][2])

for rows in arr:
    for num in rows:
        print(num, end=" ")
    print()    