word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
