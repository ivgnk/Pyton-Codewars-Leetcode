"""
Done 29.09.2024. Topics: Hash Table
432. All O`one Data Structure
https://leetcode.com/problems/all-oone-data-structure/description

Design a data structure to store the strings' count with the ability
to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.

inc(String key) Increments the count of the string key by 1.
If key does not exist in the data structure, insert it with count 1.

dec(String key) Decrements the count of the string key by 1.
If the count of key is 0 after the decrement, remove it from the data structure.
It is guaranteed that key exists in the data structure before the decrement.

getMaxKey() Returns one of the keys with the maximal count.
If no element exists, return an empty string "".

getMinKey() Returns one of the keys with the minimum count.
If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.


Example 1:
Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"


Constraints:
1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""


class AllOne:
    def __init__(self):
        self.d_s=dict()
        self.d_n=dict()
        self.mmax=-1
        self.mmin=10000000

    def inc(self, key: str) -> None:
        if key in self.d_s:
            n = self.d_s[key]+1
            self.d_s[key]=n
            self.mmax=max(self.mmax,n)
        else:
            n=1
            self.d_s[key] = n
            self.mmax = max(self.mmax,1)
            self.mmin = min(self.mmin,1)
        self.d_n[n]=key

    def dec(self, key: str) -> None:
        n=self.d_s[key]-1
        if n==0:
            del self.d_s[key]
        else:
            self.mmin=min(self.mmin,n)
        self.d_n[n]=key

    def getMaxKey(self) -> str:
        if self.mmax>0:
            return self.d_n[self.mmax]
        else: return ""

    def getMinKey(self) -> str:
        if self.mmin!=10000000:
            return self.d_n[self.mmin]
        else: return ""
    def pri(self)->None:
        ic(self.d_s)
        ic(self.d_n)

################################################################
# Runtime 7416 ms Beats 5.08%
# Memory  31.84 MB Beats 94.21%
class AllOne2:
    def __init__(self):
        self.d_s=dict()

    def inc(self, key: str) -> None:
        if key in self.d_s:
            n = self.d_s[key]+1
            self.d_s[key]=n
        else:
            n=1
            self.d_s[key] = n

    def dec(self, key: str) -> None:
        n=self.d_s[key]-1
        if n==0:
            del self.d_s[key]
        else:
            self.d_s[key]=n

    def getMaxKey(self) -> str:
        if len(self.d_s) !=0:
            vk= {v:k for k,v in self.d_s.items()}
            mmax=max(vk)
            return vk[mmax]
        else: return ""

    def getMinKey(self) -> str:
        if len(self.d_s) !=0:
            vk= {v:k for k,v in self.d_s.items()}
            mmin=min(vk)
            return vk[mmin]
        else: return ""

#########################################################
# Time Limit Exceeded - 15 / 19 testcases passed
import heapq
class AllOne3:
    def __init__(self):
        self.d_s=dict()
        self.heap=[]
        heapq.heapify(self.heap)

    def inc(self, key: str) -> None:
        if key in self.d_s:
            n = self.d_s[key]+1
            self.d_s[key]=n
        else:
            n=1
            self.d_s[key] = n
        heapq.heappush(self.heap,(n,key))

    def dec(self, key: str) -> None:
        n=self.d_s[key]
        if n-1==0:
            del self.d_s[key]
        else:
            self.d_s[key]=n-1
        fnd=(n,key)
        for i in range(len(self.heap)):
            if self.heap[i]==fnd:
                self.heap.pop(i)
                heapq.heapify(self.heap)
                break


    def getMaxKey(self) -> str:
        if len(self.d_s) !=0: # and len(self.heap) !=0
            t=heapq.nlargest(1, self.heap)
            return t[0][1]
        else: return ""

    def getMinKey(self) -> str:
        if (kk:=len(self.d_s)) !=0: #  and len(self.heap) !=0
            t=heapq.nsmallest(kk, self.heap)
            # ic('in getMinKey',t)
            if len(t)==1:
                return t[0][1]
            else:
                tt= [self.d_s[t1[1]] for t1 in t]
                mmin=min(tt)
                return t[tt.index(mmin)][1]
        else: return ""

    def pri(self):
        ic(self.d_s)
        ic(self.heap)

#########################################################
# Runtime 2469 ms Beats 9.00%
# Memory 34.13 MB Beats 12.82%
import heapq
class AllOne4:
    def __init__(self):
        self.d_s=dict()
        self.heap=[]
        heapq.heapify(self.heap)
        self.check=[0,0] # min max
        self.mmin=''
        self.mmax=''

    def inc(self, key: str) -> None:
        self.check = [0,0]
        if key in self.d_s:
            n = self.d_s[key]+1
            self.d_s[key]=n
        else:
            n=1
            self.d_s[key] = n
        heapq.heappush(self.heap,(n,key))

    def dec(self, key: str) -> None:
        self.check = [0,0]
        n=self.d_s[key]
        if n-1==0:
            del self.d_s[key]
        else:
            self.d_s[key]=n-1
        fnd=(n,key)
        for i in range(len(self.heap)):
            if self.heap[i]==fnd:
                self.heap.pop(i)
                heapq.heapify(self.heap)
                break


    def getMaxKey(self) -> str:
        if self.check[1] !=0:
            return self.mmax
        else:
            if len(self.d_s) !=0: # and len(self.heap) !=0
                t=heapq.nlargest(1, self.heap)
                res= t[0][1]
            else: res=""
            self.check[1]=1
            self.mmax=res
            return res

    def getMinKey(self) -> str:
        if self.check[0] !=0:
            return self.mmin
        else:
            if (kk:=len(self.d_s)) !=0: #  and len(self.heap) !=0
                t=heapq.nsmallest(kk, self.heap)
                # ic('in getMinKey',t)
                if len(t)==1:
                    res=t[0][1]
                else:
                    tt= [self.d_s[t1[1]] for t1 in t]
                    mmin=min(tt)
                    res =t[tt.index(mmin)][1]
            else: res= ""
            self.check[0]=1
            self.mmin=res
            return res


    def pri(self):
        ic(self.d_s)
        ic(self.heap)


# https://leetcode.com/problems/all-oone-data-structure/solutions/5847620/python-solution-runtime-118-ms-beats-100-00/
# Runtime 128 ms Beats 99.73%
# Memory 31.92 MB Beats 89.85%
class AllOne5:
    def __init__(self):
        self.dict = {}
        self.check = 0
        self.result = ""

    def inc(self, key: str) -> None:
        self.check = 0
        if (key in self.dict):
            self.dict[key] += 1
        else:
            self.dict[key] = 1

    def dec(self, key: str) -> None:
        self.check = 0
        if (self.dict[key] > 1):
            self.dict[key] -= 1
        else:
            del self.dict[key]
        return None

    def getMaxKey(self) -> str:
        if (self.check == 1):
            return self.result
        self.check = 1
        if (self.dict):
            maxv = list(self.dict.values())[0]
            maxk = list(self.dict.keys())[0]
            for i in self.dict.keys():
                if (self.dict[i] > maxv):
                    maxv = self.dict[i]
                    maxk = i
            self.result = maxk
            return maxk
        self.result = ""
        return ""

    def getMinKey(self) -> str:
        if (self.check == 2):
            return self.result
        self.check = 2
        if (self.dict):
            minv = list(self.dict.values())[0]
            mink = list(self.dict.keys())[0]
            for i in self.dict.keys():
                if (self.dict[i] < minv):
                    minv = self.dict[i]
                    mink = i
            self.result = mink
            return mink
        self.result = ""
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

from icecream import ic

def tst1():
    obj = AllOne4()
    obj.inc("hello")
    obj.inc("hello")
    ic(f'{obj.getMaxKey()=}')
    ic(f'{obj.getMinKey()=}')
    obj.inc("leet")
    ic(f'{obj.getMaxKey()=}')
    ic(f'{obj.getMinKey()=}')
    # obj.pri()

def tst10():
    obj = AllOne3()
    obj.inc("a")
    # obj.pri()
    for i in range(4): obj.inc("b")
    # obj.pri()
    for i in range(2): obj.dec("b")
    # obj.pri()
    ic(f'{obj.getMaxKey()=}')
    ic(f'{obj.getMinKey()=}')
    # obj.pri()

if __name__=="__main__":
    tst1()
    # tst10()
    # import heapq
    # seq = [(100,'a'), (2,'b'), (400,'c'), (500,'d'), (400,'e')]
    # print(heapq.nlargest(1, seq))
    # print(heapq.nsmallest(1, seq))