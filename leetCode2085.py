class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Can you use set()?
        print(Counter(words1))

        # lst = []
        count = 0

        # use a helper function to remove all the elements from in a list that appear more than once
        def help(List):
            lst = []
            for key in Counter(List):
                value = Counter(List)[key]
                if(value == 1):
                    lst.append(key)
            return(lst)
        
        # Saving the function call in variables will drmatically reduce the computational load of operations for any machine
        lst1 = help(words1)
        lst2 = help(words2)

        for i in range(len(help(words1))):

            # print(help(words1)[i])

            # This doesn't work as we are makign so many function calls, so because of that the time limit exceeds at testcase 29
            # if(help(words1)[i] in help(words2)):
                # count += 1

            # this is just much more faster eventhough it is the same as the above :- here we just reduce the function call
            if(lst1[i] in lst2):
                count += 1
        
        return(count)




        