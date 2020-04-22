num = int(input("Entrez un nombre de départ : "))
mult = int(input("Entrez le nombre par lequel vous souhaitez multiplier : "))
max = int(input("Entrez la limite : "))

print(num)

while num < max:
    num *= mult
    print(num)
