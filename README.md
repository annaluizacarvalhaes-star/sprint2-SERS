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

### Arquitetura e Justificativa Técnica do Sistema

O protótipo foi desenhado seguindo o modelo de ecossistema de Smart Charging inspirado nas tecnologias de inversores e gerenciamento de baterias da GoodWe. 

#### Arquitetura de Fluxo de Dados (IoT)
O sistema opera como um Hub em Edge Computing (computação de borda) simulado, onde o fluxo de tomada de decisão segue a seguinte lógica:
1. **Entrada de Dados do Utilizador:** O sistema mapeia o estado atual da bateria do Veículo Elétrico (VE) e a meta desejada.
2. **Leitura dos Sensores (IoT):** A lista de geração solar simula a telemetria em tempo real enviada pelo inversor fotovoltaico GoodWe para o carregador.
3. **Processamento Central (Algoritmo):** O script analisa a potência instantânea disponível (kW) e toma a decisão automatizada de qual tarifa aplicar por kWh e qual o status de carregamento ideal para aquele momento do dia.

#### Justificativa Técnica
A escolha por um sistema de carregamento adaptativo justifica-se pela instabilidade natural das fontes renováveis (como a energia solar, que varia com o passar das nuvens e o horário do dia). Em vez de injetar uma potência estática e sobrecarregar a rede elétrica comercial ou residencial, o algoritmo calcula o balanço energético dinamicamente. Se há muito sol, o sistema barateia o custo para incentivar o consumo da energia limpa gerada localmente. Se o tempo fecha, o custo aumenta para sinalizar o uso da rede elétrica convencional.



### Princípios de Sustentabilidade e Energias Renováveis

A integração proposta entre a mobilidade elétrica e o gerenciamento inteligente de dados atende diretamente aos três pilares da transição energética global abordados na Sprint 1:

* **Descarbonização Real da Matriz:** Um veículo elétrico só é verdadeiramente "zero emissões" se a fonte que gera a sua eletricidade também for limpa. O algoritmo prioriza o carregamento nos ciclos de alta geração solar (Status: Ensolarado com tarifa a R$ 0,50), garantindo que o combustível do carro seja o Sol e mitigando o uso de centrais termoelétricas fósseis.
* **Eficiência Energética e Estabilização da Rede (*Smart Grid*):** O carregamento desordenado de veículos elétricos pode colapsar subestações urbanas em horários de pico. Ao monitorar a geração e aplicar tarifas dinâmicas, o Hub inteligente atua no balanceamento de carga, incentivando o carregamento inteligente e otimizando o Ciclo de Vida Total do ecossistema de energia do comerciante.
* **Preparação para Cidades Inteligentes (*Smart Cities*):** O uso de dados em tempo real para regular a potência evita o desperdício de energia em calor e prepara a infraestrutura para a tecnologia V2G (Vehicle-to-Grid), onde o carro poderá devolver energia para o estabelecimento em momentos de tempo fechado ou emergências.
solar instantânea, o status climático do momento, o preço do kWh aplicado e o custo financeiro estimado para aquela janela de recarga.
