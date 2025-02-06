class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        class Queue():
            def __init__(self, data = None):
                if(data == None):
                    self.data = []
                else:
                    self.data = data
            def pop(self):
                if not self.is_empty():
                    return self.data.pop(0)
            def push(self, item):
                self.data.append(item)
            def peek(self):
                if not self.is_empty():
                    return self.data[0]
            def is_empty(self):
                return len(self.data) == 0
            def length(self):
                return len(self.data)
            def __str__(self):
                text = "Queue: "
                for i in range(len(self.data)):
                    text += str(self.data[i]) + ", "
                return text
            def to_list(self):
                return self.data

        result = []
        groupSizesIndex = []

        for i in range(len(groupSizes)):
            temp = [groupSizes[i], i]
            groupSizesIndex.append(temp)

        print(groupSizesIndex)

        groupQ = Queue(groupSizesIndex)

        # item = groupQ.pop()

        while not(groupQ.is_empty()):
            item = groupQ.peek()
            newQ = Queue()
            while(newQ.length() < item[0]):
                temp = groupQ.pop()
                if(temp[0] == item[0]):
                    newQ.push(temp[1])
                else:
                    groupQ.push(temp)
            result.append(newQ)

        # print(result)
        result2 = [] 
        for i in range(len(result)):
            result2.append(result[i].to_list())

        print(result2)

        return result2


        



        # print(groupQ)
        
        # item = (groupQ.pop())
        # groupQ.push(item)

        # print(groupQ)

        # THIS below works for value not the index

        # while not(groupQ.is_empty()):

        #     item = groupQ.peek()
        #     # print(item)
        #     # print(groupQ)

        #     newQ = Queue()
        #     while(newQ.length() < item):
        #         temp = groupQ.pop()
        #         if(temp == item):
        #             newQ.push(temp)
        #         else:
        #             groupQ.push(temp)
        #     print(groupQ)
        #     print(newQ)

        #     result.append(newQ)
        #     print(result)

        # for i in range(len(result)):
        #     print(result[i])
