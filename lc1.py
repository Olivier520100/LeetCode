class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        j = 0
        lastindex = len(nums)
        k = target - nums[i]

        while (i<lastindex):

            if i==j:
                j+=1

            if k == nums[j]:
                result = [i,j]
                i = lastindex
                return result

            j+=1
            if j == lastindex:

                i+=1
                j=i
                k = target - nums[i]

