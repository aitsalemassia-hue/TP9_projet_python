
import mysql.connector

from classes.Produit import Produit
from classes.Client import Client


class MySQLDAO:

     def __init__(self):
          self.conn = mysql.connector.connect(
               host="localhost",
               user="root",
               password="Assiyamysql",
               database="boutique"
          )

          self.cursor = self.conn.cursor()

          print("Connexion MySQL réussie !")

     # Ajouter un produit
     def ajouter_produit(self, produit):
          sql = "INSERT INTO Produit (nom, prix, quantite) VALUES (%s, %s, %s)"
          valeurs = (produit.nom, produit.prix, produit.quantite)

          self.cursor.execute(sql, valeurs)
          self.conn.commit()

     # Lister les produits
     def lister_produits(self):
          self.cursor.execute("SELECT * FROM Produit")
          lignes = self.cursor.fetchall()

          return [
               Produit(id, nom, prix, quantite)
               for id, nom, prix, quantite in lignes
          ]

     # Modifier le prix
     def modifier_prix(self, id, nouveau_prix):
          sql = "UPDATE Produit SET prix = %s WHERE id = %s"
          self.cursor.execute(sql, (nouveau_prix, id))
          self.conn.commit()

     # Ajouter un client
     def ajouter_client(self, client):
          sql = "INSERT INTO Client (id,nom,prenom,email) VALUES (%s, %s, %s, %s)"
          valeurs = (client.id, client.nom, client.prenom, client.email)

          self.cursor.execute(sql, valeurs)
          self.conn.commit()

     # Lister les clients
     def lister_clients(self):
          self.cursor.execute("SELECT * FROM Client")
          lignes = self.cursor.fetchall()

          return [
               Client(id, nom, prenom, email)
               for id, nom, prenom, email in lignes
          ]

     # Rechercher un client par email
     def rechercher_client(self, email):
          sql = "SELECT * FROM Client WHERE email = %s"
          self.cursor.execute(sql, (email,))

          ligne = self.cursor.fetchone()

          if ligne:
               return Client(ligne[0], ligne[1], ligne[2], ligne[3])

          return None

     # Fermer la connexion
     def fermer(self):
          self.cursor.close()
          self.conn.close()
