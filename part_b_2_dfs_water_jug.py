# Part B - 2: DFS for Problem Solving (Water Jug: 4L & 3L to get 2L)
stack = [((0, 0), [(0, 0)])]
seen = {(0, 0)}

while stack:
    (x, y), path = stack.pop()
    if x == 2 or y == 2:
        print("DFS Solution Path (Jug 1, Jug 2):")
        for step in path:
            print(step)
        break
    moves = [
        (4, y), (x, 3), (0, y), (x, 0),                       # Fill / Empty
        (max(0, x - (3 - y)), min(3, y + x)),                 # Pour x -> y
        (min(4, x + y), max(0, y - (4 - x)))                  # Pour y -> x
    ]
    for s in moves:
        if s not in seen:
            seen.add(s)
            stack.append((s, path + [s]))
