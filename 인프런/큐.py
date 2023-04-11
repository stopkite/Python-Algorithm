# 리스트로 구현하기
q = []
# enqueue O(1)
q.append(1)
q.append(2)

# dequeue O(N)
q.pop(0)
q.pop(0)


# 링크드 리스트로 구현하기
from collections import deque
queue = deque()

# enqueue O(1)
queue.append(1)
queue.append(2)

# dequeue O(1)
queue.popleft()
queue.popleft()