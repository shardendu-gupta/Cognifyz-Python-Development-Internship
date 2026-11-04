def check_palindrome(word):
    reverse = word[::-1]

    if word == reverse:
        return True
    else:
        return False


word = input("Enter a word: ").lower()

if check_palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")
