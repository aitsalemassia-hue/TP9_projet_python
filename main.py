
from classes.Produit import Produit
from classes.Client import Client

from  baseDonnees.sqlite import SQLiteDAO
from baseDonnees.MySQL import MySQLDAO


     # 1. Choisir la base de données
def choisir_base():

     print("\n      CHOIX DE LA BASE     ")
     print("1. SQLite")
     print("2. MySQL")

     choix = input("Votre choix : ")

     try:
          if choix == "1":
               dao = SQLiteDAO()
               print("Connexion SQLite réussie !")
               return dao

          elif choix == "2":
               dao = MySQLDAO()
               print("Connexion MySQL réussie !")
               return dao

          else:
               print("Choix invalide !")
               return None

     except Exception as e:
          print("Erreur de connexion :", e)
          return None


# 2. Afficher le menu principal
def afficher_menu():

     print("\n      GESTION BOUTIQUE     ")
     print("1. Ajouter un produit")
     print("2. Lister la liste des produits")
     print("3. Modifier le prix d'un produit")
     print("4. Ajouter un client")
     print("5. Lister la liste des clients")
     print("6. Rechercher un client par email")
     print("0. Quitter")

     return input("Votre choix : ")


 # 3. Programme principal
def main():

     dao = choisir_base()

     if dao is None:
          return

     while True:

          choix = afficher_menu()

          try:

               # Ajouter un produit
               if choix == "1":
                    nom = input("Nom du produit : ")
                    prix = float(input("Prix du produit : "))
                    quantite = int(input("Quantité du produit : "))
                    

                    produit = Produit( nom, prix, quantite)
                    dao.ajouter_produit(produit)

                    print("Produit ajouté avec succès !")

               # Lister les produits
               elif choix == "2":
                    produits = dao.lister_produits()

                    print("\n LISTE DES PRODUITS ")

                    for p in produits:
                         print(p)

               # Modifier le prix
               elif choix == "3":
                    id = int(input("ID du produit : "))
                    prix = float(input("Nouveau prix : "))

                    dao.modifier_prix(id, prix)

                    print("Prix modifié avec succès !")

               # Ajouter un client
               elif choix == "4":
                    id = int(input("ID du client : "))
                    nom = input("Nom du client : ")
                    prenom = input("Prénom du client : ")
                    email = input("Email du client : ")
                    

                    client = Client(id, nom, email, prenom)
                    dao.ajouter_client(client)

                    print("Client ajouté avec succès !")

               # Lister les clients
               elif choix == "5":
                    clients = dao.lister_clients()

                    print("\n LISTE DES CLIENTS ")

                    for c in clients:
                         print(c)

               # Rechercher un client
               elif choix == "6":
                    email = input("Email à rechercher : ")

                    client = dao.rechercher_client(email)

                    if client:
                         print("Client trouvé :", client)
                    else:
                         print("Aucun client trouvé !")

               # Quitter
               elif choix == "0":
                    print("Au revoir !")
                    break

               else:
                    print("Choix invalide !")

          except ValueError:
               print("Erreur : veuillez saisir une valeur valide.")

          except Exception as e:
               print("Erreur :", e)

     dao.fermer()


if __name__ == "__main__":
     main()
