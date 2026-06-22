nums = [10,20,30,20,40,20,50]
print(30 in nums)
print(nums.index(40))

count = 0
for num in nums :
    if(num == 20):
      count+=1

print(count)      