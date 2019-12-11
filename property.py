# _name = attribut protégé / __name = attribut privé
class Person:
    def __init__(self):
        self.__name=""
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value

p = Person()
p.name = "Steve"
print(p.name)

# La classe Person ci dessus comprend deux méthodes portant le même nom name(),
# mais avec un nombre différent de paramètres. C'est ce qu'on appelle la surcharge de méthode.
# La methode name(self) est marquée avec le décorateur @property
# qui indique que la methode name(self) est une méthode getter et que le nom de la propriété
# est uniquement le nom de la méthode, dans ce cas name.
# Maintenant, name(self, value) attribue une valeur à l'attribut privé __name.
# Ainsi, pour marquer cette méthode comme méthode de définition de la propriété name,
# le décorateur @name.setter est appliqué. C'est ainsi que nous pouvons définir
# une propriété et ses méthodes getter et setter.


class Apertura:
    createur = "Christian Yvon"
    nbs_voies = 2

    def __init__(self):
        self.__name=""
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value

hp = Apertura()
hp.name = "tanagra"
print(hp.name)
