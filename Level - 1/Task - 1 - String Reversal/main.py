def reversed_string(word):

    reversed_word = word[::-1]
    return reversed_word

text = input("Enter text : ")

result = reversed_string(text)

print("Reversed String : ", result)

