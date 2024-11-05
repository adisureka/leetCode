class Solution:
    def digitCount(self, num: str) -> bool:
        # lst = []
        # lst.append(num)
        # print(list(num))

        def help(string, target):
            # 1210, 0 => 1
            count = 0 
            for i in range(len(string)):
                if(target == string[i]):
                    count += 1
            return(str(count))

        # print(help(num, '1'))

        for i in range(len(num)):
            print(help(num, str(i)))
            if(help(num, str(i)) != num[i]):
                print(help(num, str(i)), num[i])
                print(type(help(num, str(i))), type(num[i]))
                return False
        else:
            return True

            # if(help() )
            #lst.append(num)
        
        