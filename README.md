# SIMULAÇÃO SISTEMA DE CARREGAMENTO INTELIGENTE FOTOVOLTAICO - GOODWE
## sprint 2 SERS
### Integrantes:
Anna Luiza Cavalcante Carvalhaes RM: 573330

Kethelyn de Oliveira Rocha RM: 574016

Samara Carvalho RM: 573666

Gabriela Batista RM: 573583

### Explicação técnica 
O nosso programa foi desenvolvido na linguagem Python, onde ele recebe a bateria inicial e a desejada do Veiculo Elétrico. Caso 
o usuário digite um nível de bateria desejada menor que a atual, o sistema solicita os valores novamente. Após o Menu inicial, o 
programa calcula o valor da energia necessária para o carregamento, o calculo feito é:
#### ((Bateria desejada - bateria atual)/100.0) * 60.0 kWh
Para o calculo da tarifa, o programa adota os seguintes valores: R$ 0,50 para momentos ensolarados, com a geração solar é maior 
igual a 5.0 kW (alta disponibilidade de energia limpa local); R$0,70  para geração solar maior ou igual a 2.5kW, mas menor que 
5.0 kW (sistema híbrido: solar + rede); R$0,90 para geração solar menor que 2.5kW (alta dependência da rede elétrica da concessionária).

Para a simulação de geração solar, criamos uma lista, com valores ficticios para 5 ciclos. Além da tarifa, o sistema exibe o status 
de geração solar, como: Ensolarado, Parcialmente ensolarado e Tempo fechado.

Para a simulação dos cenários climáticos, criamos uma estrutura de repetição (loop) que consome uma lista de valores fictícios 
representando 5 ciclos de leitura de sensores IoT. Por fim, o sistema exibe dinamicamente no terminal o número do ciclo, a potência 
solar instantânea, o status climático do momento, o preço do kWh aplicado e o custo financeiro estimado para aquela janela de recarga.
