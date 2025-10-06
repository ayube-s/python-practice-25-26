#ask for 1st name

first_number = float(input("Give the first number: "))

second_number = float(input("Give the second number: "))

operator = input("What operator would you like to use? type * for multiplication, + for addition , - for subtraction, / for division \n")

if operator == "*":
    total= first_number * second_number
    print(f"{first_number}  {operator} {second_number}  = {total}")


elif operator == "+":
    total= first_number + second_number
    print(f"{first_number}  {operator} {second_number}  = {total}")

elif operator == "-":
    total= first_number - second_number
    print(f"{first_number}  {operator} {second_number}  = {total}")

elif operator == "/":
    total = first_number / second_number
    print(f"{first_number}  {operator} {second_number}  = {total}")

else:
    print("Error: Please use one of the 4 operators listed.")





