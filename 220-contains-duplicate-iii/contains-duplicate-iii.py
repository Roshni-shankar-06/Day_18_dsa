class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Edge cases: t cannot be negative, k must be positive
        if t < 0 or k <= 0:
            return False
            
        buckets = {}
       
            
        
          
