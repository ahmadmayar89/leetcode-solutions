class Solution:
    def has_duplicate(self, nums):
        if len(set(nums)) < len(nums):
            print("Duplicates found!")
            return True
        else:
            print("No duplicates found!")
            return False


nums = [1, 2, 3, 3]
sol = Solution()
sol.has_duplicate(nums)  
