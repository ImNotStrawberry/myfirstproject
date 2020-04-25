print("/!\ Séparez les notes par des espaces et remplacez les virgules par des points /!\ ")
notes = input("Entrez vos notes : ").split()

notes = [float(i) for i in notes]

result = sum(notes) / len(notes)
print(result)
