import queue

q=queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get())
print(q.get())
print(q.get())
print(q.get())

from collections import deque

class Queue(deque):

    def enqueue(self,x):
        super().append(x)
    def dequeue(self):
        super().popleft()
    def display(self):
        for node in self .__iter__():
            print(node)

