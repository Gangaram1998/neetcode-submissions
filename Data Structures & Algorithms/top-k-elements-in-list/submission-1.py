class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        topF = {}

        for key in nums:
            if key in topF:
                topF[key] +=1

            else:
                topF[key] = 1

        res = dict(sorted(topF.items() , key=lambda item : item[1], reverse=True))
        ans = []
        for key in res:
            if len(ans) == k:
                return ans

            ans.append(int(key))

        return ans





        