from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length=len(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for first in range(length):
            third=length-1
            for second in range(first+1,length):
                    while nums[first]+nums[second]+nums[third]>target and second<third:
                           if abs(nums[first]+nums[second]+nums[third]-target)<abs(result-target):
                               result=nums[first]+nums[second]+nums[third]
                           third-=1
                    if nums[first]+nums[second]+nums[third]<target and second<third:
                           if abs(nums[first]+nums[second]+nums[third]-target)<abs(result-target):
                               result=nums[first]+nums[second]+nums[third]
                    if second==third:
                        break
                    if nums[first]+nums[second]+nums[third]== target:
                        result=target
                        return result

        return result


test=Solution()
print(test.threeSumClosest([1,1,1,0],100))

