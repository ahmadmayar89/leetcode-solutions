nums=[0,0,1,1,1,2,2,3,3,4,5,6,6,6,7,7,7]
def remove_duplicates(nums):
    if not nums:
        return 0
    
    j = 0  # Initialize the 'unique' end at the first index
    
    for i in range(1, len(nums)):  # Start checking from the second element
        if nums[i] != nums[j]:  # If a unique element is found
            j += 1  # Move the unique index up
            nums[j] = nums[i]  # Set the unique element at index j
            
    return j + 1  # Return the number of unique elements

print(remove_duplicates(nums))