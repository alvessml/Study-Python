"""
CONSTANTE = Representa "variáveis" que não devem mudar
Evitar muitas condições em um único `if` (melhor para legibilidade)
"""
# Configurações do cenário
velocidade = 61  # Velocidade atual do carro
local_carro = 100  # Posição atual do carro na estrada

# Configurações do radar
RADAR_1 = 60  # Velocidade máxima permitida no radar 1
LOCAL_1 = 100  # Localização do radar 1
RADAR_RANGE = 1  # Alcance do radar em metros

# Variáveis de controle (exemplo de valores)
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = (
    LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE
)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# Lógica de verificação
if vel_carro_pass_radar_1:
    print('Velocidade do carro excedeu o limite no radar 1')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print('Carro foi multado no radar 1')
