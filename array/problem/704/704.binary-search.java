/*
 * @lc app=leetcode id=704 lang=java
 *
 * [704] Binary Search
 */

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        if(target < nums[0] || target > nums[nums.length -1]) return -1;
        int left = 0;
        int right = nums.length -1;
        while(left <= right) {
            int mid = left + ((right -left) >> 1);
            if(nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
// @lc code=end

