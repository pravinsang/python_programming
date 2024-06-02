vowel = "aeiouAEIOU"
word = input("Enter a word")
for ch in word:
    if ch in vowel:
        print(f"{ch} is a vowel")
    else:
        print(f"{ch} is a consonant")