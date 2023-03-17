from combat import *
from pokemon import *


if input("Voulez-vous voir les Pokemon disponible ? (O/N) ").lower() == "o":
    print("\nVoici la liste des Pokemon disponible : \n")
    for i in pokemon:
        print(f"{i} : {pokemon[i]['type'].upper()} \n{separator}")

Pokemon1 = Pokemon(input("Entrez le nom de votre pokemon : "))
Pokemon2 = Pokemon(input("Entrez le nom du pokemon adverse: "))


Combat1 = Combat(Pokemon1, Pokemon2)

Combat1.combat()
