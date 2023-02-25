class Solution1:
    def searchMatrix(self, matrix, target):

        for i in matrix:

            if target in i:
                return True

        return False



class Solution:
    def check(self, matrix, target):

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if matrix[mid] > target:
                end = mid - 1
            if matrix[mid] < target:
                start = mid + 1

            if matrix[mid] == target:
                return True
        return False

    def searchMatrix(self, matrix, target):

        for i in matrix:
            ans = self.check(i, target)
            if ans == True:
                return True
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
ans = Solution()
print(ans.searchMatrix(matrix,target))