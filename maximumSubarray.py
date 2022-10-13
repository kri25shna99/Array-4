#Youtube- https://www.youtube.com/watch?v=DxAwNHH8s5s&ab_channel=%7BS30%7D
#time - O(n)
#Space - O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #null condition
        if len(nums)==0:
            return -math.inf
        if len(nums)==1:
            return nums[0]
        #consdering running sum senerio
        """
        currsum max
        -2      -2
        1       1
        -2      1
        4       4
        3       4
        5       5
        6       6
        1       6
        5       6
        """
        maximum = nums[0]
        currSum = nums[0]
        for i in range(1,len(nums)):
            currSum = max(nums[i], currSum+nums[i])
            maximum = max(currSum,maximum)
        return maximum
