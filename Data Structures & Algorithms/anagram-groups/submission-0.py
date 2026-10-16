class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs :
            val = "".join(sorted(s))

            if val in anagrams :
                anagrams[val].append(s)
            else:
                anagrams[val] = [s]


        output = []
        for key in anagrams :
            output.append(anagrams[key])

        return output





