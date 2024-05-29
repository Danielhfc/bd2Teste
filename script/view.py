from decimal import *

class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("M E N U")
        print("1. Popular a tabela de Classificacoes")
        print("2. Popular a tabela de Atracoes")
        print("3. Popular a tabela de Eventos")
        print("4. Popular a tabela de Locais")
        print("5. Sair")
        opcao = int(input("Digite a opcao desejada : "))
        return opcao

    def imprimeStatus(self, status):
        if (status == 1):
            print("Carga realizada com sucesso!")
        else:
            print(status)

