# **Day 1: "Hello, World\!", Variables, and User Interaction**

Welcome to the official start of your 100-day challenge\! Today, we're covering the absolute bedrock of Python programming. By the end of this lesson, you'll be able to write a simple program that can display information, store data, and interact with a user.

### **1\. Key Concepts Explained**

#### **A. The print() function**

The print() function is the most basic way to display output to the console. You simply put the text or variable you want to display inside the parentheses. Text, which is called a **string** in programming, must be enclosed in quotes (" or ').

* **Example:**  
  print("Hello, Python\!")  
  print(123) \# You don't need quotes for numbers

#### **B. Variables**

A variable is like a labeled box where you can store a piece of information. You give it a name and assign a value to it using the equals sign (=).

* **Key Data Types for Today:**  
  * **String (str):** Plain text. Must be in quotes. e.g., "Ayube".  
  * **Integer (int):** A whole number. e.g., 10, 2025\.  
* **Example:**  
  name \= "Ayube"  
  project\_day \= 1  
  print("My name is:")  
  print(name)

#### **C. The input() function**

The input() function displays a prompt to the user and waits for them to type something and press Enter. The text the user types is then returned as a string, which you should store in a variable.

* **Example:**  
  user\_name \= input("Please enter your name: ")  
  print("Welcome to the challenge, " \+ user\_name)

#### **D. String Concatenation**

This is the term for joining strings together. You can use the plus sign (+) to combine strings and variables into a single, longer string.

* **Example:**  
  first\_name \= "Ayube"  
  last\_name \= "S"  
  full\_name \= first\_name \+ " " \+ last\_name  
  print(full\_name) \# This will print "Ayube S"

### **2\. Daily Exercises**

Before starting the project, try to solve these small challenges to solidify your understanding.

1. **Favorite Food:** Create a variable named favorite\_food and assign it your favorite food. Print it to the console.  
2. **Personal Info:** Create two variables, age (an integer) and hometown (a string). Print them in a single sentence like: "I am \[age\] years old and I am from \[hometown\]."  
3. **Simple Q\&A:** Write a script that asks the user "What is your quest?" and then prints back "Your quest is: \[user's answer\]".

### **3\. Daily Project: Personalized Greeting App**

Now, let's build today's project. The goal is to create a script that has a short conversation with the user.

* **Project Goal:** The script will ask for the user's name and favorite color, then print a personalized message.  
* **File Name:** greeter.py  
* Save Location: Your greeter.py file should be saved at the following full path:  
  \~/python-practice-25-26/Part 1 \- Python Core Fundamentals/D01 \- Greeter App/greeter.py

#### **Instructions for Your Terminal (Project Setup):**

Follow these steps exactly to create your project structure.

\# Step 1: Navigate to your Part 1 directory from your home folder  
cd \~/python-practice-25-26/"Part 1 \- Python Core Fundamentals"

\# Step 2: Create a directory for today's project (D01 for Day 01\)  
mkdir "D01 \- Greeter App"

\# Step 3: Change into the new directory  
cd "D01 \- Greeter App"

\# Step 4: Create the Python file and the README for your project  
touch greeter.py  
touch README.md

#### **Project Implementation:**

Open the greeter.py file you just created and write the Python code to do the following:

1. Print a welcome message.  
2. Use input() to ask for the user's name and store it in a variable.  
3. Use input() again to ask for their favorite color and store it in another variable.  
4. Use print() and string concatenation (+) to display a friendly message that includes both their name and favorite color.  
* **Example Output:**  
  Hello\! Welcome to the Personalized Greeter.  
  What is your name? Ayube  
  What is your favorite color? Blue  
  It's wonderful to meet you, Ayube\! Blue is a fantastic color.

#### **Finishing Up (Git Workflow):**

Once your script is working correctly:

1. Open the README.md file in the D01 \- Greeter App folder and write a brief description of what the project does.  
2. Return to your terminal and run these commands from the **main project root directory**.

\# Navigate back to the main project root  
cd \~/python-practice-25-26

\# Add all new files to Git's tracking  
git add .

\# Commit the changes with a descriptive message  
git commit \-m "Day 1: Completed Personalized Greeting App"

\# Push your new commit to your GitHub repository  
git push  
