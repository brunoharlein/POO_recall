class LeNomDeMaClasse:
    """“if __name__ == “__main__” :” pourrait se traduire par si ce programme
     est exécuté directement comme étant le principal (main), exécuter le code qui suit !
     Si vous devez déclarer des attributs de classe dits statiques
      ne devant donc pas changer ou devant être utilisés souvent et un peu partout dans le script.
      A ne pas confondre avec les attributs d’objets déclarés dans la méthode constructeur “__init__ ()”"""

    attribut_de_classe = "Ceci est une donnée : "

    def __init__(self):
        self.attribut_01 = "hello"
        self.attribut_02 = 346

    def methode_01(self):
        compteur = 1
        while compteur <= 5:
            print (compteur, " : ", self.attribut_01)
            compteur = compteur + 1

    def methode_02(self):
        compteur = 1
        addition = 0
        while compteur <= 5:
            print (compteur, " : ", self.attribut_02 + addition)
            compteur = compteur + 1
            addition = addition + 1

    def methode_03(self):
        print (LeNomDeMaClasse.attribut_de_classe, self.attribut_01)
        print (LeNomDeMaClasse.attribut_de_classe, self.attribut_02)

if __name__ == "__main__":
    print(LeNomDeMaClasse.attribut_de_classe)
    encore_un_objet = LeNomDeMaClasse()
    print ("Exécution de la méthode 03 : ")
    encore_un_objet.methode_03()
