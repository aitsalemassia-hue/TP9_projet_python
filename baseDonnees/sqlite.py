
import sqlite3

class SQLiteDAO:

     def __init__(self):
          self.conn = sqlite3.connect("boutique.db")
          self.cursor = self.conn.cursor()
          self.creer_tables()

     def creer_tables(self):
          self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS Produit (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prix REAL NOT NULL
               )
          """)

          self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS Client (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
               )
          """)

          self.conn.commit()

     def ajouter_produit(self, produit):
          self.cursor.execute(
               "INSERT INTO Produit(nom, prix) VALUES (?, ?)",
               (produit.nom, produit.prix)
          )
          self.conn.commit()

     def lister_produits(self):
          self.cursor.execute("SELECT * FROM Produit")
          return self.cursor.fetchall()

     def modifier_prix(self, id, nouveau_prix):
          self.cursor.execute(
               "UPDATE Produit SET prix = ? WHERE id = ?",
               (nouveau_prix, id)
          )
          self.conn.commit()

     def ajouter_client(self, client):
          self.cursor.execute(
               "INSERT INTO Client(nom, email) VALUES (?, ?)",
               (client.nom, client.email)
          )
          self.conn.commit()

     def lister_clients(self):
          self.cursor.execute("SELECT * FROM Client")
          return self.cursor.fetchall()

     def rechercher_client(self, email):
          self.cursor.execute(
               "SELECT * FROM Client WHERE email = ?",
               (email,)
          )
          return self.cursor.fetchone()

     def fermer(self):
          self.conn.close()
