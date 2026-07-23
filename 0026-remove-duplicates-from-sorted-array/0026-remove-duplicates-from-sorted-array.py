class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        ch = 0
        k = 1
        cm = 1

        while cm < len(nums):
            if nums[ch] == nums[cm]:
                cm += 1
            else:
                ch += 1
                nums[ch] = nums[cm]
                k += 1
                cm += 1

        return k