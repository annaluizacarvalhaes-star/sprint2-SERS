# SIMULAÇÃO SISTEMA DE CARREGAMENTO INTELIGENTE FOTOVOLTAICO - GOODWE
from fontTools.misc.cython import returns



print("-"*60)
print ("SIMULAÇÃO SISTEMA DE CARREGAMENTO INTELIGENTE FOTOVOLTAICO - GOODWE")
print("-"*60)

bat_atual = input("Digite a Bateria atual: ")
bat_desejada = input("Digite a Bateria desejada: ")
energia = int

print("_"*60)
print("MENU")
print("-"*60)
print(f"Estado Inicial do Veículo: {bat_atual}% | Meta Desejada: {bat_desejada}%")


def tarifa (bat_atual, bat_desejada, geracao_solar):
    diferenca = bat_desejada - bat_atual
    energia = (diferenca * 0.005) * 60.0


    if geracao_solar >= 5.0:
        preco_kwh = 0.10  # Super barato! Tem muito sol gerando energia
    elif geracao_solar >= 2.5:
        preco_kwh = 0.35  # Desconto intermediário (híbrido)
    else:
        preco_kwh = 0.70  # Sem sol, usa a tarifa cheia da rede

tarifa = (energia * preco_kwh)