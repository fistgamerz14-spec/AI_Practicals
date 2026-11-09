# Part B - 3: Backtracking Search for 8-Queens Problem
def queens(cols=8, state=[]):
    if len(state) == cols:
        return [state]
    res = []
    for r in range(cols):
        if all(r != c and abs(r - c) != len(state) - i for i, c in enumerate(state)):
            res += queens(cols, state + [r])
    return res

all_solutions = queens(8)
print("Total 8-Queens Solutions Found:", len(all_solutions))
print("First Solution (Queen row positions per column):", all_solutions[0])
