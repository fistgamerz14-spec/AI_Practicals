# Part A - 2: Model-Based Agent Navigating Grid with Obstacles
pos, goal = [0, 0], [2, 2]
obs = {(1, 1)}

print(f"Start: {pos}, Goal: {goal}, Obstacles: {obs}")
while pos != goal:
    if pos[0] < goal[0] and (pos[0] + 1, pos[1]) not in obs:
        pos[0] += 1
    elif pos[1] < goal[1] and (pos[0], pos[1] + 1) not in obs:
        pos[1] += 1
    else:
        pos[0] += 1  # Bypass obstacle
    print("Agent moved to:", pos)
print("Goal reached successfully!")
