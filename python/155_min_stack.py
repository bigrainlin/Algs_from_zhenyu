"""
Method 1:
recompute min each time push/pop any value:
if push:
    just compare last time min with the new value
if pop:
    compute the min of stack[:-1], then pop
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min == None:
            self.min = x
        else:
            self.min = min(self.min, x)
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        
        if self.data:
            if self.data[:-1]:
                self.min = min(self.data[:-1])
            else:
                self.min = None
            return self.data.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.data:    
            return self.data[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        

# test

"""
Method 2:
keep a min value with each element of the stack
"""

class MinStack2(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            self.data.append((x, x))    
        else:
            self.data.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        
        if self.data:
            self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data:    
            return self.data[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][1]
        else:
            return None


obj = MinStack()
obj.push(10)
obj.push(1)
print obj.top()
print obj.pop()
print obj.getMin()
print obj.pop()
print obj.getMin()