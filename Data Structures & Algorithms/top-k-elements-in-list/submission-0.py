import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        x = {}

        for i in nums:
            if i in x:
                x[i]+=1
            else:
                x[i] = 1

        j = []
        for key,value in x.items():
            j.append((-value,key))

        heapq.heapify(j)
        l = []
        count=0

        for i in range(k):
            l.append(j[i][1])

        return l
