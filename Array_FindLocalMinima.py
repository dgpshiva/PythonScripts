class Solution:
    def __init__(self):
        self.localMinima = None

    def binarySearch(self, arr):
        mid = len(arr)//2
        if (mid==0 or arr[mid]<arr[mid-1]) and (mid==len(arr)-1 or arr[mid]<arr[mid+1]):
            self.localMinima = arr[mid]
            return True
        
        if mid > 0 and arr[mid-1] < arr[mid]:
            return self.binarySearch(arr[0:mid])

        if mid < len(arr)-1 and arr[mid+1] < arr[mid]:
            return self.binarySearch(arr[mid+1:len(arr)])

        return False


if __name__ == '__main__':
    s = Solution()
    print s.binarySearch([9, 6, 3, 14, 5, 7, 4])
    print s.localMinima
        