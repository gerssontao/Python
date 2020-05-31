# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord=input("Enter a Word: ")
userWord=userWord.upper()
unEatenLetter=[]
wordWithoutVovels=''


for letter in userWord:
    # Complete the body of the for loop.
    if (letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
        continue
    unEatenLetter.append(letter)
    wordWithoutVovels= wordWithoutVovels+letter
    print(letter)
print(unEatenLetter)
print(wordWithoutVovels)