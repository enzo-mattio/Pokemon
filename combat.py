'''
1. Créer la classe "Pokemon" avec les attributs privés "nom" et "point de vie", et les attributs publics "niveau", "puissance d'attaque", "défense" et "type". Ajouter des méthodes pour initialiser les attributs, afficher les informations du Pokémon et sauvegarder les informations du Pokémon dans un fichier JSON.

  
2. Créer les classes héritées de la classe "Pokemon" pour chaque type de Pokémon (Normal, Feu, Eau, Terre, etc.), en modifiant les attributs en fonction du type. Ajouter des méthodes pour calculer les dégâts infligés en fonction du type de l'attaquant et du défenseur.


3.  Créer la classe "Combat" pour gérer les combats entre deux Pokémon. Ajouter des méthodes pour vérifier si un Pokémon est encore en vie, choisir aléatoirement si un Pokémon attaque ou non, calculer les dégâts infligés, enlever des points de vie en fonction de la défense, déterminer le vainqueur et sauvegarder le Pokémon rencontré dans le Pokédex.


4.  Créer un menu pour lancer une partie, ajouter un nouveau Pokémon ou accéder au Pokédex. Permettre au joueur de choisir son Pokémon de départ.

  
5.  Intégrer toutes les classes et méthodes pour permettre au joueur de combattre un Pokémon choisi aléatoirement à partir d'un fichier JSON.


6.  Ajouter des fonctionnalités supplémentaires telles que l'ajout de nouveaux types de Pokémon, la mise à niveau des Pokémon et l'amélioration de l'interface utilisateur.'''
import random

class Combat:
  def __init__(self, pokemon1, pokemon2):
    self.pokemon1 = pokemon1
    self.pokemon2 = pokemon2
  def est_en_vie(self, pokemon):
    if pokemon.get_point_de_vie() > 0:
      return True
    else:
      return False
  def attaque(self, pokemon1, pokemon2):
    if random.randint(0, 1) == 0:
      pokemon2.set_point_de_vie(pokemon2.get_point_de_vie() - pokemon1.puissance_attaque)
    else:
      pokemon1.set_point_de_vie(pokemon1.get_point_de_vie() - pokemon2.puissance_attaque)
  def calculer_degats(self, pokemon1, pokemon2):
    if pokemon1.type == "feu" and pokemon2.type == "eau":
      return pokemon1.puissance_attaque * 0.5
    elif pokemon1.type == "feu" and pokemon2.type == "terre":
      return pokemon1.puissance_attaque * 2
    elif pokemon1.type == "eau" and pokemon2.type == "feu":
      return pokemon1.puissance_attaque * 2
    elif pokemon1.type == "eau" and pokemon2.type == "terre":
      return pokemon1.puissance_attaque * 0.5
    elif pokemon1.type == "terre" and pokemon2.type == "feu":
      return pokemon1.puissance_attaque * 0.5
    elif pokemon1.type == "terre" and pokemon2.type == "eau":
      return pokemon1.puissance_attaque * 2
    elif pokemon1.type == "normal" and pokemon2.type != "normal":
      return pokemon1.puissance_attaque * 0.75
    else:
      return pokemon1.puissance_attaque