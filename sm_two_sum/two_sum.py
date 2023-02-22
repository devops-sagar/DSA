class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        result = {}
        for index, value in enumerate(nums):
            if (target - value) in result:
                return [result[target - value], index]
            else:
                result[value] = index