
'''
1. Créer la classe "Pokemon" avec les attributs privés "nom" et "point de vie", et les attributs publics "niveau", "puissance d'attaque", "défense" et "type". Ajouter des méthodes pour initialiser les attributs, afficher les informations du Pokémon et sauvegarder les informations du Pokémon dans un fichier JSON.

  
2. Créer les classes héritées de la classe "Pokemon" pour chaque type de Pokémon (Normal, Feu, Eau, Terre, etc.), en modifiant les attributs en fonction du type. Ajouter des méthodes pour calculer les dégâts infligés en fonction du type de l'attaquant et du défenseur.


3.  Créer la classe "Combat" pour gérer les combats entre deux Pokémon. Ajouter des méthodes pour vérifier si un Pokdef mon est encore en vie, choisir aléatoirement si un Pokémon attaque ou non, calculer les dégâts infligés, enlever des points de vie en fonction de la défense, déterminer le vainqueur et sauvegarder le Pokémon rencontré dans le Pokédex.


4.  Créer un menu pour lancer une partie, ajouter un nouveau Pokémon ou accéder au Pokédex. Permettre au joueur de choisir son Pokémon de départ.

  
5.  Intégrer toutes les classes et méthodes pour permettre au joueur de combattre un Pokémon choisi aléatoirement à partir d'un fichier JSON.


6.  Ajouter des fonctionnalités supplémentaires telles que l'ajout de nouveaux types de Pokémon, la mise à niveau des Pokémon et l'amélioration de l'interface utilisateur.'''

# path: pokemon.py
import random
import json


class Pokemon:
  def __init__(self, nom, point_de_vie, niveau, puissance_attaque, defense, type):
    self.__nom = nom
    self.__point_de_vie = point_de_vie
    self.niveau = niveau
    self.puissance_attaque = puissance_attaque
    self.defense = defense
    self.type = type

  def get_nom(self):
    return self.__nom
  def get_point_de_vie(self):
    return self.__point_de_vie
  def set_nom(self, nom):
    self.__nom = nom
  def set_point_de_vie(self, point_de_vie):
    self.__point_de_vie = point_de_vie
  def afficher(self):
    print(f"Nom: {self.__nom}")
    print(f"Point de vie: {self.__point_de_vie}")
    print(f"Niveau: {self.niveau}")
    print(f"Puissance d'attaque: {self.puissance_attaque}")
    print(f"Défense: {self.defense}")
    print(f"Type: {self.type}")
  def sauvegarder(self):
    with open("pokemon.json", "w") as fichier:
      json.dump(self.__dict__, fichier)
      