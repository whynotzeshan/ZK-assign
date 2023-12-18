# 1. Prompt user for their name
user_name = input("Enter your name: ")

# 2. Concatenate name with "Hello, " and print
greeting = "Hello, " + user_name
print(greeting)

# 3. Ask user for age and convert to integer
user_age = int(input("Enter your age: "))

# 4. Add 5 to user's age and print the result
new_age = user_age + 5
print(f"Your age plus 5 is: {new_age}")

# 5. Create a list of three favorite colors
favorite_colors = ["blue", "green", "red"]

# 6. Ask user to enter a new color and append to the list
new_color = input("Enter a new color: ")
favorite_colors.append(new_color)

# 7. Print the final list of favorite colors
print("Your favorite colors:", favorite_colors)
