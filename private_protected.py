# _name = attribut protégé / __name = attribut privé
# Tout est accessible en Python. Il n’y a pas de variables privées.
# On peut noter aussi qu’un from module import * n’importe pas les objets commençant par “_” ou “__”.
# Il faut le faire explicitement si on veut pouvoir les manipuler.
class Monique:
    """les devs savent qu’il faut éviter d’utiliser cette variable car
    elle ne fait pas partie de l’API publique de la classe, et l’implémentation pourrait changer plus tard.
    Comme self, c’est une convention forte puisque
    la plupart des libs du code la prennent en compte."""
    def __init__(self):
        self._protected = "lessons"

m = Monique()
print(m._protected)

class Monique2:
    def __init__(self):
        self.__private = "lessons"

m2 = Monique2()
#print(m2.private)
#print(m2._Monique2__private)
m2.__private = "bruno"
print(m2.__private)
