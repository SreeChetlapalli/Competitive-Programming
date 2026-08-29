class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        f = []
        n = len(nums)

        for i in range(n):
            x = nums[i]
            y = {}
            seen_pairs = set()  # to avoid duplicate triplets from this i

            for k in range(n):
                if k == i:
                    continue
                j = nums[k]
                complement = -x - j
                if complement in y:
                    triplet = tuple(sorted([x, j, complement]))
                    if triplet not in seen_pairs:
                        seen_pairs.add(triplet)
                        f.append([x, j, complement])
                else:
                    y[j] = k

        # remove duplicate triplets across different i's
        final = []
        seen = set()
        for triplet in f:
            key = tuple(sorted(triplet))
            if key not in seen:
                seen.add(key)
                final.append(triplet)

        return final