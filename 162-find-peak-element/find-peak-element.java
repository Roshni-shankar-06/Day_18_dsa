class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // If mid is less than its right neighbor, the peak lies to the right
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
        
