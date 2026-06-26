class Solution {
    private Map<String, Integer> memo = new HashMap<>();
    public int findTargetSumWays(int[] nums, int target) {
        return backTrack(nums, target, 0, 0);
    }
    private int backTrack(int[] nums, int target, int index, int currSum){
        String key = index + "," + currSum;
        if (memo.containsKey(key)){
            return memo.get(key);
        }
        if (index == nums.length){
            return currSum == target ? 1 : 0;
        }
        int add = backTrack(nums, target, index + 1, currSum + nums[index]);
        int subtrack = backTrack(nums, target, index + 1, currSum - nums[index]);
        memo.put(key, add + subtrack);
        return memo.get(key);
    }
}
