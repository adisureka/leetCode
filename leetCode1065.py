class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        lst = []
        for word in words:
            word_len =  len(word)
            # Check each position in the text to see if it starts a substring that matches word
            for i in range(len(text) - word_len + 1):
                if text[i:i + word_len] == word:
                    lst.append([i, i + word_len - 1])
        print(lst)
        lst.sort()
        print(lst)
        return lst
        