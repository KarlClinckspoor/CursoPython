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
* Algumas vezes, uma mudança de perspectiva se torna essencial para conseguir resolver problemas, especialmente de programação. Por exemplo: Suponha que há um trêm saindo de Campinas e indo a São Paulo, a 100 km de distância, e outro trêm indo na direção oposta e partindo no mesmo horário. Ambos os trêns avançam na velocidade de 25 km/h. Uma andorinha vai e volta entre os trêns, partindo de Campinas, e voa a 50 km/h. Qual será a distância total percorrida pela andorinha quando os trêns se encontrarem? Uma solução inicial seria modelar as velocidades e posições dos três objetos e resolver o conjunto de equações envolvidas. Porém, se você notar que os trêns se encontram em 2 horas, no meio do caminho, sabemos que a andorinha teve que percorrer 100 km, pois voou continuamente por 2 horas.
* Problemas em programação são frequentemente resolvidos da seguinte maneira: Para resolver um grande e complexo problema, irei subdividi-lo em problemas menores e mais simples, até que saiba resolver todos os mini-problemas. Apesar de uma descrição simples, tal tarefa demanda experiência.

## Por que Python?

* Python ganhou muita popularidade em tempos recentes com o boom da inteligência artificial, aprendizado de máquina e ciência de dados. É uma uma linguagem acessível, gratuita, multi-paradigma, multi-plataforma, com uma sintaxe clara, e sem grandes complicações com o sistema de tipos. Possui uma quantidade grande de pacotes gratuitos, para uma enorme variedade de finalidades.
* É uma das linguagens mais populares entre aqueles que estão aprendendo a programar, e popular também entre programadores mais experientes [fonte](https://survey.stackoverflow.co/2022/#most-popular-technologies-language-learn), atrás somente de linguagens voltadas à web (p.e. Javascript). Possui uma grande comunidade de suporte e muita gente trabalhando para que sempre melhore.
* Não é uma linguagem sem falhas. Tarefas com uma alta necessidade de performance vão requerer abordagens diferentes, pois podem ser muito lentas em Python. Porém, há várias alternativas para contornar isso, como [Cython](https://cython.org/), [Numba](https://numba.pydata.org/) e [extensões para C e C++](https://docs.python.org/3/extending/extending.html). Porém, para as finalidades científicas cotidianas, é plenamente viável. Note também que o seu tempo é mais valioso que o tempo do computador. Uma tarefa demorar 3 segundos para ser executada em Python vs 3 millisegundos em C++ é, para nós, plenamente aceitável, visto que o tempo necessário para escrever o código em Python é significativamente menor (contanto exploração e compilação).
* *A tarefa dita a ferramenta que precisa ser utilizada*. Se Python não for uma boa escolha para a tarefa, busque outra ferramenta. Não seja extremista.

## Outras línguas muito utilizadas no meio científico

* Julia (focada em maior performance)
* R (focada em estatística)
* Matlab (focada em operações matriciais. Possui uma das melhores ajudas de qualquer linguagem, e uma coleção de pacotes extremamente úteis)
* Octave, alternativa open-source ao Matlab.
* Mathematica (focada em pesquisa matemática)
* Maple (focada em pesquisa matemática)

## Fluxograma de trabalho com Python

A maneira para trabalhar com Python é a seguinte:

1. Escrever código em um arquivo de texto (extensão `.py`).
2. Enviar texto para o executável (`python.exe`)
3. Avaliar o resultado. Não está bom? Volta a escrever
4. Se está bom, exportar os resultados se necessário

Que pode ser resumida neste [Fluxograma](Fluxograma.png).

Muitas linguagens de programação (p.e. C++) requerem que o código fonte passe por um longo processo antes que você consiga vê-lo sendo executado e obter o resultado. Diferente de várias outras linguagens, Python possui um "interpretador interativo" (REPL - **R**ead **E**valuate **P**rint **L**oop), que mistura as etapas 1 e 2 do fluxograma, que permite-lhe explorar a linguagem e realizar qualquer tarefa em tempo real. É isso que o torna ideal para análises exploratórias de dados. Uma mesma análise feita em C++ necessitaria da constante compilação do código e realização da análise *do zero*, que pode demorar muito.

Porém, utilizar o REPL torna-se rapidamente inconveniente se a edição de texto for minimamente mais complexa que uma função simples, e também se você desejar replicar os comandos executados outro dia. Uma ferramenta foi desenvolvida que mescla um editor de texto com o REPL, e foi batizado *Jupyter notebook* (em homenagem a **Ju**lia, **Pyt**hon e **R**), que será muito utilizado neste curso. O arquivo é organizado em células, que podem conter tanto texto quanto código, e cada célula de código possui um espaço para o *output* do código, como um gráfico ou uma tabela. Assim, é possível escrever o código, comentários sobre o código e as respostas tudo em um único local. A desvantagem deste tipo de arquivo é que *pode* introduzir mais hábitos de programação, e esse tema será abordado numa etapa futura do curso.

### Com o que escrever scripts Python

* Editores de texto simples (bloco de notas), mas não é recomendado, pois faltam várias características desejadas.
* Editores de texto como **Thonny**, Visual Studio Code, Sublime Text. São mais avançados, possuem ferramentas para autocompletação de código e realce de linguagem. **Visual Studio Code** é muito famoso e certamente o mais popular de todos citado aqui. VSCode possui suporte nativo a jupyter notebooks, mas os outros não possuem nenhum suporte.
* IDEs como **PyCharm** Community Edition (quem possui email educacional pode solicitar uma licença para a versão Professional gratuitamente) e Visual Studio. Possuem muitas ferramentas que auxiliam muito na elaboração de projetos mais complexos. Pecam no suporte para Jupyter Notebooks.

### Como rodar scripts Python

* Para rodar um script, é necessário ter o executável Python (`python.exe`) com os pacotes necessários acessíveis pelo executável. O executável pode estar tanto no seu computador, como na rede ou na nuvem. 
* A opção mais fácil é utilizar ferramentas da nuvem, mas há uma série de restrições e chateações quando se faz isso, começando pela lentidão e complicação para colocar seus dados junto da nuvem. Instalar localmente é, de forma geral, a maneira mais robusta de se utilizar a ferramenta.
* É necessário ter algum conhecimento de **linha de comando** para utilizar python e as ferramentas. Os *shells* comumente utilizados em Windows são `cmd.exe` e `powershell.exe`. Felizmente, os comandos que precisam ser utilizados frequentemente são poucos e simples. Aqui vai uma lista básica:
  * `cd <dir>` muda o diretório para `<dir>`. Por exemplo: `cd Downloads`, `cd ..` (`..` significa o diretório pai).
  * `dir` (ou também `ls` no powershell) lista os arquivos na pasta atual.
  * `explorer .` abre uma pasta do explorer no diretório atual (`.` significa diretório atual). Assim, tarefas mais complexas como criar pastas, renomear arquivos, etc, podem ser feitas pelo explorer.
  * Os comandos específicos para cada programa serão abordados em suas respectivas seções.

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

* Inicie uma instância do REPL
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

## Estrutura do curso

* Infelizmente, para podermos partir para exemplos de utilidade real, precisamos passar pelo aprendizado dos básicos. Isso constituirá a maior parte das aulas no começo. Descrições de variáveis, tipos, funções, loops (laços), condicionais e instalação e uso de pacotes serão abordados nessa etapa inicial. Os conceitos serão consolidados com alguns exemplos reais e inventados.
* Depois disso, passaremos para a resolução de exemplos reais junto com a introdução de certos pacotes mais utilizados na área científica, como `pandas`, `numpy`, `matplotlib`. Algumas vezes a solução "manual" será apresentada antes da solução feita pelo pacote, para entendermos melhor as funções empregadas. À medida que avançamos com os exemplos e nossa maturidade crescer, temas mais avançados serão abordados.
* Depois disso, passaremos para exemplos reais que utilizam várias técnicas ao mesmo tempo. Será fornecida uma descrição do problema e de conceitos necessários para resolvê-lo, junto com uma lista das técnicas e pacotes recomendados. A solução é fornecida, mas o objetivo é que você tente resolvê-los por conta própria, e depois comparar com as minhas soluções. Na medida do possível, utilizarei as melhores práticas que conheço nas resoluções que fornecerei.
* Após isso, com uma boa maturidade, abordaremos algumas questões de clareza e coesão de código, boas práticas, controle de versão e ambientes virtuais serão abordadas nesta etapa. Entraremos numa pequena tangente sobre como consolidar seu conhecimento em um pacote próprio que pode ser importado em arquivos futuros, como deixar seu pacote robusto com unit-tests, como escrever documentação e auto-gerar uma página com sphinx. Por fim, algumas palavras serão tecidas sobre como estruturar um estudo. Tudo será acompanhado de controle de versão com git. Cientistas, infelizmente, possuem a má fama de terem códigos ininteligíveis e mal estruturados. Pretendo que isso não seja uma crítica válida para vocês.

## Avaliação final

* Um repositório git, contendo controle de versão e a evolução do projeto, com instruções
  para rodá-lo. Pode ser:
  * Jupyter notebooks utilizados para o tratamento de dados. Neste caso, precisa ser completo,
    com os dados em si.
  * Pacote feito para agrupar funcionalidade. Neste caso, precisa de dados e de uma suite de
    unit-tests e os dados necessários. Precisa ter o setup.py ou pyproject.toml, instalar
    direto e depois rodar os unit-tests com uma coverage decente (não precisa ser 100%)
* Deve incluir especificações para criação de ambiente virtual, e instruções de como instalar e
  rodar (p.e. README.md).
* Avaliação será feita em etapas
  1. É um projeto de verdade (git ou não)?
  2. Consigo seguir as instruções e rodar?
  3. Está organizado?
  4. O código está limpo? Legível, com bons nomes de função, etc?
  5. O problema é simples demais? p.e. um hello world não vale. Sobre isso, pode mandar email que
     eu avalio se é um tema "válido".
* A avaliação será feita em etapas. Se não for projeto de verdade, não avança. Se não tiver boas instruções, não avança. Organização do código e limpeza serão avaliados juntos. Por fim, tudo será ponderado pela dificuldade. Se ficou barrado em alguma etapa, eu aviso e vc pode refazer ou consertar o problema, que reviso a nota. Sobre dificuldade do 

## Ajuda e material de referência

* Sites de pergunta e resposta:
  * /r/pythonprogramming
  * /r/learnprogramming
  * Python discord https://discord.gg/python
  * Stackoverflow
    * Cuidados com este em especial, na hora de fazer perguntas
  * ChatGPT
* Sites com material escrito
  * https://docs.python.org/3/
  * https://www.realpython.com
  * https://software-carpentry.org/lessons/
  * https://goodresearch.dev/
  * https://the-turing-way.netlify.app/index.html
  * https://merely-useful.tech/py-rse/index.html
  * https://coderefinery.org/lessons/core/#self-study-workshop
  * https://weisscharlesj.github.io/SciCompforChemists/intro.html
* Ferramentas
  * www.regex101.com - auxilia na elaboração de expressões regulares
  * https://pythontutor.com/ - auxilia na visualização de conceitos
  * www.hackerrank.com, https://leetcode.com/, https://adventofcode.com/ - Coleção de problemas para prática, de simples a complexos
* Artigos e livros
  * https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510
  * [Automating the Boring Stuff with Python](https://automatetheboringstuff.com/)
  * [Python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
  * [Fluent Python](https://www.fluentpython.com/) - conteúdo muito bom, mas mais apropriado para usuários intermediários-avançados.
* Cursos
  * [Python for Everybody](https://www.coursera.org/learn/python) - gratuito para testar - curso que eu fiz para aprender sobre o tema.
  * [Automate the Boring Stuff with Python](https://www.udemy.com/course/automate/) - frequentemente fica gratuito.
  * 
* Youtube
  * Arjancodes
  * mcoding
  * https://www.youtube.com/playlist?list=PLpLblYHCzJACqaFsfQiCWp0Wqy6qG4iau
  * https://www.youtube.com/watch?v=v8o-7UICRNk e outros vídeos de conferências de Python (p.e. PyCon)
  * Um dos problemas envolvendo precisão de números de ponto flutuante: https://www.youtube.com/watch?v=nYDmBdUalgo
  * 