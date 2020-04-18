age = int(input("Entrez votre age : "))

if age >= 18:
    price = 12
else:
    price = 7

print("La place de cinéma coute {}€".format(price))

popcorn = input("Souhaitez-vous du popcorn ? [Oui/Non] ")

if popcorn.startswith("o"):
    price += 5
    print("Vous allez payer {}€".format(price))
elif popcorn.startswith("n"):
    print("Vous allez payer {}€".format(price))
else:
    print("Erreur")
