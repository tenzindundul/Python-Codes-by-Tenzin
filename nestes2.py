nums=[[10,20],[30,40],[50,60]]
k=0
average_marks= []
sum=0

while k<len(nums):
    sum=sum+nums[k][0]+nums[k][1]
    avg=sum/len(nums)
    average_marks.append(avg)
    k+=1
print("The average of the list is",average_marks)