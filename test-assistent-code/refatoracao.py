def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros (list): Lista de números para análise

    Returns:
        tuple: (total, media, maior, menor) ou None se a lista estiver vazia

    Raises:
        TypeError: Se a lista contiver elementos não numéricos
    """
    if not numeros:
        return None

    # Calcula o total usando a função built-in sum()
    total = sum(numeros)

    # Calcula a média (usando divisão float)
    media = total / len(numeros)

    # Encontra o maior e menor valores usando funções built-in
    maior = max(numeros)
    menor = min(numeros)

    return total, media, maior, menor


# Lista de exemplo
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Chama a função
resultado = calcular_estatisticas(numeros)

if resultado is not None:
    total, media, maior, menor = resultado
    print(f"Total: {total}")
    print(f"Média: {media:.2f}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
else:
    print("A lista está vazia!")
