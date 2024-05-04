class Pessoa:
    def __init__(self, identificador):
        self.__nome = ""
        self.id = identificador

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome