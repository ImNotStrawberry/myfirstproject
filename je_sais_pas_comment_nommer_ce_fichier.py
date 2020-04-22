max = int(input("Entrez la limite : "))
num = int(input("Entrez un nombre de départ : "))
mult = int(input("Entrez le nombre par lequel vous souhaitez multiplier : "))
print(num)

while num < max:
    num *= mult
    print(num)
