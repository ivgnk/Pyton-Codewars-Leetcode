'''
3079. Find the Sum of Encrypted Integers
https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
'''
def sumOfEncryptedInt(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ssum=0
        # print(nums)
        for i in nums:
            if i<10:
                ssum=ssum+i
            else:
                s=str(i); llen = len(s)
                ll = [int(ss) for ss in s]
                # print(ll)
                mmax= max(ll)
                # print(mmax,type(mmax))
                sn1 = [str(mmax)]*llen
                sn = ''.join(sn1)
                ssum=ssum+int(sn)
        # print('ssum=',ssum)
        return ssum
