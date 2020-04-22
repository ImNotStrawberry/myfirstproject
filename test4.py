from random import shuffle

text = input("Entrez des mots au hasard : ").split()
num  = len(text)
print(f"Votre liste contient {num} mots")
shuffle(text)
if num < 10:
    print("La liste a été mélangée.")
    print("Voici les deux premiers termes de cette liste : "
          f"{text[0]}, {text[1]}")
else:
    print("Voici les trois derniers termes cette liste : "
          f"{text[-2]}, {text[-3]}")
