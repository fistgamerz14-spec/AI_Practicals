# Part B - 5: Intelligent Number Guessing Agent (Binary Search)
low, high = 1, 100
secret = 42
steps = 0

print(f"Target Secret Number: {secret}")
while low <= high:
    guess = (low + high) // 2
    steps += 1
    print(f"Attempt {steps}: Agent guesses {guess}")
    if guess == secret:
        print(f"Success! Agent found {secret} in {steps} steps.")
        break
    elif guess < secret:
        print("Feedback: Higher")
        low = guess + 1
    else:
        print("Feedback: Lower")
        high = guess - 1
