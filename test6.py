def vowels_number(word):
    nb_vowels = 0

    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            nb_vowels += 1

    return nb_vowels


word = input("Entrez un mot : ")
vowels_count = vowels_number(word)
print(f"Il y a {vowels_count} voyelles dans le mot {word}")
