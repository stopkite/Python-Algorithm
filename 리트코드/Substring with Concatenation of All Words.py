from itertools import permutations


class Solution:
    def findSubstring(self, s: str, words):
        answer = []

        word_dict = {}
        for permu in permutations(words):
            word = ''.join(permu)
            word_dict[word] = 1

        word_len = len(''.join(words))
        for i in range(len(s) - word_len + 1):
            if s[i: i + word_len] in word_dict:
                answer.append(i)

        return answer


solution = Solution()
print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
