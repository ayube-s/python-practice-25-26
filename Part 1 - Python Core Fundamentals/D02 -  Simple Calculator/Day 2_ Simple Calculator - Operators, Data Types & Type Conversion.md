# **Day 2: Simple Calculator \- Operators, Data Types & Type Conversion**

Welcome to Day 2\! Today, we'll build on what we learned by handling numbers and performing calculations. This is a fundamental building block for almost any program you'll write.

### **1\. Key Concepts of the Day**

#### **a. Numeric Data Types: int and float**

In Python, numbers are not all the same. The two most common numeric types are:

* **int (Integer):** Whole numbers, both positive and negative, without any decimal points.  
  * Examples: 10, \-3, 0, 5000  
* **float (Floating-Point Number):** Numbers that contain a decimal point.  
  * Examples: 10.5, \-3.14, 0.0, 2.718

\# You can check a variable's type with the type() function  
whole\_number \= 25  
decimal\_number \= 98.6

print(type(whole\_number))  \# Output: \<class 'int'\>  
print(type(decimal\_number)) \# Output: \<class 'float'\>

#### **b. Arithmetic Operators**

Python provides a full set of operators to perform mathematical calculations.

| Operator | Name | Example | Result |
| :---- | :---- | :---- | :---- |
| \+ | Addition | 5 \+ 3 | 8 |
| \- | Subtraction | 5 \- 3 | 2 |
| \* | Multiplication | 5 \* 3 | 15 |
| / | Division | 5 / 3 | 1.666... |
| // | Floor Division | 5 // 3 | 1 (discards remainder) |
| % | Modulo | 5 % 3 | 2 (returns remainder) |
| \*\* | Exponent | 5 \*\* 3 | 125 (5 to the power of 3\) |

#### **c. The Problem with input() and the Solution: Type Conversion**

The input() function is great, but it has one important characteristic: **it always returns a string.**

user\_number \= input("Enter a number: ")  
print(type(user\_number)) \# Output: \<class 'str'\>

\# This will cause an error\! You can't add a number to a string.  
\# result \= user\_number \+ 5  \# TypeError: can only concatenate str (not "int") to str

To perform math, we must convert the string from the user into a numeric type. This is called **Type Conversion** or **Type Casting**.

* int(value): Converts value to an integer. Will cause an error if the value has a decimal.  
* float(value): Converts value to a float. This is usually safer for user input that might be a decimal.

\# Correct way to handle numeric input  
user\_input \= input("Enter a number: ")  
number\_as\_float \= float(user\_input) \# Convert the string to a float  
result \= number\_as\_float \+ 5  
print(f"Your number plus 5 is: {result}")

### **2\. Warm-Up Exercises**

Create a new file called day02\_exercises.py to practice these concepts.

#### **Exercise 1: Area of a Rectangle**

Write a script that asks the user for the width and height of a rectangle, then calculates and prints the area.

#### **Exercise 2: Tip Calculator**

Write a script that asks for the total bill amount and the percentage of the tip they'd like to leave (e.g., 15 for 15%). Calculate and print the tip amount and the total bill including the tip.

#### **Exercise 3: Seconds Converter**

Write a script that asks the user for a number of minutes and converts it into the equivalent number of seconds.

### **3\. Daily Project: Simple Calculator**

Now, let's combine these concepts into a single project. You will build a calculator that takes two numbers and an operator from the user to produce a result.

* **Project Goal:** The script will ask for two numbers and an operator (+, \-, \*, /) and print the result of the calculation.  
* **File Name:** calculator.py  
* **Save Location:** \~/python-practice-25-26/Part 1 \- Python Core Fundamentals/D02 \- Simple Calculator/calculator.py

#### **Instructions for Your Terminal (Project Setup):**

\# Step 1: Navigate to your Part 1 directory  
cd \~/python-practice-25-26/"Part 1 \- Python Core Fundamentals"

\# Step 2: Create a directory for today's project  
mkdir "D02 \- Simple Calculator"

\# Step 3: Change into the new directory  
cd "D02 \- Simple Calculator"

\# Step 4: Create the Python file and the README for your project  
touch calculator.py  
touch README.md

#### **Project Implementation:**

1. Ask the user for the first number.  
2. Ask the user for the second number.  
3. Ask the user for the operator they want to use (+, \-, \*, or /).  
4. **Convert** the user's number inputs from strings to float.  
5. Use an if/elif/else statement to check which operator was entered.  
6. Based on the operator, perform the correct calculation.  
7. Print the result in a clear, readable format (e.g., "5.0 \+ 3.0 \= 8.0").  
8. If the user enters an invalid operator, print an error message.

#### **Finishing Up (Git Workflow):**

1. Write a README.md for this project explaining what it does.  
2. Navigate back to the main project root (\~/python-practice-25-26).  
3. Add, commit, and push your work to GitHub.

cd \~/python-practice-25-26  
git add .  
git commit \-m "Day 2: Completed Simple Calculator project"  
git push  
