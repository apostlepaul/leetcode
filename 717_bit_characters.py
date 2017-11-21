class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) <= 2:
            return bits[0] != 1
        if bits[-2] == 0:
            return True
        
        s = [False] * (len(bits))
        s[0] = (bits[0]==0)
        s[1] = not (bits[0]==0 and bits[1] ==1)
        for i in range(2, len(s)):
            if bits[i] == 1:
                if bits[i-1] == 1:
                    s[i] = s[i-2]
                else:
                    s[i] = False
            else:
                if bits[i-1] == 1:
                    s[i] = s[i-2] or s[i-1]
                if bits[i-1] == 0:
                    s[i] = s[i-1]
        
        return s[i-1] and not s[i-2]
