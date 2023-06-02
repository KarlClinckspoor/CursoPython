Planejo reestruturar este curso. Ele era bem simples e gostaria de deixá-lo mais atualizado e seguindo
melhores práticas.

* Adicionar exemplos de boas práticas de realização de projetos, seguindo alguns exemplos do
  "Good Research Code Handbook"
    * Adicionar exemplos de criação de ambientes virtuais com pip, virtualenv e conda
* Falar sobre testes e unit-tests
* Falar sobre como consolidar código que foi escrito em um notebook para um módulo, de forma a ser
  reutilizado no futuro.
* Falar um pouco sobre eficiência, incluir um exemplo de tomografia e como um algoritmo diferente,
  junto com certo entendimento do funcionamento do numpy, permitiu acelear a execução do código
* Falar um pouco de classes, dataclass, namedtuple, e como deixar o código com mais texto e menos
  valores absolutos o torna mais legível para você e para outros.
* Falar sobre nuances de listas e tuplas.
* Pythontutor
* Problemas frequentes em matplotlib
* Mais funções de pandas, como agrupamento
* Expressões regulares e regex101
* Diferenças de finalidade entre jupyter notebooks e arquivos .py
* Unidades com pint
* Automação com pyautogui
* Falar sobre tipos. Ints, floats, como ints são "infinitos", floats tem precisão (inclusive citar
  o vidro mucho loko do pannenkoek e do suckerpinch (?)), e como numpy tem tipos diferentes.
* Datetimes, gerar e imprimir
* f-strings, formatação de floats, de decimais
* Operadores bitwise, e como isso se junta com pandas e matplotlib
* Enums
* Typehinting. Como fazer para dataframes, matplotlib, numpy e pandas (nptyping). Validação com Pandera, Pydantic
* Logging
* Decorators (@dataclass, @property, @staticmethod, @classmethod)
* Básicos de Markdown.
    * Formatação básica
    * Em notebooks, latex.
* Docstrings, sphinx
* Arquivos do excel (xlsx), word (docx), powerpoint (pptx) são só arquivos .zip com dados em XML.
* Serialização com pickle, JSON
* Importância de seguir estilos de código.
    * Colaborações
    * Menor peso cognitivo
    * Manter uma lingua só. Inglês e português juntos me deixa confuso.
* turtle
* Estruturar o curso baseado no início em explicar os conceitos básicos e depois partir para
  exemplos e mais exemplos de problemas que já resolvi no meu tempo.


## Programmer's brain

* Memória de curto prazo, de trabalho e de longo prazo
* Agrupamento de memórias "chunking" ''''- exemplo do xadrez, "cat loves cake" vs "abk mrtpi gbar"
* Equação de perda de memória de Ebbinghaus
* Técnicas de aprendizado e retenção
* Capacidade de recall
* Sobre entender o que foi escrito e o pq algo foi escrito daquela forma
* Sobre algumas maneiras de auxiliar a memória no entendimento de um código
    * Tipos de variáveis (acumuladores, temporários, etc)
* De vez em qdo, uma mudança na visualização é o suficiente para fazer o problema ficar simples
* Criar modelos mentais

## Algoritmos e problemas

* Quantas bolinhas cabem em um recipiente
* Script para posicionamento do centro de círculos
* Binary search
* BFS e DFS, como exemplos mais pro final
* Diferentes tipos de derivadas.
* Média móvel manual vs a do pandas
* Localização de máximos de picos
* Ajustes de modelo:
    * curve_fit
    * lmfit
    * obtenção de erros padrão normal, monte-carlo
* Estatística
    * Testes estatísticos. Teste t, teste F
    * Planejamento de experimentos e regressões multilineares
    * statsmodels (modelo linear)
    * Bootstrap
* PCA, criação, visualização
* Propagação de incertezas manual, com sympy e com uncertainties
* Conversão de unidades manual e com pint
* Fazer uma GUIzinha com tkinter (https://tkdocs.com/index.html)
* Fazer um desenho em SVG e utilizar Python para alterar algum texto
* Extrair os títulos de uma sequência de resumos (utilizar o chatGPT para gerar o texto?)
* wordclouds de algum texto, talvez proj. gutemberg. Posso colocar o exemplo da minha tese de doutorado


## Matplotib

* Plot normal vs scatter
* Como mapear cores e símbolos para tipos diferenets de dados
* Como fazer degradês utilizando as cores
* Alterando os ciclos de cor. Palettable?
* Como associar as cores à um colorbar
* Um pouco sobre cartopy. Utilizar aqueles dados da Petrobras, que foi interessante, e mapas de relevo
* Contour, contourf, e como plotar uma superfície a partir de um modelo 2D e X e Y 1D.
* Como fazer animações manuais (png por png) ou pelo anim mesmo
* Legendas:
    * Dentro ou fora
    * colunas, tamanho, borda, transparência
    * Legendas com símbolos arbitrários
* 

## Pandas

* Groupby
* rolling
* datetime
* read_csv
* read_excel
* to_excel, ExcelWriter
* dataframe.plot

## Git

* Git add, commit, branch, push
* Conta no github/gitlab
* Pull requests e colaboração
* Como lidar com jupyter notebooks

## Referências

* Practical Statistics with R and Python
* Jake vanderplas
* programmer's brain
* Fluent Python
* Automate the boring stuff with Python
* data science from scratch (?)
* Arjancodes, mcoding

## Ajuda

* /r/pythonprogramming
* /r/learnprogramming
* Python discord https://discord.gg/python
* Stackoverflow
    * Cuidados com este em especial, na hora de fazer perguntas
* ChatGPT
* RealPython

## Prova final

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
* A avaliação será feita em etapas. Se não for projeto de verdade, não avança. Se não tiver boas
  instruções, não avança. Organização do código e limpeza serão avaliados juntos. Por fim, tudo
  será ponderado pela dificuldade. Se ficou barrado em alguma etapa, eu aviso e vc pode refazer
  ou consertar o problema, que reviso a nota. Sobre dificuldade do 













