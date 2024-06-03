from view import View
from model import API

class Controller:
    def __init__(self, API):
        self.view = View()
        self.API = API
    
    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 5:
            if opcao == 1:
                result = self.API.getClassifications()
                self.view.imprimeStatus(result)
            if opcao == 2:
                result = self.API.getVenues()
                self.view.imprimeStatus(result)
            if opcao == 3:
                result = self.API.getEvents()
                self.view.imprimeStatus(result)
            if opcao == 4:
                result = self.API.getAttractions()
                self.view.imprimeStatus(result)
                
            opcao = self.view.menu()

if __name__ == "__main__":
    API = API()
    main = Controller(API)
    main.inicio()