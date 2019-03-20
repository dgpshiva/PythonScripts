class JobExpiry():
    def __init__(self, unexpiredJobs):
        self.unexpiredJobs = unexpiredJobs
    

    def isExpired(self, jobID):

        leftExtreme = int(self.unexpiredJobs[0].split("-")[0]) if "-" in self.unexpiredJobs[0] else int(self.unexpiredJobs[0])
        if jobID < leftExtreme:
            return True
        
        rightExtremeIndex = len(self.unexpiredJobs)-1
        rightExtreme = int(self.unexpiredJobs[rightExtremeIndex].split("-")[1]) if "-" in self.unexpiredJobs[rightExtremeIndex] else int(self.unexpiredJobs[rightExtremeIndex])
        if jobID > rightExtreme:
            return True
        
        i = 0
        j = rightExtremeIndex

        while i<=j:
            mid = (i+j)//2

            if "-" not in self.unexpiredJobs[mid]:
                if jobID == int(self.unexpiredJobs[mid]):
                    return False
                if jobID < int(self.unexpiredJobs[mid]):
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                leftValue = int(self.unexpiredJobs[mid].split("-")[0])
                rightValue = int(self.unexpiredJobs[mid].split("-")[1])
                if jobID >= leftValue and jobID <= rightValue:
                    return False
                if jobID < leftValue:
                    j = mid - 1
                else:
                    i = mid + 1
            
        return True



if __name__ == '__main__':
    j = JobExpiry(["2", "100-150", "199", "200-210", "215", "300-350"])
    # print j.isExpired(3)
    # print j.isExpired(101)
    print j.isExpired(355)
