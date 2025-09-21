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

    def ir_para_primeiro(self):
        self.cursor = self.primeiro

    def ir_para_ultimo(self):
        self.cursor = self.ultimo

    def inserir_apos_atual(self, novo):
        if self.cursor is None:
            print("Erro: cursor não está em uma posição válida")
            return

        novo_elemento = Elemento(novo)
        novo_elemento.proximo = self.cursor.proximo
        novo_elemento.anterior = self.cursor

        self.cursor.proximo = novo_elemento

        if novo_elemento.proximo is not None:
            novo_elemento.proximo.anterior = novo_elemento
        else:
            self.ultimo = novo_elemento

    def inserir_antes_atual(self, novo):
        if self.cursor is None:
            print("Erro: cursor não está em uma posição válida")
            return

        if self.cursor.anterior is None:
            self.inserir_como_primeiro(novo)
            return

        novo_elemento = Elemento(novo)
        novo_elemento.proximo = self.cursor
        novo_elemento.anterior = self.cursor.anterior

        self.cursor.anterior.proximo = novo_elemento
        self.cursor.anterior = novo_elemento

    
    def inserir_na_posicao(self, K, novo):
        if K < 1:
            print("Erro: Posição inválida")
            return False

        novo_elemento = Elemento(novo)

        if K == 1:
            self.inserir_como_primeiro(novo)
            return True
        
        posicao_atual = 1
        elemento_atual = self.primeiro

        while elemento_atual is not None and posicao_atual < K - 1:
            elemento_atual = elemento_atual.proximo
            posicao_atual += 1

        if elemento_atual is None:
            self.inserir_como_ultimo(novo)
            return True


        novo_elemento.proximo = elemento_atual.proximo
        novo_elemento.anterior = elemento_atual
        elemento_atual.proximo = novo_elemento

        if novo_elemento.proximo is not None:
            novo_elemento.proximo.anterior = novo_elemento
        else:
            self.ultimo = novo_elemento

        return True


    def excluir_atual(self):
        if self.cursor is None:
            print("Erro: cursor não está em uma posição válida")
            return
        
        elemento_a_excluir = self.cursor

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
            self.cursor = None
            return


        if elemento_a_excluir == self.primeiro:
            self.primeiro = elemento_a_excluir.proximo
            self.primeiro.anterior = None
            self.cursor = self.primeiro
            return


        if elemento_a_excluir == self.ultimo:
            self.ultimo = elemento_a_excluir.anterior
            self.ultimo.proximo = None
            self.cursor = None
            return

        proximo = elemento_a_excluir.proximo
        anterior = elemento_a_excluir.anterior

        anterior.proximo = proximo
        proximo.anterior = anterior

        self.cursor = proximo

    
    def excluir_prim(self):
        if self.vazia():
            print("Erro: Lista Vazia")
            return
        
        self.ir_para_primeiro()
        self.excluir_atual()

    def excluir_ult(self):
        if self.vazia():
            print("Erro: Lista Vazia")
            return

        self.ir_para_ultimo()
        self.excluir_atual()


    def acessar_atual(self):
        if self.cursor is not None:
            return self.cursor.dado

        else:
            print("Erro: cursor inválido")
            return None

    def buscar(self, chave):
        elemento_atual = self.primeiro
        while elemento_atual is not None:
            if elemento_atual.dado == chave:
                self.cursor = elemento_atual
                return True
            elemento_atual = elemento_atual.proximo
        self.cursor = None
        return False


    def posicao_de(self, chave):
        posicao = 1
        elemento_atual = self.primeiro
        while elemento_atual is not None:
            if elemento_atual.dado == chave:
                return posicao
            elemento_atual = elemento_atual.proximo
            posicao += 1
        return -1


    def avancar_k_posicoes(self, K):
        if self.cursor is None:
            print("Erro: cursor inválido")
            return

        posicoes_percorridas = 0
        while posicoes_percorridas < K and self.cursor.proximo is not None:
            self.cursor = self.cursor.proximo
            posicoes_percorridas += 1


    def retroceder_k_posicoes(self, K):
        if self.cursor is None:
            print("Erro: cursor inválido")
            return

        posicoes_percorridas = 0
        while posicoes_percorridas < K and self.cursor.anterior is not None:
            self.cursor = self.cursor.anterior
            posicoes_percorridas += 1


    def __str__(self):
        elementos = []
        no_atual = self.primeiro
        while no_atual is not None:
            if no_atual == self.cursor:
                elementos.append(f"->[{no_atual.dado}]<-")
            else:
                elementos.append(str(no_atual.dado))
            no_atual = no_atual.proximo
        return " <-> ".join(elementos) or "[]"
