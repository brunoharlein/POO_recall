# Le décorateur @classmethod peut être appliqué à n'importe quelle méthode d'une classe.
# Ce décorateur nous permettra d'appeler cette méthode en utilisant le nom de classe au lieu de l'objet.

class Person:
    totalObjects=0
    def __init__(self):
        Person.totalObjects=Person.totalObjects+1

    @classmethod
    def showcount(cls):
        print("Total objects: ",cls.totalObjects)

# Dans l'exemple ci-dessus, @classmethod est appliqué à la showcount()méthode.
# La showcount()méthode a un paramètre cls, qui fait référence à la classe personne.
# Maintenant, nous pouvons appeler la showcount()méthode en utilisant le nom de classe, comme indiqué ci-dessous.

p1 = Person() # totalObjects=1
print(Person.totalObjects)
p2 = Person() # totalObjects=2
print(Person.totalObjects)
p3 = Person() # totalObjects=3
print(Person.totalObjects)
p4 = Person() # totalObjects=4
print(Person.totalObjects)
p5 = Person()
print(Person.totalObjects)
p6 = Person()
print(Person.totalObjects)

Person.showcount()



# cls implique que la méthode appartient à la classe tandis que self implique que la méthode
# est liée à l'instance de la classe, donc le membre avec cls est accessible par le nom de la classe
# alors que celui avec self est accessible par l'instance de la classe ...
# c'est le même concept comme static memberet non-static membersen java si vous êtes d'origine java.
