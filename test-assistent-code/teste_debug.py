# Teste automático do código corrigido
import sys
from io import StringIO

# Simular entrada do usuário
input_data = """João Silva
2
10.50
1
25.00
3
5.75
5
"""

# Redirecionar stdin
sys.stdin = StringIO(input_data)

# Importar e executar o código (simulando)
exec(open('debug.py').read())