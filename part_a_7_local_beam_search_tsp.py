# Part A - 7: Local Beam Search for Traveling Salesman Problem (TSP)
import random

cities = [0, 1, 2, 3]
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(t):
    return sum(dist[t[i]][t[(i+1)%len(t)]] for i in range(len(t)))

# Keep beam of k=2 best states
beam = [random.sample(cities, 4) for _ in range(2)]

for _ in range(5):
    cand = []
    for s in beam:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                cpy = list(s)
                cpy[i], cpy[j] = cpy[j], cpy[i]
                cand.append(cpy)
    cand.sort(key=cost)
    beam = cand[:2]

print("Best TSP Tour:", beam[0], "Total Cost:", cost(beam[0]))
