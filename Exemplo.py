def main():
    """
    Função principal que executa o script de exemplo.
    """
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Resultado: {result}")


def process_data(data):
    """
    Processa uma lista de dados, retornando a soma dos elementos.

    Args:
        data (list): Lista de números a serem processados.

    Returns:
        int: Soma dos elementos da lista.
    """
    return sum(data)


if __name__ == "__main__":
    main()