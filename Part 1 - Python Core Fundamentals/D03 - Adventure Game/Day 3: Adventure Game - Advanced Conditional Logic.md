Day 3: Adventure Game - Advanced Conditional Logic
Welcome to Day 3! You've learned how to get input and perform basic calculations. Now, let's give your programs a brain. Today is all about conditional logic, which allows your code to make decisions and follow different paths based on different situations.

1. Key Concepts of the Day
a. The if/elif/else Chain
You've already used a simple if/else structure. But what if you have more than two possible outcomes? That's where elif (short for "else if") comes in. It lets you check for multiple different conditions in a sequence.

if: Starts the chain. The code inside only runs if its condition is True.

elif: Checks another condition only if the previous if (or elif) was False. You can have as many elif statements as you need.

else: Is the catch-all. Its code runs only if all the preceding if and elif conditions were False.

# Example: Grading system
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

b. Comparison and Logical Operators
To create powerful conditions, you need to compare values and combine checks.

Comparison Operators:
| Operator | Meaning                | Example       | Result if x=5, y=10 |
| :------- | :--------------------- | :------------ |:--------------------|
| ==     | Equal to               | x == y      | False             |
| !=     | Not equal to           | x != y      | True              |
| >      | Greater than           | x > y       | False             |
| <      | Less than              | x < y       | True              |
| >=     | Greater than or equal to | x >= 5      | True              |
| <=     | Less than or equal to  | y <= 10     | True              |

Logical Operators: These let you combine boolean (True/False) values.
| Operator | Meaning                                   | Example                   | Result if age=25 |
| :------- | :---------------------------------------- | :------------------------ | :-----------------|
| and    | True if both sides are True       | age > 18 and age < 30   | True             |
| or     | True if at least one side is True | age < 18 or age > 65    | False            |
| not    | Inverts the boolean value                 | not (age > 30)          | True             |

2. Warm-Up Exercises
Create a new file called day03_exercises.py to practice.

Exercise 1: Weekend Checker
Write a script that asks for the day of the week (e.g., "Monday"). If it's "Saturday" or "Sunday", print "It's the weekend!". Otherwise, print "It's a weekday."

Exercise 2: Ticket Prices
Write a script for a movie theater. Ask for the user's age. If they are under 12, the ticket is $5. If they are between 12 and 65 (inclusive), it's $10. If they are over 65, it's $7. Print the correct ticket price.

Exercise 3: Simple Validation
Ask the user for a password. If the password is "python123", print "Login successful." If it's anything else, print "Incorrect password."

3. Daily Project: Text-Based Adventure Game
Your project today is to create a simple "Choose Your Own Adventure" game. The story will unfold based on the user's choices. This is a perfect way to practice nested if/elif/else statements.

Project Goal: Guide a user through a short, branching story where their decisions determine the outcome.

File Name: adventure.py

Save Location: ~/python-practice-25-26/Part 1 - Python Core Fundamentals/D03 - Adventure Game/adventure.py

Instructions for Your Terminal (Project Setup):
# Step 1: Navigate to your Part 1 directory
cd ~/python-practice-25-26/"Part 1 - Python Core Fundamentals"

# Step 2: Create a directory for today's project
mkdir "D03 - Adventure Game"

# Step 3: Change into the new directory
cd "D03 - Adventure Game"

# Step 4: Create the Python file and the README for your project
touch adventure.py
touch README.md

Project Implementation:
Start by printing a welcome message and the first scenario (e.g., "You wake up in a dark forest. There is a path to your left and a cave to your right. Which do you choose?").

Use an input() to get the user's first choice.

Create an if/elif/else block to handle the user's choice.

Inside each block, present the user with a new scenario and a new choice.

Use another, nested if/elif/else block to handle this second choice.

Each of these second-level choices should lead to a final outcome (e.g., "You found a treasure chest! You win!", "A dragon eats you. Game Over.").

Make sure to have an else block at each stage to handle invalid user input (e.g., "Invalid choice. Game Over.").

Finishing Up (Git Workflow):
Write a README.md for this project.

Navigate back to the main project root (~/python-practice-25-26).

Add, commit, and push your work to GitHub.

cd ~/python-practice-25-26
git add .
git commit -m "Day 3: Completed Text-Based Adventure Game"
git push
