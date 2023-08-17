nums=[10,20,30,40,50,60]
k=0
item_found=False
while k<len(nums) and not item_found:
    if nums[k]==40:
        item_found=True
    else:
        k=k+1
if item_found:
    print("Item was found")
else:
    print("Item not found")