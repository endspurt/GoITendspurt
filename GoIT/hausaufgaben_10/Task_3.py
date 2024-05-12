class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass
        
    def change_weight(self, new_weight):
        self.weight = new_weight 
      
animal = Animal("Simon", 10)
animal.change_weight( 12)

'''Um den geforderten Python-Klasse Animal zu erstellen, ergänzen wir nun zusätzlich zur Klasse und ihrer say Methode auch die change_weight Methode, die das Gewicht des Tieres ändern kann. 
Dann erstellen wir eine Instanz dieser Klasse und ändern deren Gewicht mit der neuen Methode:'''