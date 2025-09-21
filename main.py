from lista import ListaDuplamenteEncadeada

if __name__ == "__main__":
    print("--- DEMONSTRAÇÃO DA LISTA DUPLAMENTE ENCADEADA ---")
    lista = ListaDuplamenteEncadeada()
    
    print("\n1. Inserindo elementos:")
    lista.inserir_como_primeiro("Cachorro")
    print(f"Lista após inserir 'Cachorro' como primeiro: {lista}")
    print(f"Cursor aponta para: {lista.acessar_atual()}")

    lista.inserir_como_ultimo("Elefante")
    print(f"Lista após inserir 'Elefante' como último: {lista}")
    print(f"Cursor aponta para: {lista.acessar_atual()}")
    
    lista.ir_para_primeiro()
    lista.inserir_apos_atual("Gato")
    print(f"Lista após inserir 'Gato' após o cursor (Cachorro): {lista}")
    print(f"Cursor ainda aponta para: {lista.acessar_atual()}")
    
    lista.inserir_na_posicao(2, "Leão")
    print(f"Lista após inserir 'Leão' na posição 2: {lista}")

    print("\n2. Buscando e movendo o cursor:")
    encontrado = lista.buscar("Gato")
    print(f"Busca por 'Gato': {encontrado}")
    print(f"Cursor agora aponta para: {lista.acessar_atual()}")
    
    posicao = lista.posicao_de("Elefante")
    print(f"Posição de 'Elefante': {posicao}")

    print("\n3. Navegando o cursor:")
    lista.ir_para_primeiro()
    print(f"Cursor movido para o primeiro: {lista.acessar_atual()}")
    lista.avancar_k_posicoes(2)
    print(f"Cursor avançou 2 posições: {lista.acessar_atual()}")

    print("\n4. Excluindo elementos:")
    lista.excluir_atual()
    print(f"Lista após excluir o elemento atual: {lista}")
    print(f"Cursor agora aponta para: {lista.acessar_atual()}")
    
    lista.excluir_ult()
    print(f"Lista após excluir o último elemento: {lista}")
    
    lista.excluir_prim()
    print(f"Lista após excluir o primeiro elemento: {lista}")

    print("\n5. Estado final da lista:")
    print(f"Lista final: {lista}")
    print(f"A lista está vazia? {lista.vazia()}")
