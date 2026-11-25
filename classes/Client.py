class Client:
     def __init__(self,id, nom, prenom, email): 
          self.id = id
          self.nom = nom
          self.prenom = prenom
          self.email = email

     def __str__(self):
          return f"Client: {self.id } , {self.nom} {self.prenom}, Email: {self.email}"