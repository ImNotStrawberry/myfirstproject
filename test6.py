def num_vowels(word):
    vowels = 0

    for letter in word:
        if letter = ['a', 'e', 'i', 'o', 'u', 'y']:
            vowels += 1

    return vowels


word = input("Entrez un mot : ")
nb = num_vowels(word)
print(f"Il y a {nb} dans le mot {word}")
