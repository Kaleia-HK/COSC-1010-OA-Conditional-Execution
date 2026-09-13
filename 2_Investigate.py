"""
# PRIMM: Investigate 1

## Instructions

Now, let's investigate the code from the "Predict" activity. 
Run the code in a Python environment to see the actual output. 
Then, answer the questions below.

---

### Questions

1.  **First Question:** The first `if` statement checks the condition `age < 13`. Is this condition `True` or `False`?
    Why?
This condition is false because 15 is not less than 13.

2.  **Second Question:** The `elif` statement checks the condition `age < 18`. Why does the program check this condition
    *after* the first `if` statement?
The program checks that condition after the if statement because the if statement was proven false, so the program
goes onto the next condition to check.

3.  **Flow of Control:** Which of the three `print` statements for the ticket price was executed? Why were the other
    two skipped?
The print("Ticket price: $8 (Child)") statement was printed because the variable satisfied the condition for it to print.
The other two were skipped because 15 is not less than 13, and since the first elif statement was fulfilled, the other
statements did not need to be run through.

4.  **Indentation:** What do you think would happen if you removed the indentation (the spaces) before
    `print("Ticket price: $12 (Teen)")`?
If the indentation was removed, the program will display an error because it will read the print statement globally
rather than local to that elif statement.

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
Investigate Activity 2: Grade Boundaries

Task: Run this code with different values for `score`.
Answer the questions in the comments below.
"""

score = 89.9# Try changing this value! (e.g., 89, 90, 91)

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
else:
  grade = "Needs Improvement"

print(f"A score of {score} gets a grade of {grade}.")

"""
Questions:

1. What is the lowest score you can get and still receive a "B"?
   Why does this happen?
The lowest score you can get and still receive a "B" is 80 because anything else under 80 does not make the first elif 
statement true, however it does make the second elif statement true. 

2. What happens if you enter a score of 89.9? What about 90?
   What does the `>=` operator mean?
When entering a score of 89.9, the program outputs that: A score of 89.9 gets a grade of B. and when entering a score of
90, the program outputs: A score of 90 gets a grade of A.

3. If the first `if` statement was `if score > 90:`, how would that
   change the grade for a score of 90?
It would change the score by giving the value 90 a grade of B because 90 cannot be more than 90. 
"""

"""
Investigate Activity 3: Nested Conditions

Task: Run this code and observe its behavior.
Answer the questions in the comments below.
"""

is_logged_in = True
is_admin = True # Try changing this to True!

if is_logged_in:
  print("Welcome to the system.")
  if is_admin:
    print("You have admin privileges.")
  else:
    print("You have standard user privileges.")
else:
  print("Please log in to continue.")


"""
Questions:

1. What two conditions must be true for the message "You have admin privileges."
   to be printed?
The variables `is_logged_in` and `is_admin` have to be true for the message "You have admin privileges." to be printed. 

2. Why is the second `if/else` block indented inside the first `if` block?
   What does this indentation tell Python?
The second `if/else` block is indented inside the first if block because it requires `is_logged_in` to be true before starting
the if loop. The indentation tells Python that the `if/else` block is local to the `if is_logged_in` block. 

3. What is printed if `is_logged_in` is `False`? Does the program even
   check if the user is an admin in that case? Why?
If `is_logged_in` is false, the program does not check if the user is an admin in that case because that loop function is 
tied into the admin. If the user is not logged in, then the program cannot know whether the user is admin or not. 
"""


