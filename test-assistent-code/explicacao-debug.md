# Depuração do Código - debug.py

## Visão Geral dos Erros
O código `debug.py` contém vários erros de sintaxe e lógica que impedem sua execução correta. Abaixo, identifico e corrijo cada erro encontrado.

---

## Análise Detalhada dos Erros

### Erro 1: Sintaxe Inválida no input do Item 1
**Linha problemática:**
```python
item1 = float(input(Preço do item 1? ))
```

**Problema:**
- Falta aspas duplas `"` ao redor da string no `input()`
- Sintaxe: `input(Preço do item 1? )` → Erro de sintaxe

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

**Explicação:**
- O `input()` requer uma string como argumento
- As aspas delimitam a string que será exibida ao usuário

---

### Erro 2: Parênteses Desnecessários no input do Cupom
**Linha problemática:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

**Problema:**
- Parênteses externos são desnecessários e podem causar confusão
- Embora não cause erro de sintaxe, é má prática

**Correção:**
```python
desconto_cupom = input("Você tem um cupom de desconto? (Digite o percentual ou 0): ")
```

**Explicação:**
- O `input()` já retorna uma string, não precisa de parênteses extras
- Código mais limpo e seguindo convenções Python

---

### Erro 3: Falta do 'f' na f-string do Item 2
**Linha problemática:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Problema:**
- Falta o prefixo `f` para indicar que é uma f-string
- Sintaxe: `" Item 2:        R$ {total_item2:.2f}"` → String literal comum, não f-string

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

**Explicação:**
- f-strings (introduzidas no Python 3.6) permitem interpolação de variáveis
- Sem o `f`, as chaves `{}` são tratadas como texto literal

---

### Erro 4: Comparação de String com Número Inteiro
**Linha problemática:**
```python
if desconto_cupom > 0:
```

**Problema:**
- `desconto_cupom` é uma string (retornada pelo `input()`)
- Não é possível comparar string com inteiro diretamente
- TypeError: `'>' not supported between instances of 'str' and 'int'`

**Correção:**
```python
if float(desconto_cupom) > 0:
```

**Explicação:**
- Converter a string para float antes da comparação
- Permite verificar se o desconto é maior que zero

---

### Erro 5: Uso de String em Formatação Numérica
**Linha problemática:**
```python
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problema:**
- `desconto_cupom` é string, mas está sendo formatado como float (`.0f`)
- ValueError: `Unknown format code 'f' for object of type 'str'`

**Correção:**
```python
print(f" Desconto ({float(desconto_cupom):.0f}%): -R$ {desconto:.2f}")
```

**Explicação:**
- Converter `desconto_cupom` para float antes da formatação
- Permite exibir o percentual corretamente

---

### Erro 6: Uso Redundante de round() em f-string
**Linha problemática:**
```python
print(f" TOTAL:         R$ {round(total, 2):.2f}")
```

**Problema:**
- `round(total, 2)` arredonda para 2 casas decimais
- Depois aplica `:.2f` que também formata para 2 casas
- Embora funcione, é redundante e pode causar problemas de precisão

**Correção:**
```python
print(f" TOTAL:         R$ {total:.2f}")
```

**Explicação:**
- `:.2f` já formata o número com 2 casas decimais
- Mais eficiente e direto

---

## Código Corrigido Completo

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = input("Você tem um cupom de desconto? (Digite o percentual ou 0): ")
desconto = subtotal * (float(desconto_cupom) / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if float(desconto_cupom) > 0:
    print(f" Desconto ({float(desconto_cupom):.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

---

## Teste de Validação

### Entrada de Teste:
```
Nome: João Silva
Quantidade 1: 2
Preço 1: 10.50
Quantidade 2: 1
Preço 2: 25.00
Quantidade 3: 3
Preço 3: 5.75
Cupom: 5
```

### Saída Esperada:
```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 21.00
 Item 2:        R$ 25.00
 Item 3:        R$ 17.25
-------------------------------
 Subtotal:      R$ 63.25
 Imposto (10%): R$ 6.33
 Desconto (5%): -R$ 3.16
===============================
 TOTAL:         R$ 66.42
===============================
```

---

## Lições Aprendidas

1. **Sintaxe**: Sempre use aspas em strings do `input()`
2. **Tipos de Dados**: `input()` retorna string, converta quando necessário
3. **f-strings**: Não esqueça o prefixo `f` para interpolação
4. **Conversões**: Use `float()` e `int()` para conversões seguras
5. **Formatação**: Entenda como funcionam os especificadores de formato

---

## Melhorias Sugeridas (Opcionais)

1. **Validação de Entrada**: Verificar se os valores são positivos
2. **Tratamento de Erros**: Usar try/except para entradas inválidas
3. **Constantes**: Definir taxa de imposto como constante
4. **Funções**: Modularizar o código em funções menores
5. **Comentários**: Adicionar mais comentários explicativos

Este código agora está funcional e segue boas práticas básicas de Python! ✅
