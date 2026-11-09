# Part B - 7: Game-Playing Agent using Minimax (Tic-Tac-Toe)
def winner(b):
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for r in lines:
        if b[r[0]] == b[r[1]] == b[r[2]] != ' ':
            return b[r[0]]
    return 'Tie' if ' ' not in b else None

def minimax(b, is_max):
    res = winner(b)
    if res == 'X': return 1
    if res == 'O': return -1
    if res == 'Tie': return 0

    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            scores.append(minimax(b, not is_max))
            b[i] = ' '
    return max(scores) if is_max else min(scores)

board = ['X', 'O', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
empty_indices = [i for i in range(9) if board[i] == ' ']

best_move = -1
best_val = -float('inf')
for i in empty_indices:
    board[i] = 'X'
    val = minimax(board, False)
    board[i] = ' '
    if val > best_val:
        best_val = val
        best_move = i

print(f"Board State: {board}")
print(f"Optimal Next Move Index for 'X': {best_move}")
