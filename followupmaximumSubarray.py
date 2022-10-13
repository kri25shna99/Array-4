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
        start = 0
        end = 0
        #pointer for start index 
        currStart =0
        for i in range(1,len(nums)):
            if nums[i] >currSum+nums[i]:
                currStart =i
                currSum = nums[i]
            else:
                currSum = currSum + nums[i]
            if currSum>maximum:
                maximum = currSum
                #resetting the start and end pointer
                start = currStart
                end = i
        #followup
        print("startindex :", start)
        print("endindex :", end)
        return maximum
