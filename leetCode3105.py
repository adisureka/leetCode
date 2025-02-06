class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        class Stack():
            def __init__(self, data = None):
                if(data == None):
                    self.data = []
                else:
                    self.data = data
            def pop(self):
                if not self.is_empty():
                    return self.data.pop()
            def push(self, item):
                self.data.append(item)
            def peek(self):
                if not self.is_empty():
                    return self.data[-1]
            def is_empty(self):
                return len(self.data) == 0
            def length(self):
                return len(self.data)
            def __str__(self):
                text = "Stack: "
                for i in range(len(self.data)):
                    text += str(self.data[i]) + ", "
                return text
            def to_list(self):
                return self.data

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

        largest = 1

        source = Queue(nums.copy())
        temp = Stack()

        temp.push(source.pop())

        while not(source.is_empty()):
            # print(source)
            # print(temp)
            item = source.pop()
            if(item > temp.peek()):
                temp.push(item)
            else:
                if(temp.length() > largest):
                    largest = temp.length()
                temp = Stack()
                temp.push(item)
        
        if(temp.length() > largest):
            largest = temp.length()
        
        source = Queue(nums)
        temp = Stack()

        temp.push(source.pop())

        while not(source.is_empty()):
            # print(source)
            # print(temp)
            item = source.pop()
            if(item < temp.peek()):
                temp.push(item)
            else:
                if(temp.length() > largest):
                    largest = temp.length()
                temp = Stack()
                temp.push(item)

            # print(largest)
            # print("-------------------")
        if(temp.length() > largest):
            largest = temp.length()

        return largest
        # temp.push(source.pop())

        # print(source)
        # print(temp)

        # print(source.peek())
        # print(temp.peek())

            
# Solution 1: Naive approach using nested list 

        # lst = []
        # subarr = []
        # l = len(nums)

        # while(l > 0):
        #     left = 0
        #     right = left + l
        #     while(right < len(nums)):
        #         subarr.append(nums[left:right + 1])
        #         left += 1
        #         right += 1
        #     l -= 1

        # # print(subarr)
        # result = []
        
        # def increasing(arr):
        #     for i in range(1, len(arr)):
        #         if(arr[i] <= arr[i - 1]):
        #             return False
        #     else:
        #         return arr

        # def decreasing(arr):
        #     for i in range(1, len(arr)):
        #         if(arr[i] >= arr[i - 1]):
        #             return False
        #     else:
        #         return arr

        # for i in range(len(subarr)):
        #     if(increasing(subarr[i]) != False):
        #         result.append(subarr[i])

        # for i in range(len(subarr)):
        #     if(decreasing(subarr[i]) != False):
        #         result.append(subarr[i])
        
        # print(result)

        # length = 1

        # for i in range(len(result)):
        #     if(len(result[i]) > length):
        #         length = len(result[i])
        
        # return length