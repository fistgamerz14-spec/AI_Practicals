# Part A - 5: Tower of Hanoi by State Space Search (BFS)
from collections import deque

start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))
q = deque([(start, 0)])
seen = {start}

while q:
    state, steps = q.popleft()
    if state == goal:
        print(f"Tower of Hanoi solved in {steps} steps!")
        break
    for i in range(3):
        for j in range(3):
            if state[i] and (not state[j] or state[i][-1] < state[j][-1]):
                nxt = [list(p) for p in state]
                nxt[j].append(nxt[i].pop())
                nxt = tuple(tuple(p) for p in nxt)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
