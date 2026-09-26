class Solution {
    public int maximumGap(int[] nums) {
        if (nums == null || nums.length < 2) {
            return 0;
        }

        int min = nums[0];
        int max = nums[0];
        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        // Minimum possible gap for the buckets
        int bucketSize = Math.max(1, (max - min) / (nums.length - 1));
        int bucketCount = (max - min) / bucketSize + 1;

        int[] minBucket = new int[bucketCount];
        int[] maxBucket = new int[bucketCount];
        java.util.Arrays.fill(minBucket, Integer.MAX_VALUE);
        java.util.Arrays.fill(maxBucket, Integer.MIN_VALUE);

        // Distribute numbers into buckets
     
