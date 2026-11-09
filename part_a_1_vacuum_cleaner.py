# Part A - 1: Simple Reflex Agent for Vacuum Cleaner World
env = {'A': 'DIRTY', 'B': 'DIRTY'}
loc = 'A'

print("Initial Environment:", env)
for step in range(4):
    if env[loc] == 'DIRTY':
        env[loc] = 'CLEAN'
        print(f"Step {step+1}: At {loc} -> Action: SUCK (Cleaned)")
    else:
        loc = 'B' if loc == 'A' else 'A'
        print(f"Step {step+1}: At room -> Action: Move to {loc}")
print("Final Environment:", env)
