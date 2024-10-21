class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # dict_ = {}
        # new_dict = {}

        # for i in range(len(s)):
        #     key = s[i]
        #     if key not in dict_:
        #         dict_[key] = 1
        #     else:
        #         dict_[key] += 1

        # print(dict_)
        # lst = []
        # for key in dict_:
        #     lst.append(dict_[key])
        # print(lst)

        # return len(set(lst)) == 1

        # temp = set(dict(Counter(s)).values())
        # print(temp)

        # One line answer
        return len(set(dict(Counter(s)).values())) == 1

            # understand the below statement properly
            # .get() is a method in pythonic dictionary :- "(s[i], 0) + 1" as if there is no key for s[i]
            # then the dictionary records it and +1 is added to it
            # new_dict[s[i]] = new_dict.get(s[i], 0) + 1

        # for key in dict_:
        # count = list(new_dict.values())
        # print(count)
        
        # Pythonic language
        # return all(freq == count[0] for freq in count)

                 


        