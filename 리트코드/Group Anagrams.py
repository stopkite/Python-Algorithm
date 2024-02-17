class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string] = [string]
            else:
                anagram_dict[sorted_string].append(string)

        answer = []
        for value in anagram_dict.values():
            answer.append(value)

        return answer

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(["ddddddddddg", "dgggggggggg"]))  # [["dgggggggggg"],["ddddddddddg"]]
