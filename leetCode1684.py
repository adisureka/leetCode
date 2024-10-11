class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # short version that works for Java too
        # Below is a better verison that is more explanatory

        count = 0
        for i in range(len(words)):
            for j in range(len(words[i])):
                if(words[i][j] not in allowed):
                    break
            else:+
                count += 1
        
        return(count)

        '''
        def helper(rules, word):
            # this works for one word, now make it work for a list
            for i in range(len(word)):
                if(word[i] not in rules):
                    return False
            # using a for else:
            # we use a for else instead of putting the else after the if
            # as for else means that if there is not a single match in the nested if for the loop, then it goes to the else
            else:
                return True
        
        # counter to count the number of matching strings from the list
        count = 0

        # Checking the entire list with the defined rules
        for i in range(len(words)):
            if helper(allowed, words[i]):
                print(words[i])
                count += 1

        print(helper("ab", "aaba"))
        print(helper("ab", "ad"))

        return(count)

        '''


        