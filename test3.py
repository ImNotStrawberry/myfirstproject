age = int(input("Entrez votre age : "))

if age >= 18:
    price = 12
else:
    price = 7

print(f"La place de cinéma coute {price}€")

popcorn = input("Souhaitez-vous du popcorn ? [Oui/Non] ")

if popcorn.startswith("o"):
    price += 5
    print(f"Vous allez payer {price}€")
elif popcorn.startswith("n"):
    print(f"Vous allez payer {price}€")
else:
    print("Erreur")

