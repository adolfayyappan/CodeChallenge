class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ordnum = []
        nm = list(s)
        ordnum.append(''.join(nm))
        for i in range(0, len(nm) - 1 ):
            if (int(nm[i]) % 2) == (int(nm[i+1]) % 2):
                if int(nm[i]) > int(nm[i+1]):
                    x = nm[i]
                    nm[i] = nm[i+1]
                    nm[i+1] = x
                    ordnum.append(''.join(nm))
                    break

        # print(sorted(ordnum)[0])
        return sorted(ordnum)[0]


#ob = Solution()
#print(ob.getSmallestString('45320'))
