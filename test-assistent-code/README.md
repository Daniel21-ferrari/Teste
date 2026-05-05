# Test Assistant Code

## Descrição

Este projeto é uma coleção de exemplos de código Python desenvolvidos para auxiliar no aprendizado e prática de conceitos fundamentais de programação, incluindo algoritmos básicos, depuração de código, refatoração e testes automatizados. Cada arquivo demonstra um aspecto específico do desenvolvimento de software, com explicações detalhadas em arquivos Markdown acompanhantes.

O projeto serve como um assistente para estudantes e desenvolvedores que desejam melhorar suas habilidades em Python através de exemplos práticos e correções passo a passo.

## Estrutura do Projeto

### Arquivos Principais

- **`num_primos.py`**: Implementa uma função otimizada para verificar se um número é primo, utilizando um algoritmo eficiente que reduz a complexidade de tempo.
  
- **`debug.py`**: Script de cálculo de fatura de compras que contém erros intencionais para prática de depuração. Inclui entrada de dados do usuário, cálculos de totais, impostos e descontos.

- **`refatoracao.py`**: Versão refatorada de uma função de cálculo de estatísticas básicas (total, média, maior e menor valor) de uma lista de números, demonstrando boas práticas de código limpo.

- **`teste_debug.py`**: Script de teste automatizado que simula entradas para o `debug.py` e executa o código corrigido.

### Arquivos de Explicação

- **`explicacao_num_primo.md`**: Análise linha a linha da função `eh_primo()`, explicando a lógica matemática e otimizações implementadas.

- **`explicacao_refatoracao.md`**: Comparação entre o código original confuso e a versão refatorada, destacando melhorias em nomeclatura, eficiência e legibilidade.

- **`explicacao-debug.md`**: Identificação e correção detalhada dos erros de sintaxe e lógica encontrados no `debug.py`.

## Como Usar

### Pré-requisitos

- Python 3.x instalado no sistema

### Execução dos Scripts

1. **Verificação de Números Primos**:
   ```bash
   python num_primos.py
   ```
   O script executará testes com uma lista de números pré-definidos e exibirá se cada um é primo.

2. **Script de Depuração**:
   ```bash
   python debug.py
   ```
   Solicitará entrada interativa do usuário para nome do cliente, quantidades e preços de 3 itens, e percentual de desconto.

3. **Função Refatorada**:
   ```bash
   python refatoracao.py
   ```
   Calcula e exibe estatísticas de uma lista de números de exemplo.

4. **Teste Automatizado**:
   ```bash
   python teste_debug.py
   ```
   Executa o `debug.py` com entradas simuladas automaticamente.

### Leitura das Explicações

Os arquivos `.md` podem ser abertos em qualquer editor de texto ou visualizados diretamente no GitHub/VS Code para entender a lógica por trás de cada código.

## Conceitos Demonstrados

- **Algoritmos**: Verificação de primalidade com otimização
- **Depuração**: Identificação e correção de erros de sintaxe e lógica
- **Refatoração**: Transformação de código confuso em código limpo e eficiente
- **Testes**: Simulação automatizada de entradas para validação
- **Documentação**: Uso de docstrings no estilo Google
- **Comentários**: Explicações inline de decisões lógicas

## Contribuição

Este projeto é educacional e pode ser expandido com mais exemplos. Sugestões de melhorias são bem-vindas através de issues ou pull requests.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.</content>
<parameter name="filePath">c:\Users\DANIELFERRARIBELETTI\Documents\Teste\test-assistent-code\README.md