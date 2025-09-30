
a = int(input("Enter your age: "))
print(a)
if a < 18:
    print("Sorry, You are too young for this!!")
if a >= 18:
    print("Yup, You can go ahead")
Username = str(input("Whats ur name?"))
if len(Username) < 4: 
  print("Name is too short!")
if len(Username) > 20:
    print("Name is too long!")

print("loading...")
Password = str(input("Set your password: "))
if len(Password) < 6:
    print("Password is too short!")
Confirm_password = input("Please re-enter your password: ")
if Password != Confirm_password:
    print("Incorrect password")
if Password == Confirm_password:
    print("You are logged in successfully")
    print("Welcome", Username)
    print("loading...")
    print("You have successfully created your account")
    print("Thank you for registering", Username)

print("You can now login to your account")
Login_username = str(input("Enter your username: "))
Login_password = str(input("Enter your password: "))
if Login_username != Username:
    print("Username not found")
if Login_username == Username:
    if Login_password != Password:
        print("Incorrect password")
    if Login_password == Password:
        print("You are logged in successfully")
        print("Welcome back", Username)

Experience = input("So, how was your experience with us? ")
print("Thank you for your valuable feedback")
if len(Experience) < 10:
    print("Please elaborate your feedback")
if len(Experience) >= 10:
    print("Thank you for your detailed feedback")
print("Have a nice day ahead", Username)

# This is a simple user registration and login system with basic validations.
# It checks for age, username length, password strength, and confirms password match.
# It also includes a feedback section at the end.
# The program provides appropriate messages based on user input and validation results.

website = input("Do you want to visit our website? (yes/no): ")
if website.lower() == "yes":
    print("Redirecting to our website...")
    print("https://godofentities.odoo.com")
if website.lower() == "no":
    print("Thank you for using our service. Goodbye!")