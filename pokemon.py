
'''
1. Créer la classe "Pokemon" avec les attributs privés "nom" et "point de vie", et les attributs publics "niveau", "puissance d'attaque", "défense" et "type". Ajouter des méthodes pour initialiser les attributs, afficher les informations du Pokémon et sauvegarder les informations du Pokémon dans un fichier JSON.

  
2. Créer les classes héritées de la classe "Pokemon" pour chaque type de Pokémon (Normal, Feu, Eau, Terre, etc.), en modifiant les attributs en fonction du type. Ajouter des méthodes pour calculer les dégâts infligés en fonction du type de l'attaquant et du défenseur.


3.  Créer la classe "Combat" pour gérer les combats entre deux Pokémon. Ajouter des méthodes pour vérifier si un Pokdef mon est encore en vie, choisir aléatoirement si un Pokémon attaque ou non, calculer les dégâts infligés, enlever des points de vie en fonction de la défense, déterminer le vainqueur et sauvegarder le Pokémon rencontré dans le Pokédex.


4.  Créer un menu pour lancer une partie, ajouter un nouveau Pokémon ou accéder au Pokédex. Permettre au joueur de choisir son Pokémon de départ.

  
5.  Intégrer toutes les classes et méthodes pour permettre au joueur de combattre un Pokémon choisi aléatoirement à partir d'un fichier JSON.


6.  Ajouter des fonctionnalités supplémentaires telles que l'ajout de nouveaux types de Pokémon, la mise à niveau des Pokémon et l'amélioration de l'interface utilisateur.'''

# path: pokemon.py
import json
import json

with open("attaques.json", "r") as fichier:
    attaques = json.load(fichier)
with open("type.json", "r") as fichier:
    type = json.load(fichier)
with open("pokedex.json", "r") as fichier:
    pokemon = json.load(fichier)
separator = "----------------------------------------"

class Pokemon:
  def __init__(self, nom):

    self.__nom = nom
    self.__point_de_vie = pokemon[self.__nom]["pv"]
    self.puissance_attaque = pokemon[self.__nom]["attaque"]
    self.defense = pokemon[self.__nom]["defense"]
    self.type = pokemon[self.__nom]["type"]
    self.Id = pokemon[self.__nom]["ID"]
    self.niveau = pokemon[self.__nom]["niveau"]
  def __str__(self):
    return f"ID: {self.Id} \nNom: {self.__nom}\nPoint de vie: {self.__point_de_vie}\nPuissance d'attaque: {self.puissance_attaque}\nDéfense: {self.defense}\nType: {self.type}"

  def get_nom(self):
    return self.__nom

  def get_point_de_vie(self):
    return self.__point_de_vie

  def set_nom(self, nom):
    self.__nom = nom

  def get_attaques(self):
    return attaques[self.__nom]

  def set_point_de_vie(self, point_de_vie):
    self.__point_de_vie = point_de_vie

  def sauvegarder(self):
    with open("pokedex.json", "w") as fichier:
      json.dump(self.__dict__, fichier)
        
  def get_type(self):
    return self.type