"""
    CONSTANTE = "Variáveis que não vão mudar"
    Muitas condições no mesmo if (ruim)
    <-- Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 #Existe uma convenção de que são utilizados letras maiusculas para constante(nunca irão mudar)

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

if velocidade > RADAR_1:
    print('Velocidade carro passou radar 1')

if local_carro >= (LOCAL_1 + RADAR_1) and \
    local_carro <= (LOCAL_1 - RADAR_1) and \
        velocidade_carro_passou_radar_1:
    print('Carro multado em radar 1')