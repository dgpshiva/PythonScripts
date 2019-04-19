# Given collection of intervals, merge overlapping intervals
# Egs:
    # print s.merge([[1,3],[2,6],[8,10],[15,18]])   Expected output: [[1,6], [8,10], [15,18]]]
    # print s.merge([[1,4], [1,4]])                 Expected output: [[1,4]]
    # print s.merge([[1,4], [0,4]])                 Expected output: [[0,4]]
    # print s.merge([[1,4], [2,3]])                 Expected output: [[1,4]]
    # print s.merge([[1,4],[0,2],[3,5]])              Expected output: [[0,5]]

# O(nlog(n)) time
# O(n) space
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        if len(intervals) == 0:
            return output
        intervals.sort(key=lambda x: x[0])
        output.append(intervals[0])
        j = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            overlap = False
            contained = False
            if interval[0] >= output[i-j][0] and interval[0] <= output[i-j][1] and interval[1] >= output[i-j][1]:
                overlap = True
                intervalStart = output[i-j][0]
                intervalEnd = interval[1]
            elif interval[0] >= output[i-j][0] and interval[1] <= output[i-j][1]:
                contained = True
                intervalStart = output[i-j][0]
                intervalEnd = output[i-j][1]
            elif interval[0] <= output[i-j][0] and interval[1] >= output[i-j][0] and interval[1] <= output[i-j][1]:
                overlap = True
                intervalStart = interval[0]
                intervalEnd = output[i-j][1]
            elif interval[0] <= output[i-j][0] and interval[1] >= output[i-j][1]:
                contained = True
                intervalStart = interval[0]
                intervalEnd = interval[1]
                
            if overlap or contained:
                output[i-j] = [intervalStart, intervalEnd]
                j += 1
            else:
                output.append(interval)
        
        return output



# O(1) space:
# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if len(intervals) == 0:
#             return intervals
#         intervals.sort(key=lambda x: x[0])
#         j = 1
#         tail = 0
#         for i in range(1, len(intervals)):
#             interval = intervals[i]
#             overlap = False
#             contained = False
#             if interval[0] >= intervals[i-j][0] and interval[0] <= intervals[i-j][1] and interval[1] >= intervals[i-j][1]:
#                 overlap = True
#                 intervalStart = intervals[i-j][0]
#                 intervalEnd = interval[1]
#             elif interval[0] >= intervals[i-j][0] and interval[1] <= intervals[i-j][1]:
#                 contained = True
#                 intervalStart = intervals[i-j][0]
#                 intervalEnd = intervals[i-j][1]
#             elif interval[0] <= intervals[i-j][0] and interval[1] >= intervals[i-j][0] and interval[1] <= intervals[i-j][1]:
#                 overlap = True
#                 intervalStart = interval[0]
#                 intervalEnd = intervals[i-j][1]
#             elif interval[0] <= intervals[i-j][0] and interval[1] >= intervals[i-j][1]:
#                 contained = True
#                 intervalStart = interval[0]
#                 intervalEnd = interval[1]
                
#             if overlap or contained:
#                 intervals[i-j] = [intervalStart, intervalEnd]
#                 tail = i-j
#                 j += 1
#                 intervals[i] = None
#             else:
#                 intervals[i-j+1] = interval
#                 tail = i-j+1
            
#         return intervals[0:tail+1]


if __name__ == '__main__':
    s = Solution()
    print s.merge([[1,3],[2,6],[8,10],[15,18]])
    print s.merge([[1,4], [1,4]])
    print s.merge([[1,4], [0,4]])
    print s.merge([[1,4], [2,3]])
    print s.merge([[1,4],[0,2],[3,5]])
    
