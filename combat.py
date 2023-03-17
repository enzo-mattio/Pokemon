'''
1. Créer la classe "Pokemon" avec les attributs privés "nom" et "point de vie", et les attributs publics "niveau", "puissance d'attaque", "défense" et "type". Ajouter des méthodes pour initialiser les attributs, afficher les informations du Pokémon et sauvegarder les informations du Pokémon dans un fichier JSON.

  
2. Créer les classes héritées de la classe "Pokemon" pour chaque type de Pokémon (Normal, Feu, Eau, Terre, etc.), en modifiant les attributs en fonction du type. Ajouter des méthodes pour calculer les dégâts infligés en fonction du type de l'attaquant et du défenseur.


3.  Créer la classe "Combat" pour gérer les combats entre deux Pokémon. Ajouter des méthodes pour vérifier si un Pokémon est encore en vie, choisir aléatoirement si un Pokémon attaque ou non, calculer les dégâts infligés, enlever des points de vie en fonction de la défense, déterminer le vainqueur et sauvegarder le Pokémon rencontré dans le Pokédex.


4.  Créer un menu pour lancer une partie, ajouter un nouveau Pokémon ou accéder au Pokédex. Permettre au joueur de choisir son Pokémon de départ.

  
5.  Intégrer toutes les classes et méthodes pour permettre au joueur de combattre un Pokémon choisi aléatoirement à partir d'un fichier JSON.


6.  Ajouter des fonctionnalités supplémentaires telles que l'ajout de nouveaux types de Pokémon, la mise à niveau des Pokémon et l'amélioration de l'interface utilisateur.'''

import time
import random
from pokemon import *


class Combat(Pokemon):
  def __init__(self, attaquant, defenseur):
    self.attaquant = attaquant
    self.defenseur = defenseur
  

    
  def combat(self):
    print(f"Le combat commence entre {self.attaquant.get_nom()} et {self.defenseur.get_nom()} ! \n{separator}")
    # Presentation des pokemons
    print(f"{self.attaquant.get_nom()} : \n{self.attaquant} \n{separator}")
    print(f"{self.defenseur.get_nom()} : \n{self.defenseur} \n{separator}")
    while self.est_en_vie(self.attaquant) and self.est_en_vie(self.defenseur):
      self.attaque(self.attaquant, self.defenseur)
      time.sleep(1)
      if self.est_en_vie(self.defenseur):
        self.attaque(self.defenseur, self.attaquant)
      time.sleep(1)

    self.vainqueur(self.attaquant, self.defenseur)

  def est_en_vie(self, pokemon):
    if pokemon.get_point_de_vie() > 0:
      return True
    else:
      return False
  
  def baisser_pp(self,attaquant,attaque):
    attaque_restante = attaques[attaquant.get_nom()][attaque]["pp"]
    
    attaque_restante -= 1
    return attaque_restante
  # def verifier_attaque(self, verif):
  #   while verif:
  #       choix_attaque = int(input('Choisissez une attaque (1-4) : '))
  #       if not (1 <= choix_attaque <= 4):
  #           print("Choix invalide. Veuillez choisir un nombre entre 1 et 4.")
  #       else:
  #           verif = False
  #   return choix_attaque

  def attaque(self, attaquant, defenseur):
    

    # Vérification que l'attaquant a des attaques disponibles
    if attaquant.get_nom() not in attaques:
      raise ValueError(f"{attaquant.get_nom()} n'a aucune attaque disponible.")

    # Affichage des attaques disponibles
    print(f"Choisissez une attaque :  \n{separator}")
    
    attaques_disponibles = attaques[attaquant.get_nom()]
    
    for i, attaque in enumerate(attaques_disponibles):
      
      puissance = attaques_disponibles[attaque]['puissance']
      precision = attaques_disponibles[attaque]['precision']
      type_attaque = attaques_disponibles[attaque]['type']
      
      print(f"{i+1}. {attaque}: \n  {puissance} puissance d'attaque \n  Précision: {precision} \n  Type: {type_attaque} \n{separator}")

    check=True
    
    while check:
      choix_attaque = input('Choisissez une attaque (1-4) : ')
      if choix_attaque in '1234':
        # Calcul des dégâts et affichage
        choix_attaque = int(choix_attaque) - 1
        nom_attaque = list(attaques_disponibles.keys())[choix_attaque]
        
        degats = self.calculer_degats(attaquant, defenseur, nom_attaque)
        if self.baisser_pp(attaquant,nom_attaque) > 0:
          if random.randint(0, 100) <= attaques_disponibles[nom_attaque]['precision']:
            print(f"{separator}\n{attaquant.get_nom()} utilise {nom_attaque} !")
          
            defenseur.set_point_de_vie(defenseur.get_point_de_vie() - degats)
            
            print(f"{attaquant.get_nom()} inflige {degats} dégâts à {defenseur.get_nom()} \n{separator}")
            
            print(f"{attaquant.get_nom()} a encore {self.baisser_pp(attaquant,nom_attaque)} {nom_attaque} possible \n{separator}")
            print(self.voir_efficacite(attaquant, defenseur,nom_attaque))
            
            print(f"{defenseur.get_nom()} a {defenseur.get_point_de_vie()} points de vie \n{separator}")
          else:
            print(f"{attaquant.get_nom()} a raté son attaque ! \n{separator}")
          
          check=False
      else:
        print("Choix invalide. Veuillez choisir un nombre entre 1 et 4.")
        continue
      
      
      

  
  def calculer_degats(self, attaquant, defenseur, attaque):

    niveau = attaquant.niveau
    attaque_attaquant = attaquant.puissance_attaque
    defense_defenseur = defenseur.defense
    puissance_attaque = attaques[attaquant.get_nom()][attaque]["puissance"]
    type_attaque = attaques[attaquant.get_nom()][attaque]["type"]
      
    
    return int(((((((2 * int(niveau)) // 5) + 2) * int(attaque_attaquant) * int(puissance_attaque)) // int(defense_defenseur)) // 50) + 2) * self.calculer_CM(defenseur, type_attaque)

  def voir_efficacite(self, attaquant, defenseur, attaque):
    
    type_attaque = attaques[attaquant.get_nom()][attaque]["type"]
      # Affichage Efficacité
    if self.calculer_CM(defenseur, type_attaque) == 0.5:
      return "Ce n'est pas très efficace..."
    elif self.calculer_CM(defenseur, type_attaque) == 2:
      return "C'est super efficace !"
    else:
      return "C'est efficace !"

  def calculer_CM(self, defenseur, attaque):
      
    type_defenseur = defenseur.type
    type_attaque = attaque
    faible = type[type_attaque]["faible"]
    fort = type[type_attaque]["fort"]

    if type_defenseur in faible:
      return 0.5
    elif type_defenseur in fort:
      return 2
    else:
      return 1
           
  def vainqueur(self, attaquant, defenseur):
  
    if self.est_en_vie(attaquant):
      print(f"{attaquant.get_nom()} a gagné !")
    else:
      print(f"{defenseur.get_nom()} a gagné !")