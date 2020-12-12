#三数之和

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j = 0, len(nums) - 1
        if j < 2:
            return []
        nums.sort()
        m = []
        while i < len(nums):
            p = nums[i]
            if p > 0: break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            k = i + 1
            j = len(nums) - 1
            while k < j:
                n = nums[k]
                if nums[i] + nums[j] + nums[k] == 0:
                    m.append([nums[i], nums[k], nums[j]])
                    while k < j and nums[j] == nums[j - 1]:
                        j -= 1
                    while n == nums[k + 1] and k < j:
                        k += 1
                    K = k + 1
                    j = j - 1
                if nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                if nums[i] + nums[j] + nums[k] < 0:
                    k += 1
            i += 1
        return m
a=Solution()
print(a.threeSum( [0,0,-1,-1,-1,1,1,1,1,1]))


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans
