from collections import Counter

nums = [1,1,1,2,2,2,2,3,3,3,3,3,4,4]

def majorityElement(nums):
    counts = Counter(nums)
    # Find the element with the maximum count
    return max(counts, key=counts.get)

print(majorityElement(nums))
