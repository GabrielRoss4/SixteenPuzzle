'''
* This file will house helper objects and functions for 
  the puzzle project
'''

class queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return True

    def dequeue(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

    def present(self, someItem):
        return someItem in self.queue

class stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)
        return True 
    
    def pop(self):
        return self.stack.pop(0)

    def empty(self):
        return len(self.stack) == 0