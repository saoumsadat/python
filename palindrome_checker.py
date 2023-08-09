str = input("Enter string: ");

def word_refiner(word):
    #turning every char into lowercase
    word_lowered = word.lower();
    refined_word = "";

    #iterating through every character
    for char in word_lowered:

        #adding if the character is a letter
        if char >= "a" and char <= "z":
            refined_word += char;

    return refined_word;

word_final = word_refiner(str);

def palindrome_checker(word_final):
    is_palindrome = True;

    for x in range(0, int(len(word_final) / 2)):
        if word_final[x] != word_final[(len(word_final) - 1) - x]:
            is_palindrome = False;

    if is_palindrome:
        return "This is a palindrome"
    else:
        return "This is not a palindrome"

print(palindrome_checker(word_final))
