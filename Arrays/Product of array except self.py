def productExceptSelf(nums):
    length = len(nums)
    # Initialize prefix and suffix arrays
    prefix = [1] * length
    suffix = [1] * length
    output = [1] * length

    # Calculate prefix products
    for i in range(1, length):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Calculate suffix products
    for i in range(length - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Calculate the result by multiplying prefix and suffix
    for i in range(length):
        output[i] = prefix[i] * suffix[i]

    return output

# Test the function with an example
print(productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]