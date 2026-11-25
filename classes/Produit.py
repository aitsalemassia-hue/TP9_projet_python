class Produit:
     def __init__(self, nom, prix, quantite): 
          self.nom = nom
          self.prix = prix
          self.quantite = quantite


     def __str__(self):
          return f"Produit: {self.nom}, Prix: {self.prix}, Quantité: {self.quantite}"