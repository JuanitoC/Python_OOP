class Claseando:
    indice = 1
    listado = []

    def __init__(self, name):
        self.name = name
        self.id = Claseando.indice
        Claseando.indice += 1

        self.list = Claseando.listado

        Claseando.listado.append(self.id)




c1 = Claseando('clase1')
c2 = Claseando('clase2')
c3 = Claseando('clase3')
c4 = Claseando('clase4')

print(c1.id, c1.name, c1.list)
print(c2.id, c2.name, c2.list)
print(c3.id, c3.name, c3.list)
print(c4.id, c4.name, c4.list)
