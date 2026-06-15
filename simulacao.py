print("-" * 60)
print("SIMULAÇÃO SISTEMA DE CARREGAMENTO INTELIGENTE FOTOVOLTAICO - GOODWE")
print("-" * 60)


bat_atual = float(input("Digite a Bateria atual (%): "))
bat_desejada = float(input("Digite a Bateria desejada (%): "))
if bat_atual > bat_desejada:
    bat_atual = float(input("Valor inválido! Digite a Bateria atual (%): "))
    bat_desejada = float(input("Digite a Bateria desejada (%): "))


print("_" * 60)
print("MENU DE MONITORAMENTO EM TEMPO REAL")
print("-" * 60)
print(f"Estado Inicial do Veículo: {bat_atual}% | Meta Desejada: {bat_desejada}%")
print("-" * 60)


def simular_tarifa_dinamica(bat_atual, bat_desejada):
    geracao_solar = [5.2, 3.2, 2.7, 4.1, 1.3]

    energia_total = ((bat_desejada - bat_atual) / 100.0) * 60.0

    print(f"Energia total necessária para a recarga: {energia_total:.2f} kWh\n")

    for ciclo, geracao in enumerate(geracao_solar, start=1):

        if geracao >= 5.0:
            preco_kwh = 0.50
            status = "ENSOLARADO"
        elif geracao >= 2.5:
            preco_kwh = 0.70
            status = "PARCIALMENTE ENSOLARADO"
        else:
            preco_kwh = 0.90
            status = "TEMPO FECHADO"

        tarifa_ciclo = energia_total * preco_kwh

        print(f"[Ciclo {ciclo}] Sol: {geracao} kW | Status: {status}")
        print(f"          └─► Preço do kWh: R$ {preco_kwh:.2f} | Custo Estimado: R$ {tarifa_ciclo:.2f}")
        print("-" * 60)


simular_tarifa_dinamica(bat_atual, bat_desejada)