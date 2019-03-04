class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sumEven = 0
        for val in A:
            if val%2 == 0:
                sumEven += val

        output = [None] * len(queries)

        for i in range(0, len(queries)):
            val = queries[i][0]
            index = queries[i][1]
            if index>=0 and index<len(A):
                if A[index]%2 == 0:
                    sumEven -= A[index]
            else:
                continue
            A[index] += val
            if A[index]%2 == 0:
                sumEven += A[index]
            output[i] = sumEven

        return output


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]

    s = Solution()
    print s.sumEvenAfterQueries(A, queries)
