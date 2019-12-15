class QuadriLateral: #classe mama
    def __init__(self, a, b, c, d):
        """Le constructeur (__init__()méthode) reçoit quatre paramètres
         et les affecte à quatre variables d'instance.
         Pour tester la classe ci-dessus, déclarez son objet
         et appelez la methode perimeter()."""
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d

    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=",p)

forme = QuadriLateral(7, 5, 6, 4)
forme.perimeter() # = 22 (7+5+6+4)

class Rectangle(QuadriLateral):
    def __init__(self, a, b):
        """Nous concevons maintenant une classe rectangle
         basée sur la classe quadriLateral (le rectangle EST un quadrilatère!).
         Les variables d'instance et la methode perimeter() de la classe
         de base doivent être disponibles automatiquement sans la redéfinir."""
        super().__init__(a, b, a, b)
        """Puisque les côtés opposés du rectangle sont identiques,
        nous n'avons besoin que de deux côtés adjacents pour construire son objet.
        Par conséquent, les deux autres paramètres de la méthode __init__() sont définis
        sur aucun. La méthode __init__() transmet les paramètres au constructeur
        de sa classe de base (quadriLateral) à l'aide de la fonction super().
        L'objet est initialisé avec side3 et side4 défini sur aucun.
        Les côtés opposés sont rendus égaux par le constructeur de la classe rectangle.
        N'oubliez pas qu'il a hérité automatiquement de la méthode perimeter(),
        il n'est donc pas nécessaire de la redéfinir."""
forme2 = Rectangle(10, 20) # 60 = 10+20+10+20
forme2.perimeter()
