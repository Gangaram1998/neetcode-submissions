class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict ={}

        for i,num in enumerate(nums) :

            dict[num] = i

        for  i, num in enumerate(nums) :
            val = target-num

            if dict.get(val) :
                return [i,dict.get(val)]

            
        