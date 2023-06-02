# Introdução

## Sobre ferramentas e programação

* Para fazer ciência, precisamos de ferramentas que nos ajudem nas tarefas, tanto habituais como específicas. O uso de computadores se tornou ubíquo em todas as áreas da ciência, e há uma variedade infindável de programas feitos para as mais diferentes tarefas. Eu gosto bastante de procurar programas que me auxiliam em diversas tarefas, como realizar anotações, administrar bibliografia, e outras coisas.
* Porém, a maneira mais flexível de interação com um computador é por meio de linguagens de programação. Elas fazem a intermediação entre o ser humano e a máquina e, preferencialmente, são facilmente lidas por *seres humanos*. A programação no meio científico é uma ferramenta bastante poderosa para auxiliar, dentre outras coisas, na execução de projetos e análise de dados.
* Mas uma linguagem de programação é somente uma ferramenta. Não faz sentido defender uma ferramenta frente à outra, sem conhecer o contexto da tarefa e da pessoa. Eu, pessoalmente, gosto de programar e automatizar certas tarefas. Acho que os resultados ficam mais organizados, consigo ser mais rigoroso em certas análises, testo mais possibilidades. Mas há sempre um investimento de tempo necessário, tanto para *aprender* quanto para *aplicar*.
* Algumas características positivas e negativas sobre utilizar programação num contexto científico
  * *Pode* poupar muito tempo, como também *pode* ser perda de tempo.
  * *Pode* permitir realizar várias análises num conjunto de dados
  * *Pode* permitir trocar algum parâmetro de análise facilmente, e tudo se refazer do zero
  * *Pode* permitir padronizar formatos de gráfico e tratamento de dados
  * *Pode* ser uma maneira mais legível para o registro de atividades que, p.e., uma planilha do Excel ou um projeto do Origin mas vai depender da sua capacidade de organização também.
    * O problema do Excel e do Origin é que são essencialmente não-lineares. Um script, necessariamente, é executado de "cima para baixo". Porém, se você não tiver o cuidado necessário, jupyter notebooks podem ter um pouco desta não-linearidade. Vamos abordar isso no curso.
  * *Pode* ser uma atividade divertida, mas *pode* ser bastante frustrante.
  * Pacotes são geralmente gratuitos e de código aberto. Isso pode-lhe permitir realizar tarefas que outros teriam que lidar com softwares pagos (ou pirataria). Por outro lado, muitas vezes tais pacotes são menos documentados e mais difíceis de se usar do que algumas soluções pagas, então a utilidade final irá depender do tempo disponível para aprender e da quantidade de dados a serem tratados.
    * Dependendo da tarefa, é tão específica que não há softwares para resolvê-la, então você precisa se virar para criar algo.

## Exemplos de situações onde programar foi útil para mim.

1. Uma amiga possuía um grande conjunto de curvas força-distância de AFM, e desejava obter a força necessária para a liberação da ponteira. Ela utilizava o Origin, plotava, colocava o cursor sobre o ponto mínimo e depois sobre o ponto de liberação, anotava os valores numa planilha, e continuava para o próximo dado. Não só era impreciso, mas muito entediante. Eu era relativamente amador e consegui fazer um script para tratar todos os dados dela rapidamente.
2. Eu me deparei com uma quantidade grande de dados de reologia de um projeto que participei. Cada arquivo específico possuía 3 curvas, em sequência, cada curva utilizava colunas diferentes do arquivo. Precisava remover pontos espúrios, fitar modelos em cada seção, plotar tudo e retornar uma tabela. Essa tarefa demoraria dias para realizar manualmente, mas consegui realizar tudo em uma tarde. Depois notei um erro e re-tratei tudo em 15 minutos.
3. Uma das tarefas durante o tratamento de dados de tomografia médica para análise de rochas, é a segmentação. Possuíamos um procedimento para amostras consolidadas, mas depois recebemos amostras com grandes buracos e o procedimento não era mais válido. Tornou-se necessário realizar a segmentação semi-manual, que demorava cerca de 10 minutos de trabalho monótono (com uma automação para acelerar) e altamente dependente do analista, o que nunca é muito desejado. Escrevi um script em Python que conseguia realizar isso em 30 segundos, e necessitava somente de uma visualização rápida para ver se tudo havia sido feito corretamente.
4. Neste mesmo tema, o protocolo de tratamento de tomografia possuía várias etapas, algumas bastante demoradas por conta dos algoritmos envolvidos. O software possuía uma interface em Python para automação e outra em Matlab para cálculos. Otimizando a segmentação (Python) e alguns cálculos (matlab) e automatizando algumas tarefas (filtração e aplicação de cálculos), o procedimento passou de 1 dia por amostra para 10 amostras por dia. E melhor, a maior parte do tempo era de espera, e não de procedimentos manuais entediantes, então era muito mais tranquilo.
5. Uma vez, precisávamos realizar experimentos ao longo de horas utilizando um equipamento de RMN de baixo campo. O equipamento não possuía a funcionalidade para isso. Escrevi um script utilizando pyautogui que clicava os botões no software do equipamento para realizar as medidas e conseguimos, então, realizar as medidas durante a noite. Depois, fiz outro script para automatizar o tratamento dos dados no mesmo software, que também não possuía a funcionalidade de tratamento em batelada.
6. Consegui meu primeiro emprego após a pós-graduação porque possuía conhecimentos em Python, que foi considerado um diferencial.

## Sobre como aprender a programar

* Programação geralmente requer uma abordagem diferente de outras ferramentas. É necessário seguir à risca as regras da linguagem. Ao contrário do Excel, por exemplo, não há uma interface simples para explorar e aprender experimentalmente. É necessário criar o programa essencialmente *do zero*, escrevendo-o linha por linha. Por isso, é absolutamente necessário memorizar várias coisas, como palavras chave, sintaxes, e inclusive algumas maneiras de organização de código. Alguns dos conceitos utilizados não são comumente encontrados em outros contextos, como *recursão*, e podem ser complicados de se entender. A chave para aprender tudo isso é esforço, repetição e treino, não há escapatória.
* Felizmente há ferramentas disponíveis para auxiliar no aprendizado de programação (de qualquer tema, realmente). Neste curso, utilizarei várias passagens do livro *The programmer's Brain*, de Felienne Hermans, para fornecer dicas de aprendizado e mostrar como nosso cérebro funciona na hora de aprender e resolver problemas.
* Por exemplo, a curva do esquecimento de Ebbinghaus mostra o quanto conseguimos reter de certa informação com o tempo:
 [Ebbinghaus](ebbinghaus.png)
 Note que cerca de algumas horas após aprender alguma coisa, já é capaz de termos esquecido 60% da informação. Porém, a repetição espaçada (com um espaçamento adequato, não muito curto nem muito longo) pode permitir-lhe relembrar de informação com maior eficiência, pois torna a curva de Ebbinghaus menos abrupta. 
* Se você já têm experiência com outras linguagens, aprender uma nova é muito mais fácil - desde que a abordagem da linguagem é similar (se tiverem curiosidade, procurem depois por APL, Lisp e Haskell para verem algumas abordagens diferentes).

## Por que Python?

* Python ganhou muita popularidade em tempos recentes com o boom da inteligência artificial, aprendizado de máquina e ciência de dados. É uma uma linguagem acessível, gratuita, multi-paradigma, multi-plataforma, com uma sintaxe clara, e sem grandes complicações com o sistema de tipos. Possui uma quantidade grande de pacotes gratuitos, para uma enorme variedade de finalidades.
* É uma das linguagens mais populares entre aqueles que estão aprendendo a programar, e popular também entre programadores mais experientes [fonte](https://survey.stackoverflow.co/2022/#most-popular-technologies-language-learn), atrás somente de linguagens voltadas à web (p.e. Javascript). Possui uma grande comunidade de suporte e muita gente trabalhando para que sempre melhore.
* Não é uma linguagem sem falhas. Porém, para as finalidades científicas cotidianas, é plenamente viável. Tarefas com uma alta necessidade de performance vão requerer abordagens diferentes, pois podem ser muito lentas em Python. Porém, há várias alternativas para contornar isso, como [Cython](https://cython.org/), [Numba](https://numba.pydata.org/) e [extensões para C e C++](https://docs.python.org/3/extending/extending.html).
* *A tarefa dita a ferramenta que precisa ser utilizada*. Se Python não for uma boa escolha para a tarefa, busque outra ferramenta. Não seja extremista.

## Outras línguas muito utilizadas no meio científico

* Julia (focada em maior performance)
* R (focada em estatística)
* Matlab (focada em operações matriciais. Possui uma das melhores ajudas de qualquer linguagem, e uma coleção de pacotes extremamente úteis)
* Octave, alternativa open-source ao Matlab.
* Mathematica (focada em pesquisa matemática)
* Maple (focada em pesquisa matemática)

## Fluxograma de trabalho com Python

1. Escrever código
2. Enviar código para o executável
3. Avaliar o resultado. Não está bom? Volta a escrever
4. Se está bom, exportar os resultados se necessário

[Fluxograma](Fluxograma.png)

### Com o que escrever scripts Python

* Editores de texto simples (bloco de notas), mas não é recomendado, pois faltam várias características desejadas.
* Editores de texto como **Thonny**, Visual Studio Code, Sublime Text. São mais avançados, possuem ferramentas para autocompletação de código e realce de linguagem. **Visual Studio Code** é muito famoso e certamente o mais popular de todos citado aqui. Possui um extenso ecossistema de extensões para habilitar muitas funcionalidades ao código.
* IDEs como **PyCharm** Community Edition (quem possui email educacional pode solicitar uma licença para a versão Professional gratuitamente) e Visual Studio. Possuem muitas ferramentas que auxiliam muito na elaboração de projetos mais complexos. Pecam no suporte para Jupyter Notebooks.

### Como rodar scripts Python

* Para rodar um script, é necessário ter o executável Python (`python.exe`) com os pacotes necessários acessíveis pelo executável. O executável pode estar tanto no seu computador, como na rede ou na nuvem. 
* A opção mais fácil é utilizar ferramentas da nuvem, mas há uma série de restrições e chateações quando se faz isso, começando pela lentidão e complicação para colocar seus dados junto da nuvem. Instalar localmente é, de forma geral, a maneira mais robusta de se utilizar a ferramenta.
* É necessário ter algum conhecimento de **linha de comando** para utilizar python e as ferramentas. Os *shells* comumente utilizados em Windows são `cmd.exe` e `powershell.exe`. Felizmente, os comandos que precisam ser utilizados frequentemente são poucos e simples.

### Como instalar

* Utilizando o instalador do site [python.org], versão 3.11 ou mais recente
  * Pacote básico, não precisa de permissão de administrador
* Utilizando o instalador [Anaconda](https://www.anaconda.com/download/) (ou [miniconda](https://docs.conda.io/en/latest/miniconda.html))
  * Pacote voltado para ciência de dados. Já vem com vários pacotes pré-instalados e um gerenciador de pacotes próprio, o conda, que é mais poderoso que o nativo, pip. Não precisam de permissão de administrador.
  * Anaconda vem com várias coisas extras que podem ser úteis para você. Miniconda é mais recomendado se você só quer uma instalação básica e irá criar seus ambientes depois. Para este curso, o Anaconda é mais recomendado.
* [Thonny](https://thonny.org/), um editor que já vem com sua instalação python própria.
* Ferramentas online
* https://replit.com/ - Tem planos gratuitos para criar alguns projetos. Funciona a base de arquivos .py e não de notebooks. Bastante lento na minha opinião, não servirá para muitas coisas além do mais básico do começo.
* https://www.online-python.com/ - Este é OK para o começo, mas quando avançarmos a temas mais relevantes, principalmente quanto tivermos que utilizar pacotes científicos, é melhor utilizar outras opções.
* Online, baseado em jupyter notebooks
* Google Colab - ferramenta padrão para notebooks online.
* JetBrains Datalore - tem planos gratuitos para iniciantes.
* [Jupyter Lite](https://jupyter.org/try-jupyter/lab/)

* **Recomendação**: Anaconda, ou Thonny seguido de Anaconda.


### Primeiro script, para verificar se tudo está correto.

* Inicie uma instância do interpretador
  * Python puro: abra um `shell` digitando na barra de pesquisa `cmd` ou `powershell`, clique no ícone, depois digite `python`, aperte Enter.
  * Anaconda (miniconda): Em iniciar, encontre o `Anaconda Prompt` e clique, digite `python`, aperte Enter.
  * Thonny: Abra o editor.
  * Nuvem: crie um novo notebook, e depois uma célula no notebook.
* Digite o seguinte código:
  
```python
print("Hello world!")
```
  * Aperte Enter (ou Shift+Enter nos notebooks). Se a mensagem `Hello world!` aparecer logo em seguida, tudo está funcionando direito.
  * Se, ao digitar `python` no `shell` e aparecer um erro de que o comando não foi encontrado, você possui um problema na variável `PATH` de ambiente. Siga [este](https://realpython.com/add-python-to-path/) tutorial caso isso ocorra.