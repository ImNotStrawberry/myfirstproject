from random import randint

just_price = randint(1, 999)
run = True

while run:
    price = int(input("Entrez un nombre : "))
    if price == just_price:
        print("Félicitations !")
        run = False
    elif price > just_price:
        print("Trop haut")
    elif price < just_price:
        print("Trop bas")

print("Fin du jeu")
