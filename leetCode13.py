class Solution:
    def romanToInt(self, s: str) -> int:


# Solution 3 - stack version
        class Stack():
            """docstring for Stack"""
            def __init__(self):
                self.data = []

            def is_empty(self):
                return(len(self.data)) == 0
                
            def peek(self):
                if(not self.is_empty()):
                    return(self.data[-1])
                else: 
                    return("Stack is empty")

            def push(self, item):
                self.data.append(item)

            def remove(self):
                if(not self.is_empty()):
                    return(self.data.pop())
                else:
                    return None

        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
            
        stack = Stack()
        stack.push(s[0])

        for i in range(1, len(s)):
            if(s[i] in "VX" and stack.peek() == "I") or (s[i] in "LC" and stack.peek() == "X") or (s[i] in "DM" and stack.peek() == "C"):
                result -= d[stack.remove()]
                stack.push(s[i])
            
            else:
                result += d[stack.remove()]
                stack.push(s[i])
        result += d[stack.remove()]
        return result


# Solution 2

        # d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        # result = 0

        # for i in range(len(s)):

        #     print(s[i])
        #     if(i > 0):
        #         if(s[i-1] == "I" and s[i] in "XV"):
        #             temp =  d[s[i]] - (d[s[i-1]] * 2)
        #             result += temp
        #             print("if", temp)
        #         elif(s[i-1] == "X" and s[i] in "LC"):
        #             temp = d[s[i]] - (d[s[i-1]] * 2)
        #             result += temp
        #             print("elif 1", temp)
        #         elif(s[i-1] == "C" and s[i] in "DM"):
        #             temp = d[s[i]] - (d[s[i-1]] * 2)
        #             result += temp
        #             print("elif 2", temp)
        #         else:
        #             temp = d[s[i]]
        #             result += temp
        #             print("else", temp)
        #     else:
        #         temp = d[s[i]]
        #         result += temp

        # return result

# Solution 1

        # def table(char):
        #     if(char == "I"):
        #         return 1
        #     elif(char == "V"):
        #         return 5
        #     elif(char == "X"):
        #         return 10
        #     elif(char == "L"):
        #         return 50
        #     elif(char == "C"):
        #         return 100
        #     elif(char == "D"):
        #         return 500
        #     elif(char == "M"):
        #         return 1000
        
        # integer = 0
        # i = 0

        # while (True):
        #     if(i >= len(s)):
        #         break
        #     elif(s[i] == "C"):
        #         if(i + 1 < len(s) and s[i + 1] == "M"):
        #             integer += 900
        #             i += 1
        #         elif(i + 1 < len(s) and s[i + 1] == "D"):
        #             integer += 400
        #             i += 1
        #         else: integer += table(s[i])
        #     elif(s[i] == "X"):
        #         if(i + 1 < len(s) and s[i + 1] == "L"):
        #             integer += 40
        #             i += 1
        #         elif(i + 1 < len(s) and s[i + 1] == "C"):
        #             integer += 90
        #             i += 1
        #         else: integer += table(s[i])
        #     elif(s[i] == "I"):
        #         if(i + 1 < len(s) and s[i + 1] == "V"):
        #             integer += 4
        #             i += 1
        #         elif(i + 1 < len(s) and s[i + 1] == "X"):
        #             integer += 9
        #             i += 1
        #         else: integer += table(s[i])
        #     else: 
        #         integer += table(s[i])
        #     i += 1


        # # for i in range(len(s)):
        #     # integer += table(s[i])

        # return integer
