# Explicação Linha a Linha - Função de Verificação de Números Primos

## Visão Geral
Este código implementa uma função que determina se um número é primo usando um algoritmo otimizado que reduz significativamente o tempo de execução.

---

## Análise Detalhada

### Definição da Função
```python
def eh_primo(numero):
```
- Define uma função chamada `eh_primo`
- Recebe um parâmetro `numero` (o número a ser verificado)

### Docstring (Documentação)
```python
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
```
- Documentação da função (docstring)
- Explica o propósito da função
- Descreve o parâmetro de entrada: `numero` deve ser um inteiro
- Descreve o retorno: `True` (é primo) ou `False` (não é primo)

### Primeira Verificação - Números Menores que 2
```python
    if numero < 2:
        return False
```
- **Condição**: Verifica se o número é menor que 2
- **Justificativa**: Por definição matemática, números menores que 2 (incluindo negativos, 0 e 1) NÃO são primos
- **Ação**: Retorna `False` imediatamente (não precisa verificar mais)

### Segunda Verificação - O Número 2
```python
    if numero == 2:
        return True
```
- **Condição**: Verifica se o número é exatamente 2
- **Justificativa**: 2 é o único número par que é primo
- **Ação**: Retorna `True` imediatamente (é primo)
- **Otimização**: Evita passes desnecessários no próximo if

### Terceira Verificação - Números Pares
```python
    if numero % 2 == 0:
        return False
```
- **Operação**: `numero % 2` calcula o resto da divisão por 2
- **Condição**: Se o resto é 0, o número é par
- **Justificativa**: Todos os números pares maiores que 2 NÃO são primos (têm 2 como divisor)
- **Ação**: Retorna `False` imediatamente
- **Otimização**: Elimina metade dos números de uma só vez!

### Loop de Verificação - O Coração do Algoritmo
```python
    for i in range(3, int(numero ** 0.5) + 1, 2):
```
- **`range(3, int(numero ** 0.5) + 1, 2)`**: Cria uma sequência de números
  - **Começa em**: 3 (começamos em 3 porque já verificamos 2)
  - **Termina em**: `int(numero ** 0.5) + 1` (raiz quadrada do número + 1)
  - **Passo**: 2 (verifica apenas números ímpares: 3, 5, 7, 9, ...)
  
- **Por que até a raiz quadrada?**
  - Se um número `n` tem um divisor maior que √n, ele também tem um divisor menor que √n
  - Exemplo: 36 = 6 × 6 (√36 = 6). Se 36 tem divisor 9 (> 6), então 36 ÷ 9 = 4 (< 6)
  - Isso reduz drasticamente o tempo de verificação!

- **Por que apenas números ímpares?**
  - Já eliminamos todos os pares na verificação anterior
  - Não há necessidade de testar números pares novamente

### Verificação de Divisibilidade
```python
        if numero % i == 0:
            return False
```
- **`numero % i`**: Calcula o resto da divisão de `numero` por `i`
- **Condição**: Se o resto é zero, significa que `i` divide `numero` perfeitamente
- **Conclusão**: Se encontra um divisor, o número NÃO é primo
- **Ação**: Retorna `False` imediatamente (não precisa verificar mais)

### Retorno Final
```python
    return True
```
- Se passou por todas as verificações sem encontrar divisores
- Significa que o número é primo
- Retorna `True`

---

## Exemplos de Execução

### Exemplo 1: Número 2
```
eh_primo(2):
- 2 < 2? Não
- 2 == 2? Sim → retorna True ✓
```

### Exemplo 2: Número 4
```
eh_primo(4):
- 4 < 2? Não
- 4 == 2? Não
- 4 % 2 == 0? Sim → retorna False ✓
```

### Exemplo 3: Número 17
```
eh_primo(17):
- 17 < 2? Não
- 17 == 2? Não
- 17 % 2 == 0? Não (17 é ímpar)
- Loop: i em [3, 5] (√17 ≈ 4.1, então até 5)
  - 17 % 3 == 0? Não
  - 17 % 5 == 0? Não
- Retorna True ✓ (17 é primo)
```

---

## Seção de Testes
```python
if __name__ == "__main__":
```
- **`if __name__ == "__main__":`**: Verifica se o arquivo está sendo executado diretamente
- Se verdadeiro, executa o código abaixo
- Se o arquivo for importado em outro módulo, esta seção NÃO executa

### Criação da Lista de Teste
```python
    numeros_teste = [1, 2, 3, 4, 5, 10, 17, 20, 29, 100]
```
- Lista com 10 números para testar
- Inclui: números pequenos, número 1, 2, pares, ímpares e números primos

### Print Inicial
```python
    print("Verificando números primos:\n")
```
- Exibe um cabeçalho
- `\n` cria uma linha em branco

### Loop de Iteração
```python
    for num in numeros_teste:
```
- Percorre cada número da lista `numeros_teste`
- `num` recebe o valor de cada número um por vez

### Resultado em Português
```python
        resultado = "sim" if eh_primo(num) else "não"
```
- **Operador ternário**: `valor_se_true if condicao else valor_se_false`
- Se `eh_primo(num)` retorna `True`: `resultado = "sim"`
- Se `eh_primo(num)` retorna `False`: `resultado = "não"`

### Print Formatado
```python
        print(f"{num:3d} é primo? {resultado}")
```
- **f-string**: String formatada com variáveis
- **`{num:3d}`**: Exibe `num` como um inteiro (d) ocupando 3 espaços, alinhado à direita
- Exemplo de saída: `  2 é primo? sim`

---

## Complexidade do Algoritmo

| Aspecto | Detalhes |
|--------|----------|
| **Complexidade de Tempo** | O(√n) - verifica valores até a raiz quadrada |
| **Complexidade de Espaço** | O(1) - usa apenas variáveis, sem estruturas adicionais |
| **Melhor Caso** | O(1) - quando o número é < 2, == 2, ou par |
| **Pior Caso** | O(√n) - quando o número é primo grande |

---

## Otimizações Implementadas

1. ✅ **Verificação de 2**: Trata o único par primo separadamente
2. ✅ **Eliminação de Pares**: Descarta metade dos números logo no início
3. ✅ **Raiz Quadrada**: Reduz iterações significativamente
4. ✅ **Passo de 2**: Verifica apenas números ímpares no loop
5. ✅ **Saída Antecipada**: Retorna `False` assim que encontra um divisor

Essas otimizações fazem o algoritmo ser **MUITO mais rápido** que uma verificação bruta!
