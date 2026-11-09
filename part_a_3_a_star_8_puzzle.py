# Part A - 3: A* Search for 8-Puzzle Problem
import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):  # Misplaced tiles heuristic
    return sum(1 for i in range(9) if s[i] and s[i] != goal[i])

def get_next(s):
    i = s.index(0)
    r, c = divmod(i, 3)
    res = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= r + dr < 3 and 0 <= c + dc < 3:
            ni = (r + dr) * 3 + (c + dc)
            lst = list(s)
            lst[i], lst[ni] = lst[ni], lst[i]
            res.append(tuple(lst))
    return res

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
pq = [(h(start), 0, start)]
seen = set()

while pq:
    f, g, s = heapq.heappop(pq)
    if s == goal:
        print(f"8-Puzzle solved in {g} steps!")
        break
    seen.add(s)
    for nxt in get_next(s):
        if nxt not in seen:
            heapq.heappush(pq, (g + 1 + h(nxt), g + 1, nxt))
