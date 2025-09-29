def moveZeroes(nums):
    # Step 1: Initialize the last non-zero index
    last_non_zero_found_at = 0

    # Step 2: Traverse the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Step 3: Swap the elements
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            # Step 4: Move the non-zero index forward
            last_non_zero_found_at += 1

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  