nums=[[10,20],[30,40],[50,60]]


k=0
sum=0
for x in range(len(nums)):
    sum=sum+nums[x][0]
average_marks=sum/len(nums)
print(average_marks)
