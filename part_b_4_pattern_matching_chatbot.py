# Part B - 4: Simple Chatbot using Predefined Rules and Pattern Matching
import re

pairs = {
    r'.*(hi|hello|hey).*': "Hello! How can I assist you today?",
    r'.*name.*': "I am a simple rule-based AI bot.",
    r'.*(heuristic|admissible).*': "An admissible heuristic never overestimates the true distance to the goal.",
    r'.*bye.*': "Goodbye and good luck with your viva!"
}

def reply(text):
    for pattern, ans in pairs.items():
        if re.search(pattern, text, re.I):
            return ans
    return "I am sorry, I do not understand that."

test_inputs = ["Hello", "What is your name?", "Explain admissible heuristic", "bye"]
for inp in test_inputs:
    print(f"User: {inp}")
    print(f"Bot : {reply(inp)}\n")
