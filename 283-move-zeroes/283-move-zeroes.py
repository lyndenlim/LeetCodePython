class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for element in range(len(nums)):
              if nums[element] == 0: 
                nums.append(nums[element])
                nums.remove(nums[element])
