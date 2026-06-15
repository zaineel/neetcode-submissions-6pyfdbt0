/*
1. scan each cell
2. as soon i hit '1'-> land
 a. do dfs to calculate the max area of that island
 b. max_area varaible is responsible to help me get maximum area seen \
 so far
3. return max_area from main loop 
*/
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int max_area = 0;
        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                if (grid[row][col] == 1){
                    int area = dfs(grid, row, col);
                    max_area = Math.max(max_area, area);
                    
                }
            }
        }

        return max_area;
    }

    private int dfs(int[][] grid, int row, int col){
        int rows = grid.length;
        int cols = grid[0].length;

        // base case
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] != 1){
            return 0;
        }
        grid[row][col] = 0; // mark the cell as visited
        return 1 + dfs(grid, row + 1, col) 
                 + dfs(grid, row - 1, col)
                 + dfs(grid, row, col + 1)
                 + dfs(grid, row, col - 1);
    }
}
