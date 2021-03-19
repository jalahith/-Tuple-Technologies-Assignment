public class SoldierProblem {
    static int N = 4;

    void printSolution(int board[][])
    {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                System.out.print(" " + board[i][j] + " ");
            System.out.println();
        }
    }

    boolean isSafe(int board[][], int row, int col)
    {
        int i, j;

        /* Check this row on left side */
        for (i = 0; i < col; i++)
            if (board[row][i] == 1)
                return false;

        /* Check upper diagonal on left side */
        for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1)
                return false;

        /* Check lower diagonal on left side */
        for (i = row, j = col; j >= 0 && i < N; i++, j--)
            if (board[i][j] == 1)
                return false;

        return true;
    }

    boolean solveNSoliderUtil(int board[][], int col)
    { 

        if (col >= N)
            return true; 

        for (int i = 0; i < N; i++) { 
            /* Check if the soldier can be placed on
               board[i][col] */
            if (isSafe(board, i, col)) {
                board[i][col] = 1;
                if (solveNSoliderUtil(board, col + 1) == true)
                    return true;
                board[i][col] = 0; // BACKTRACK 
            }
        }
        return false;
    }


    boolean solveNSoldier()
    {
        int[][] board = new int[N][N];
        for(int i = 0; i<N ;i++){
            for(int j = 0; j<N ;j++){
                board[i][j]=0;
            }
        }
        if (!solveNSoliderUtil(board, 0)) {
            System.out.print("Solution does not exist");
            return false;
        }

        printSolution(board);
        return true;
    }

    // main driver function
    public static void main(String args[])
    {
        SoldierProblem problem = new SoldierProblem();
        // Provide your input here
        N = 8;
        problem.solveNSoldier();
    }
}