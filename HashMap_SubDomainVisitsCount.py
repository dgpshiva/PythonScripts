class Solution(object):
    def __init__(self):
        self.domainCounts = {}

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        for countDomain in cpdomains:
            count = int(countDomain.split(' ')[0])
            domain = countDomain.split(' ')[1]
            domainParts = domain.split('.')
            if len(domainParts) > 0:
                subdomain = domainParts[-1]
                self.insertIntoDict(subdomain, count)
            if len(domainParts) > 1:
                subdomain = '.'.join(domainParts[-2:])
                self.insertIntoDict(subdomain, count)
            if len(domainParts) > 2:
                subdomain = '.'.join(domainParts[-3:])
                self.insertIntoDict(subdomain, count)

        output = []
        for key, val in self.domainCounts.items():
            output.append(str(val) + " " + key)

        return output

    def insertIntoDict(self, subdomain, count):
        if subdomain not in self.domainCounts:
            self.domainCounts[subdomain] = count
        else:
            self.domainCounts[subdomain] += count



if __name__ == '__main__':
    s = Solution()
    print s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
