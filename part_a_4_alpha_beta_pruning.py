# Part A - 4: Adversarial Search with Alpha-Beta Pruning
def alphabeta(d, idx, is_max, vals, a, b):
    if d == 3:
        return vals[idx]
    if is_max:
        best = -float('inf')
        for i in range(2):
            best = max(best, alphabeta(d + 1, idx * 2 + i, False, vals, a, b))
            a = max(a, best)
            if b <= a:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            best = min(best, alphabeta(d + 1, idx * 2 + i, True, vals, a, b))
            b = min(b, best)
            if b <= a:
                break
        return best

vals = [3, 5, 6, 9, 1, 2, 0, -1]
print("Leaf Values:", vals)
print("Optimal Game Value:", alphabeta(0, 0, True, vals, -float('inf'), float('inf')))
