class Elemento:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.cursor = None
        self.tamanho = 0

    def vazia(self):
        return self.primeiro is None


    def cheia(self):
        return False

    def inserir_como_primeiro(self, novo):
        novo_elemento = Elemento(novo)
        if self.vazia():
            self.primeiro = novo_elemento
            self.ultimo = novo_elemento
        else:
            novo_elemento.proximo = self.primeiro
            self.primeiro.anterior = novo_elemento
            self.primeiro = novo_elemento

        self.cursor = novo_elemento


    def inserir_como_ultimo(self, novo):
        novo_elemento = Elemento(novo)
        if self.vazia():
            self.primeiro = novo_elemento
            self.ultimo = novo_elemento
        else:
            self.ultimo.proximo = novo_elemento
            novo_elemento.anterior = self.ultimo
            self.ultimo = novo_elemento

        self.cursor = novo_elemento
