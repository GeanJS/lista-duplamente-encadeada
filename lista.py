class Elemento:
    def __init__(self, dado):
        self.__dado = dado
        self.__anterior = None
        self.__proximo = None

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, novo_valor):
        self.__dado = novo_valor

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, novo_valor):
        self.__anterior = novo_valor

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def fim(self, novo_valor):
        self.__proximo = novo_valor 
