

while True:
    act_username="sarala"
    act_password="asd#123"
    username=input("Enter the username:")
    password=input("Enter the password:")
    if username==act_username and password==act_password :
        print("Logged in")
        break
    else:
        print("Invalid username and password")