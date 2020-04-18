def main():
    wallet = int(input("Argent possédé : "))
    product = 60
    wallet -= product
    print("Le jeu Animal Crossing New Horizons coûte 60€")
    print("Après achat, il vous reste " + str(wallet) + "€")


if __name__ == '__main__':
    main()
