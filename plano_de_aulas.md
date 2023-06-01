# Plano de aulas

## Aula 1

* Sobre programar, e sua função aplicada ao meio científico
  * Imagem da produtividade. Tempo de latência.
    * *Pode* poupar muito tempo
    * *Pode* permitir realizar várias análises num conjunto de dados
    * *Pode* permitir trocar algum parâmetro de análise facilmente, e tudo se refazer do zero
    * *Pode* permitir padronizar formatos de gráfico e tratamento
  * *Pode* ser uma maneira mais legível para o registro de atividades que, p.e., uma planilha do Excel ou um projeto do Origin mas vai depender da sua capacidade de organização também.
    * O problema do Excel e do Origin é que são essencialmente não-lineares. Um script, necessariamente, é executado de "cima para baixo". Porém, se você não tiver o cuidado necessário, jupyter notebooks podem ter um pouco desta não-linearidade. Vamos abordar isso no curso.
  * *Pode* ser uma atividade divertida, mas pode ser bastante frustrante.
  * Pacotes são geralmente gratuitos e de código aberto. Isso pode-lhe permitir realizar tarefas que outros
  * Para alguns problemas, é a única maneira de se realizar algumas tarefas em tempo hábil, sem depender de softwares de terceiros (pagos ou não). Dependendo da tarefa, é tão específica que não há softwares para resolvê-la.
* Exemplos de situações onde programar foi útil para mim.
  1. Uma amiga possuía um grande conjunto de curvas força-distância de AFM, e desejava obter a força necessária para a liberação da ponteira. Ela utilizava o Origin, plotava, colocava o cursor sobre o ponto mínimo e depois sobre o ponto de liberação, anotava os valores numa planilha, e continuava para o próximo dado. Não só era impreciso, mas muito entediante. Eu era relativamente amador e consegui fazer um script para tratar todos os dados dela rapidamente.
  2. Eu me deparei com uma quantidade grande de dados de reologia de um projeto que participei. Cada arquivo específico possuía 3 curvas, em sequência, cada curva utilizava colunas diferentes do arquivo. Precisava remover pontos espúrios, fitar modelos em cada seção, plotar tudo e retornar uma tabela. Essa tarefa demoraria dias para realizar manualmente, mas consegui realizar tudo em uma tarde. Depois notei um erro e re-tratei tudo em 15 minutos.
  3. Uma das tarefas durante o tratamento de dados de tomografia médica para análise de rochas, é a segmentação. Possuíamos um procedimento para amostras consolidadas, mas depois recebemos amostras com grandes buracos e o procedimento não era mais válido. Tornou-se necessário realizar a segmentação semi-manual, que demorava cerca de 10 minutos de trabalho monótono (com uma automação para acelerar) e altamente dependente do analista, o que nunca é muito desejado. Escrevi um script em Python que conseguia realizar isso em 30 segundos, e necessitava somente de uma visualização rápida para ver se tudo havia sido feito corretamente.
  4. Neste mesmo tema, o protocolo de tratamento de tomografia possuía várias etapas, algumas bastante demoradas por conta dos algoritmos envolvidos. O software possuía uma interface em Python para automação e outra em Matlab para cálculos. Otimizando a segmentação (Python) e alguns cálculos (matlab) e automatizando algumas tarefas (filtração e aplicação de cálculos), o procedimento passou de 1 dia por amostra para 10 amostras por dia. E melhor, a maior parte do tempo era de espera, e não de procedimentos manuais entediantes, então era muito mais tranquilo.
  5. Uma vez, precisávamos realizar experimentos ao longo de horas utilizando um equipamento de RMN de baixo campo. O equipamento não possuía a funcionalidade para isso. Escrevi um script utilizando pyautogui que clicava os botões no software do equipamento para realizar as medidas e conseguimos, então, realizar as medidas durante a noite. Depois, fiz outro script para automatizar o tratamento dos dados no mesmo software, que também não possuía a funcionalidade de tratamento em batelada.



* Como instalar Python
    * Utilizando o instalador do site python.org, versão 3.11 ou mais recente
    * Utilizando o instalador Anaconda
    * Utilizando o instalador miniconda
    * Utilizando online, por meio do Google Colab, 