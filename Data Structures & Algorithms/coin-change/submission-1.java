// base case
// dp[i] -> min coins
// dp[i] = 0 -> return
// dp[0] = 0
// dp[amount]
// length = amount + 1
// dp[i] = min(dp[i], 1 + dp[i-coin])
// 12
// dp[0] = 0
// dp[1] = 1
// dp[2] = 2
// dp[3] = 3
// dp[4] = 4
// dp[5] = 1
//dp[10] = 1
// 
// dp[13]



class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++){
            for (int coin : coins){
                if(coin <= i){
                    dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
                }
            }
        }

        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
}
