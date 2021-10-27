class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.mycdq = [0] * k # 初始化数组空间
        self.k = k # k值虽然可以由数组长度计算得出，但需要频繁使用，还是单独列出提升效率
        self.start = 0 # 记录元素起始位置
        self.end = 0 # 记录元素结束后的第一个空闲位置
        self.count = 0 # 记录元素个数



    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.k: # 如队列已满
            return False
        self.start = (self.start - 1) % self.k # 更新start的位置
        self.mycdq[self.start] = value # 给新的start位置赋值
        self.count += 1
        return True



    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.k: # 如队列已满
            return False
        self.end = (self.end + 1) % self.k # 更新start的位置
        self.mycdq[self.end] = value # 给新的start位置赋值
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.start=self.start+1
        self.count-=1
        return True



    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.end=self.end-1
        self.count-=1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.mycdq[self.start]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.mycdq[self.end]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.mycdq[self.start:self.end+1])==0


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.mycdq[self.start:self.end+1])==self.k
