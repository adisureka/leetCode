class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # lst = []
        result = []
        temp = []
        # temp2 = []
        # temp3 = []

        while (len(nums) > 0):
            temp = []
            i = 0
            leng = len(nums)
            while(i < leng):
                item = nums.pop(0)
                if(item not in temp):
                    temp.append(item)
                    # print(temp)
                else:
                    nums.append(item)
                    # print(nums)
                i += 1
            print(nums)
            result.append(temp)

        return(result)

        # for i in range(len(nums)):
        #     if(nums[i] not in lst):
        #         lst.append(nums[i])

            


        # result.append(lst)
        # result.append(temp)
        # if(len(temp2) > 0):
        #     result.append(temp2)
        # if(len(temp3) > 0):
        #     result.append(temp3)


        # for i in range(len(nums)):
        #     if(nums[i] not in lst):
        #         lst.append(nums[i])
        #         # nums.pop(nums[i])
        # result.append(lst)
        # lst = []


        # print(lst)
        # return(result)

    # Solution : Queue for all programming languages

        # class Queue():
        #     def __init__(self, data = None):
        #         if(data == None):
        #             self.data = []
        #         else:
        #             self.data = data
        #     def is_empty(self):
        #         return len(self.data) == 0
        #     def push(self, item):
        #         self.data.append(item)
        #     def peek(self):
        #         if(not self.is_empty()):
        #             return self.data[0]
        #     def pop(self):
        #         if(not self.is_empty()):
        #             return self.data.pop(0)
        #     def __str__(self):
        #         # return self.data
        #         temp = []
        #         for i in range(len(self.data)):
        #             temp.append(str(self.data[i]))
        #         return "Queue:" + ", ".join(temp)
        #     def to_list(self):
        #         return self.data
        #     def length(self):
        #         return len(self.data)

        # q1 = Queue(nums)
        # print(q1)

        # result = []

        # # Queue only works with nested while loops or while loops
        # while not (q1.is_empty()):
        #     temp = []
        #     i = 0
        #     leng = q1.length()
        #     while(i < leng):
        #         item = q1.pop()
        #         if(item not in temp):
        #             temp.append(item)
        #         else:
        #             q1.push(item)
        #         i += 1
        #     print(q1)
        #     result.append(temp)
        
        # # print(result)

        # return(result)



        # Testing how many sets of each number we have
        # test = Counter(nums)
        # print(test)


        # lst = []
        # result = []
        # temp = []
        # temp2 = []
        # temp3 = []

        # for i in range(len(nums)):
        #     if(nums[i] not in lst):
        #         lst.append(nums[i])
        #     elif(nums[i] not in temp):
        #         temp.append(nums[i])
        #     elif(nums[i] not in temp2):
        #         temp2.append(nums[i])
        #     else:
        #         temp3.append(nums[i])


        # result.append(lst)
        # result.append(temp)
        # if(len(temp2) > 0):
        #     result.append(temp2)
        # if(len(temp3) > 0):
        #     result.append(temp3)


        # for i in range(len(nums)):
        #     if(nums[i] not in lst):
        #         lst.append(nums[i])
        #         # nums.pop(nums[i])
        # result.append(lst)
        # lst = []


        # print(lst)
        # return(result)