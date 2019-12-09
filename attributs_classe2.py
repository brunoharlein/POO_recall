class Test:
    a = "attribut de classe"

    def __init__(self):
        self.b = "attribut d'objet"

if __name__ == "__main__":
    attribut = Test ( )
    print(attribut.b)
    print(Test.a)

# Pour utiliser le(s) attribut(s) de classe,
# il est inutile de créer un objet de cette classe puisque l’attribut est une propriété de la classe
class Test1:
    a = "attribut de classe"

    def __init__(self):

        self.b = "attribut d'objet"

if __name__ == "__main__":
    print(Test1.a)
