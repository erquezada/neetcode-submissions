class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Given an integer array nums, return true if any value appears more 
        Than once in the array, otherwise return false.
        '''
        my_set = set() # create a set (a set cannot have anny duplicates)
        for i in nums: # iterate through array
            my_set.add(i) # place the values of the array into set
        if len(nums) != len(my_set): 
            return True
        else: 
            return False