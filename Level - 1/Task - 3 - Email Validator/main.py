def validate_email(email):

    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    username = parts[0]
    domin = parts[1]

    if username == "" or domin == "":
        return False

    if "." not in domin:
        return False

    domin_parts = domin.rsplit(".", 1)

    if domin_parts[0] == "" or domin_parts[1] == "":
        return False
    
    return True

email = input("Enter your email : ")

if validate_email(email):
    print("Valid email address")

else:
    print("Invalid email address")


