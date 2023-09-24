class Solution(object):
    def containsDuplicate(self, nums):
        help_set = set()

        for i in nums:
            if i in help_set:
                return True
 
            help_set.add(i)
            
        return False