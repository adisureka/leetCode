from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if len(str1) > len(str2):
                return False

            # Check if str1 is a prefix of str2
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return False

            # Check if str1 is a suffix of str2
            for i in range(len(str1)):
                if str1[i] != str2[len(str2) - len(str1) + i]:
                    return False

            return True

        count = 0
        n = len(words)

        # Iterate over all pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
                    print(f"Pair ({i}, {j}) with words '{words[i]}' and '{words[j]}' is valid")
        # print(isPrefixAndSuffix("ab", "abcab"))
        return count

# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         def isPrefixAndSuffix(str1: str, str2: str):
#             # Special case where len(str1) > len(str2)
#             if(len(str1) > len(str2)):
#                 return False
#             pre = ""
#             suf = ""
#             # Str2 should be the longer string
#             for i in range(len(str2)):
#                 if(str1[i] == str2[i] and len(str1) < len(str2)):
#                     print(i)
#                     pre += str2[i]
#                     print("Prefix is: ", pre)
#                 else: print("No match in the str2") 
#         print(isPrefixAndSuffix("ab", "abcab"))

        