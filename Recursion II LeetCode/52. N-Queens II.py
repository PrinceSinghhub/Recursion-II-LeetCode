class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        p_diag = set()
        n_diag = set()

        count = 0
        res = []

        def valid_sol(r):
            nonlocal count
            # Base case

            if r == n:
                count += 1

            for c in range(n):

                if c in cols or c + r in p_diag or c - r in n_diag:
                    continue


                else:

                    cols.add(c)
                    p_diag.add(c + r)
                    n_diag.add(c - r)

                    valid_sol(r + 1)  # Recurrsive call for next row

                    cols.remove(c)
                    p_diag.remove(c + r)
                    n_diag.remove(c - r)

        valid_sol(0)
        return count

ans = Solution()
n = 4
print(ans.totalNQueens(n))