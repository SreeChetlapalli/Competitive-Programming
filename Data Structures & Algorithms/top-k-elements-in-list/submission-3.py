class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        x = {}
        for num in nums:
            if num in x:
                x[num] += 1
            else:
                x[num] = 1

        Y = []
        for num, count in x.items():
            heapq.heappush(Y, (-count, num))

        z = []
        for i in range(k):
            count, num = heapq.heappop(Y)
            z.append(num)

        return z
