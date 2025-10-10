
#ex1

#version1
# day_of_the_week= input("Choose a day of the week: ").lower()

# if day_of_the_week == "monday":
#     print("it is a weekday")
# elif day_of_the_week == "tuesday":
#     print("it's the weekday")
#
# elif day_of_the_week == "wednesday":
#     print("it's the weekday")
# elif day_of_the_week == "thursday":
#     print("it's the weekday")
# elif day_of_the_week == "friday":
#     print("it's the weekday")
#
# elif day_of_the_week == "saturday":
#     print("it's the weekend")
#
#
# elif day_of_the_week == "sunday":
#     print("it's the weekend")
#
# else:
#     print("Error: please type the day of the week correctly")


#shorter version

# if (day_of_the_week =="monday") | (day_of_the_week =="tuesday")  | (day_of_the_week =="wednesday")  | (day_of_the_week =="thursday") | (day_of_the_week =="friday"):
#     print("it's the weekday")
# elif (day_of_the_week =="saturday") | (day_of_the_week =="sunday"):
#     print("it's the weekend")
#


# age = int(input("What is your age: "))
#
#
# if age > 65:
#     price = 7
#
#
# elif (age <=65) & (age >= 12):
#     price = 12
#
# else:
#     price = 5
#
#
# print(f"Your ticket price is  ${price}")

#ex 3

password_typed = input("Please type your password: \n")

if password_typed == "python123":
    print("Login successful.")
else:
    print("Password is incorrect, please try again.")

