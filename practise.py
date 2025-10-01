
a = int(input("Enter your age: "))
print(a)
if a < 18:
    print("Sorry, You are too young for this!!")
    exit()
else:
    print("Yup, You can go ahead")

# Username input with retry
while True:
    Username = str(input("Whats ur name? "))
    if len(Username) < 4:
        print("Name is too short! Try again.")
        continue
    if len(Username) > 20:
        print("Name is too long! Try again.")
        continue
    break

print("loading...")
# Password input with retry
while True:
    Password = str(input("Set your password: "))
    if len(Password) < 6:
        print("Password is too short! Try again.")
        continue
    Confirm_password = input("Please re-enter your password: ")
    if Password != Confirm_password:
        print("Incorrect password. Try again.")
        continue
    break

print("You are logged in successfully")
print("Welcome", Username)
print("loading...")
print("You have successfully created your account")
print("Thank you for registering", Username)


print("You can now login to your account")
# Login with retry
while True:
    Login_username = str(input("Enter your username: "))
    if Login_username != Username:
        print("Username not found. Try again.")
        continue
    Login_password = str(input("Enter your password: "))
    if Login_password != Password:
        print("Incorrect password. Try again.")
        continue
    print("You are logged in successfully")
    print("Welcome back", Username)
    break


# Feedback with retry
while True:
    Experience = input("So, how was your experience with us? ")
    print("Thank you for your valuable feedback")
    if len(Experience) < 10:
        print("Please elaborate your feedback. Try again.")
        continue
    if len(Experience) >= 10:
        print("Thank you for your detailed feedback")
        break
print("Have a nice day ahead", Username)

# This is a simple user registration and login system with basic validations.
# It checks for age, username length, password strength, and confirms password match.
# It also includes a feedback section at the end.
# The program provides appropriate messages based on user input and validation results.

# Website prompt with retry
while True:
    website = input("Do you want to visit our website? (yes/no): ")
    if website.lower() == "yes":
        print("Redirecting to our website...")
        print("https://godofentities.odoo.com")
        break
    elif website.lower() == "no":
        print("Thank you for using our service. Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'. Try again.")