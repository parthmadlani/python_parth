#WAP that A) stores correct password in a variable b) Ask user to enter his or her password c) Validate the two password 
password = 'parth'
text = str(input("Enter a password to check if its correct or not: "))
if text == "":
    print("Enter a password.")
elif text != password:
    print("Wrong password.")
else:
    print("Correct password.")