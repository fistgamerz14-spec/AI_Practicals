# Part B - 6: Goal Stack Planning for Blocks World
# Initial: OnTable(A), OnTable(B), Clear(A), Clear(B), ArmEmpty
state = {"ONTABLE(A)", "ONTABLE(B)", "CLEAR(A)", "CLEAR(B)", "ARMEMPTY"}
goal = "ON(A,B)"
stack = [goal]
plan = []

while stack:
    top = stack.pop()
    if top == "ON(A,B)":
        if top not in state:
            stack.extend(["STACK(A,B)", "HOLDING(A)", "CLEAR(B)"])
    elif top == "HOLDING(A)":
        if top not in state:
            stack.extend(["PICKUP(A)", "ONTABLE(A)", "CLEAR(A)", "ARMEMPTY"])
    elif top.startswith("PICKUP") or top.startswith("STACK"):
        plan.append(top)
        state.add(top)

print("Generated Blocks World Plan:", plan)
