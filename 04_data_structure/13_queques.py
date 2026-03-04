from collections import deque


queue = deque([])


queue.append(1)
queue.append(2)
queue.append(3)

print("queues :",queue)

queue.popleft()

print("After poping the list :",queue)