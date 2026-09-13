"""
# PRIMM: Predict 1

## Instructions

Read the following Python code snippet carefully. 
**Without running the code**, write down what you think the exact output will be. 
Explain your reasoning in a sentence or two.

---

### Your Prediction

**Predicted Output:**
Ticket price: $12 (Teen)
Enjoy the show!

**Reasoning:**
The program will compare the age variable to the condition. Since the first if statement is true, then the program will
print what the rest of the if statement says to do and skip over the elif and else statements to then print the ending
message.
"""

# A simple program to check age for a movie ticket
age = 15

print("Welcome to the theater!")

if age < 13:
    print("Ticket price: $8 (Child)")
elif age < 18:
    print("Ticket price: $12 (Teen)")
else:
    print("Ticket price: $15 (Adult)")

print("Enjoy the show!")


"""
Predict Activity 2: Number Check

Task: Without running the code, predict what the output will be.
Write down your prediction and your reasoning in a comment.

What do you think will be printed to the screen when this program runs?
"""

# Your Prediction:
# The program will print:
# It's not too hot today
# Your Reasoning:
# The program will compare the temperature variable to the if statement first. Since the variable makes the if statement
# false, the program will then skip to the else statement, which is to print "It's not too hot today."

temperature = 25

if temperature > 30:
  print("It's a hot day!")
else:
  print("It's not too hot today.")
