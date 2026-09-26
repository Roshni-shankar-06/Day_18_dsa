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
        # The width of each bucket is t + 1
        width = t + 1
        
        for i, num in enumerate(nums):
            # In Python 2, integer division handles rounding towards negative infinity 
            # naturally for positive integers. For negative numbers, floor division 
            # '//' functions consistently across versions.
            bucket_id = num // width
            
            # Scenario 1: Two numbers fall into the absolute same bucket
            if bucket_id in buckets:
                return True
                
            # Scenario 2: Check the left adjacent bucket
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= t:
                return True
                
            # Scenario 3: Check the right adjacent bucket
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= t:
                return True
                
            # Place the current number into its corresponding bucket
            buckets[bucket_id] = num
            
            # Maintain the sliding window size of k
            if i >= k:
                old_bucket_id = nums[i - k] // width
                del buckets[old_bucket_id]
                
        return False
          
