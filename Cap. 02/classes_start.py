#
# Exemplo de como criar classes
#

class minhasClasse():
    def __init__(self):
        self.meuAtributo = "Passou pelo construtor!"

    def meuMetodo(self):
        print("Passou pelo meuMetodo");

    def meuMetodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)

    
def criaObjeto():
    meuObj = minhasClasse()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()
    meuObj.meuMetodo2("Executando meu método 2")

criaObjeto()