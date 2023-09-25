# import packages
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from Results.selectionSort import (
    c, c_almost_sorted, c_inverse,
    java, java_inverse, java_almost_sorted,
    python, python_inverse, python_almost_sorted,
    typescript, typescript_inverse, typescript_almost_sorted
)

from Results.quickSort import (
    c as c_quick, c_almost_sorted as c_quick_almost_sorted, c_inverse as c_quick_inverse,
    java as java_quick, java_inverse as java_quick_inverse, java_almost_sorted as java_quick_almost_sorted,
    python as python_quick, python_inverse as python_quick_inverse, python_almost_sorted as python_quick_almost_sorted,
    typescript as type_quick, typescript_inverse as type_quick_inverse, typescript_almost_sorted as type_quick_almost_sorted
)

from Results.countingSort import (
    c as c_counting, c_almost_sorted as c_counting_almost_sorted, c_inverse as c_counting_inverse,
    java as java_counting, java_inverse as java_counting_inverse, java_almost_sorted as java_counting_almost_sorted,
    python as python_counting, python_inverse as python_counting_inverse, python_almost_sorted as python_counting_almost_sorted,
    typescript as type_counting, typescript_inverse as type_counting_inverse, typescript_almost_sorted as type_counting_almost_sorted
)


st.set_page_config(page_title='Sort Algorithms', page_icon="🦾", layout='centered', initial_sidebar_state='auto')

st.title("Sort Algorithms - Análises")


st.header("Contexto")

st.markdown(
    "Este projeto possui como finalidade efetuar a análise de desempenho de 3 classes "
    "de algoritmos de ordenação diferentes para diferentes cenários e diferentes linguagens "
    "de programação. Para este estudo, foram selecionados os algoritmos **Selection Sort, "
    "Quick Sort e Counting Sort**."
)

st.subheader("Linguagens")

st.markdown(
    """ As linguagens de programação escolhidas para efetuar tal estudo foram: 
    * **C**;
    * **Java**; 
    * **Python**;
    * **Typescript**; 
    
    OBS: Typescript como linguagem adicional."""
)

st.subheader("Cenários")

st.markdown(
    """Para cada uma das linguagens e para cada um dos três algoritmos selecionados
    foram aplicados três diferentes cenários com quatro diferentes quantidades de entradas, 
    ou seja,
    
    Cenários: 
    1. Números inteiros/reais aleatórios;
    2. Números inteiros/reais aleatórios em ordem decrescente;
    3. Números inteiros/reais aleatórios 95% ordenados;
    

    Tamanho das entradas (quantidade de dados):
    1. 1000;
    2. 10000;
    3. 100000;
    4. 1000000;
    """
)

st.subheader("Ambiente Computacional")

st.markdown(
    """ Os algoritmos foram executados em uma máquina linux com as seguintes configurações: 
    
    **Versões**
    
    * Ubuntu: 22.04.3
    * **C**: 11.4.0;
    * **Java**: openjdk 11.0.20.1; 
    * **Python**: 3.10.12;
    * **Typescript** (node): 14.17.1; 
    
    **Configurações da máquina:** 
    
    
    * Arquitetura: x86_64
    * Modo(s) operacional da CPU: 32-bit, 64-bit
    * Address sizes:              39 bits physical, 48 bits virtual
    * Ordem dos bytes:            Little Endian
    * CPU(s):                       4
    * Lista de CPU(s) on-line:    0-3
    * ID de fornecedor:             GenuineIntel
    * Nome do modelo:             Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
    * Família da CPU:           6
    * Modelo:                   142
    * Thread(s) per núcleo:     2
    * Núcleo(s) por soquete:    2
    * Soquete(s):               1
    * Step:                     9
    * CPU MHz máx.:             3500,0000
    * CPU MHz mín.:             400,0000
    * BogoMIPS:                 5799.77
    
    **Memória:**
    
    Dois dipositivos de memória:
    
    * SODIMM 4GB DDR4 2133 MT/s 1.2 V
    * SODIMM 16GB DDR4 2133 MT/s 1.2 V
    
    
    OBS: Todas as implementações nas diferentes linguagens assim como os arquivos
    que geraram os dados constam em anexo na pasta zipada codigos.zip ou no seguinte 
    endereço: https://github.com/DevLeoo/unifesp-aed-sort-algorithms
    """
)


def modified_min_max_scaling(column):
    min_val = column.min()
    max_val = column.max()
    range_val = max_val - min_val
    if range_val == 0:
        return column
    scaled_column = (column - min_val) / range_val
    return scaled_column


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(modified_min_max_scaling)


def print_chart(df: pd.DataFrame):
    # scaler = MinMaxScaler()
    # normalized = scaler.fit_transform(df)
    # normalized_df = pd.DataFrame(normalized, columns=df.columns)

    fig, ax = plt.subplots()
    #  normalized_df.plot(kind="bar", rot=0, ax=ax)
    normalized_df = normalize(df)
    normalized_df.plot(kind="bar", rot=0, ax=ax)
    ax.set_xlabel("Repetitions")
    ax.set_ylabel("Execution Time")
    ax.legend(title="Data Size")
    st.markdown("Dados coletados")
    st.dataframe(df)
    st.markdown("Descrição estatística")
    st.dataframe(df.describe())
    st.pyplot(fig)

    plt.close()


def print_comparative(
      df_c: pd.DataFrame,
      df_java: pd.DataFrame,
      df_python: pd.DataFrame,
      df_type: pd.DataFrame,
      amount: str
):
    # Create a Matplotlib figure and axis
    plt.figure(figsize=(10, 6))

    # Plot the data from each DataFrame as lines
    plt.plot(df_c[amount],  label='C')
    plt.plot(df_java[amount], label='Java')
    plt.plot(df_python[amount], label='Python')
    plt.plot(df_type[amount],  label='Typescript')

    # Add labels, title, and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(f"Tempo de execução das linguagens para {amount} entradas")
    plt.legend()

    # Show the plot
    plt.grid(True)
    st.pyplot(plt)

    plt.close()


st.header("Resultados")
st.markdown(
    """
        Todos os valores apresentados estão na grandeza de milisegundos.
        
        Dicionário de dados para as tabelas.
        
        Tabela de Dados Coletados:
        * first: primeira execução
        * second: segunda execução
        * third: terceira execução
        As colunas se referem à quantidade de dados.
        
        
        Tabela de Descrições estatísticas:
        * count: Quantidade de dados
        * mean: Média do valores
        * std: Desvio padrão
        * min: Mínimo dos valores
        * 25%: Percentil 25
        * 50%: Percentil 50
        * 75%: Percentil 75
        * max: Máximo dos valores
        
    """
)

st.title("Selection Sort")
st.title("C")

st.subheader("Cenário 1:")
print_chart(c)

st.subheader("Cenário 2:")
print_chart(c_inverse)

st.subheader("Cenário 3:")
print_chart(c_almost_sorted)

st.title("Java")
st.subheader("Cenário 1:")
print_chart(java)

st.subheader("Cenário 2:")
print_chart(java_inverse)

st.subheader("Cenário 3:")
print_chart(java_almost_sorted)

st.title("Python")
st.subheader("Cenário 1:")
print_chart(python)

st.subheader("Cenário 2:")
print_chart(python_inverse)

st.subheader("Cenário 3:")
print_chart(python_almost_sorted)

st.title("Typescript")
st.subheader("Cenário 1:")
print_chart(typescript)

st.subheader("Cenário 2:")
print_chart(typescript_inverse)

st.subheader("Cenário 3:")
print_chart(typescript_almost_sorted)


st.title("Quick Sort")
st.subheader("Cenário 1:")
print_chart(c_quick)

st.subheader("Cenário 2:")
print_chart(c_quick_inverse)

st.subheader("Cenário 3:")
print_chart(c_quick_almost_sorted)

st.title("Java")
st.subheader("Cenário 1:")
print_chart(java_quick)

st.subheader("Cenário 2:")
print_chart(java_quick_inverse)

st.subheader("Cenário 3:")
print_chart(java_quick_almost_sorted)

st.title("Python")
st.subheader("Cenário 1:")
print_chart(python_quick)

st.subheader("Cenário 2:")
print_chart(python_quick_inverse)

st.subheader("Cenário 3:")
print_chart(python_quick_almost_sorted)

st.title("Typescript")
st.subheader("Cenário 1:")
print_chart(type_quick)

st.subheader("Cenário 2:")
print_chart(type_quick_inverse)

st.subheader("Cenário 3:")
print_chart(type_quick_almost_sorted)

st.title("Counting Sort")
st.subheader("Cenário 1:")
print_chart(c_counting)

st.subheader("Cenário 2:")
print_chart(c_counting_inverse)

st.subheader("Cenário 3:")
print_chart(c_counting_almost_sorted)

st.title("Java")
st.subheader("Cenário 1:")
print_chart(java_counting)

st.subheader("Cenário 2:")
print_chart(java_counting_inverse)

st.subheader("Cenário 3:")
print_chart(java_counting_almost_sorted)

st.title("Python")
st.subheader("Cenário 1:")
print_chart(python_counting)

st.subheader("Cenário 2:")
print_chart(python_counting_inverse)

st.subheader("Cenário 3:")
print_chart(python_counting_almost_sorted)

st.title("Typescript")
st.subheader("Cenário 1:")
print_chart(type_counting)

st.subheader("Cenário 2:")
print_chart(type_counting_inverse)

st.subheader("Cenário 3:")
print_chart(type_counting_almost_sorted)

st.title("Comparativo")

st.title("Selection Sort")

st.subheader("Cenário 1")
print_comparative(c, java, python, typescript, "1000")
print_comparative(c, java, python, typescript, "10000")
print_comparative(c, java, python, typescript, "100000")
print_comparative(c, java, python, typescript, "1000000")

st.subheader("Cenário 2")
print_comparative(c_inverse, java_inverse, python_inverse, typescript_inverse, "1000")
print_comparative(c_inverse, java_inverse, python_inverse, typescript_inverse,  "10000")
print_comparative(c_inverse, java_inverse, python_inverse, typescript_inverse,  "100000")
print_comparative(c_inverse, java_inverse, python_inverse, typescript_inverse,  "1000000")

st.subheader("Cenário 3")
print_comparative(c_almost_sorted, java_almost_sorted, python_almost_sorted, typescript_almost_sorted, "1000")
print_comparative(c_almost_sorted, java_almost_sorted, python_almost_sorted, typescript_almost_sorted,  "10000")
print_comparative(c_almost_sorted, java_almost_sorted, python_almost_sorted, typescript_almost_sorted,  "100000")
print_comparative(c_almost_sorted, java_almost_sorted, python_almost_sorted, typescript_almost_sorted, "1000000")


st.title("Quick Sort")
st.subheader("Cenário 1:")
print_comparative(c_quick, java_quick, python_quick, type_quick, "1000")
print_comparative(c_quick, java_quick, python_quick, type_quick, "10000")
print_comparative(c_quick, java_quick, python_quick, type_quick, "100000")
print_comparative(c_quick, java_quick, python_quick, type_quick, "1000000")

st.subheader("Cenário 2:")
print_comparative(c_quick_inverse, java_quick_inverse, python_quick_inverse, type_quick_inverse, "1000")
print_comparative(c_quick_inverse, java_quick_inverse, python_quick_inverse, type_quick_inverse, "10000")
print_comparative(c_quick_inverse, java_quick_inverse, python_quick_inverse, type_quick_inverse, "100000")
print_comparative(c_quick_inverse, java_quick_inverse, python_quick_inverse, type_quick_inverse, "1000000")

st.subheader("Cenário 3:")
print_comparative(c_quick_almost_sorted, java_quick_almost_sorted, python_quick_almost_sorted, type_quick_almost_sorted, "1000")
print_comparative(c_quick_almost_sorted, java_quick_almost_sorted, python_quick_almost_sorted, type_quick_almost_sorted, "10000")
print_comparative(c_quick_almost_sorted, java_quick_almost_sorted, python_quick_almost_sorted, type_quick_almost_sorted, "100000")
print_comparative(c_quick_almost_sorted, java_quick_almost_sorted, python_quick_almost_sorted, type_quick_almost_sorted, "1000000")

st.title("Counting Sort")
st.subheader("Cenário 1:")
print_comparative(c_counting, java_counting, python_counting, type_counting, "1000")
print_comparative(c_counting, java_counting, python_counting, type_counting, "10000")
print_comparative(c_counting, java_counting, python_counting, type_counting, "100000")
print_comparative(c_counting, java_counting, python_counting, type_counting, "1000000")

st.subheader("Cenário 2:")
print_comparative(c_counting_inverse, java_counting_inverse, python_counting_inverse, type_counting_inverse, "1000")
print_comparative(c_counting_inverse, java_counting_inverse, python_counting_inverse, type_counting_inverse, "10000")
print_comparative(c_counting_inverse, java_counting_inverse, python_counting_inverse, type_counting_inverse, "100000")
print_comparative(c_counting_inverse, java_counting_inverse, python_counting_inverse, type_counting_inverse, "1000000")

st.subheader("Cenário 3:")
print_comparative(c_counting_almost_sorted, java_counting_almost_sorted, python_counting_almost_sorted, type_counting_almost_sorted, "1000")
print_comparative(c_counting_almost_sorted, java_counting_almost_sorted, python_counting_almost_sorted, type_counting_almost_sorted, "10000")
print_comparative(c_counting_almost_sorted, java_counting_almost_sorted, python_counting_almost_sorted, type_counting_almost_sorted, "100000")
print_comparative(c_counting_almost_sorted, java_counting_almost_sorted, python_counting_almost_sorted, type_counting_almost_sorted, "1000000")

st.title("Conclusão")

st.markdown(
    "Analisando categoricamente as linguagens e algoritmos, foi observado que para o **selectio sort** em C"
    "obtivemos o melhor resultado para comparações até N=1000 e N=10000 entradas em um contexto geral, "
    "mas não se destacou em nenhum cenário, para Java, no início de cada cenário (1000 entradas), java teve um tempo "
    "de execução até que alto, porém no desenvolver e conforme aumentava o número de entradas, Java teve uma "
    "estabilização e se destaca para entrada de grandes entradas como a de 1 milhão. Com Python, apenas no primeiro "
    "valor python pode ser equiparado, no demais python se demonstrou uma linguagem muito lenta, o tempo de execução "
    "foi muito elevado comparado às outras linguagens, para n= 1 milhão a execução do selection sort em "
    "python levou aproximadamente 9 horas para executar apenas um dos cenários. Já em typescript, até N=100000 ficou "
    "com um tempo de execução bem parecido com a linguagem C, porém, no cenário 2 typescript tomou destaque em "
    "todos os cenários"
)

st.markdown(
    "Analisando categoricamente as linguagens e algoritmos, foi observado que para o **selection sort** em C"
    "obtivemos o melhor resultado para comparações até N=1000 e N=10000 entradas em um contexto geral, "
    "mas não se destacou em nenhum cenário, para Java, no início de cada cenário (1000 entradas), java teve um tempo "
    "de execução até que alto, porém no desenvolver e conforme aumentava o número de entradas, Java teve uma "
    "estabilização e se destaca para entrada de grandes entradas como a de 1 milhão. Com Python, apenas no primeiro "
    "valor python pode ser equiparado, no demais python se demonstrou uma linguagem muito lenta, o tempo de execução "
    "foi muito elevado comparado às outras linguagens, para n= 1 milhão a execução do selection sort em "
    "python levou aproximadamente 9 horas para executar apenas um dos cenários. Já em Typescript, até N=100000 ficou "
    "com um tempo de execução bem parecido com a linguagem C, porém, no cenário 2 typescript tomou destaque em "
    "todos os cenários."
    
    "No cenário 1, para casos pequenos (até 10000) com números aleatórios, o melhor a se usar são as linguagens "
    "compiladas observadas, mas conforme visto, Java tem uma melhoria no seu desempenho para entradas grandes e "
    "python só houve um decrescimento escalar no desempenho, visto também que selection sort é um algoritmo de "
    "complexidade quadrática. No cenário 2, até 1000 números as linguagens compiladas  ainda se destacaram, "
    "porém não pode-se observar uma grande diferença para o tipo de linguagem, mas nesse cenário typescript "
    "ganhou destaque em todos os casos de entradas. O cenário 3 teve um comportamento bem similar ao cenário 1 e 2, "
    "sendo Java a linguagem de destaque. C e Typescript tiveram um comportamento similar até 10000 valores, porém "
    "typescript se destacou no cenário 2 e em um contexto geral Java foi a melhor linguagem observada, com isso "
    "pôde-se observar que para valores muito altos, o algoritmo tem um tempo de execução constante, sem variar muito"
)

st.markdown(
    "Para o **Quick Sort**, foi observado que C comparando a média dos cenários até N=10.000, performou melhor para "
    "o teste 1, já para n>=100.000 o algoritmo performou melhor no cenário 2. Em Java, comparando as médias de tempo o "
    "cenário com n = 1.000 foi similar para todos os testes, já com n maiores o Java Executou o cenário 1 em menor "
    "tempo. Em Python, o cenário 1 teve a melhor performance para N=1.000 já para 10 mil e 100 mil o cenário que "
    "performou melhor foi o 3, por fim, para N= 1 milhão o cenário que teve melhor tempo foi o 2, no geral o cenário "
    "com pior desempenho foi o 1. Já com Typescript, nesse caso ele teve muitos valores zerados que foram adotados "
    "tendo em vista que o algoritmo apresentou **stack overflow**, para entradas muito grandes, porém se feito uma "
    "análise dos primeiros dados em comparação aos outros e as linguagens também, typescript teve um tempo de execução "
    "elevado"
    "Para o cenário 1, C foi a linguagem com a melhor performance para todos os valores de N, já Python teve um "
    "comportamento interessante: para n= 1.000 foi o segundo melhor, seguido do Typescript e Java; para n= 10 mil já "
    "era o 3º lugar só na frente do Java e para n>= 100 mil python foi a linguagem mais lenta. Para o Cenário 2"
    "as linguagens têm o mesmo comportamento de performance mudando apenas suas grandezas de velocidade."
    "Para o Cenário 3: mesmo com muitos valores zerados, em comparação às demais linguagens python teve o pior "
    "resultado enquanto a linguagem C teve a melhor performance."
    
    "Comparando as linguagens entre si, C teve de longe a melhor performance das linguagens testadas para todos os "
    "valores de N e para todos os cenários de teste, python teve uma boa performance para casos de n=1.000 mas sempre "
    "a pior performance valores grandes de N; Typescript foi a segunda melhor linguagem seguida de Java. No geral o "
    "cenário 1 foi o mais rápido para n=1.000 em todas as linguagens"
)

st.markdown(
    "Para o **Counting Sort**, notamos que em C, no geral os cenários tiveram tempos de execução parecidos, "
    "a discrepância maior acontece no cenário 1 quando N = 1 milhão, onde ele foi o cenário mais lento, seguido "
    "do 3º e 2º cenário foi o mais rápido; Para N=1 mil o cenário 2 e 3 executaram na mesma velocidade e o cenário 1 "
    " foi o mais lento novamente; para n=10 mil o cenário mais rápido foi o 3 e o pior o 2. e por fim para o caso "
    "de n= 100 mil o cenário com melhor performance foi o 1º e o pior o 2º. Os cenários realizados em Java obtiveram "
    "velocidades de execução muito semelhantes para dado N, não houve nenhuma grande discrepância de valores. "
    "Para n= 1 mil o cenário 2 foi o melhor e o 3 o pior; para n=10 mil os cenários 1 e 3 tiveram valores de "
    "execução iguais e o cenário 2 foi o mais lento; para n=100 mil  e n=1 milhão o cenário 1 executou mais rápido "
    "e o cenário 3 foi mais lento. Em Python, novamente, os cenários testados foram executados em tempos semelhantes, "
    "as maiores discrepâncias aparecem somente para n=1 milhão. para n= 1 mil as velocidades são próximas às obtidas "
    "nos testes em C, sendo o cenário 3 o mais rápido e o cenário 1 o mais lento; todos os cenários tiveram tempos "
    "iguais para n=10 mil; o melhor cenário de n= 100 mil foi o 3º e para n=1 milhão foi o 2º cenário, o pior tempo "
    "em ambos foi o cenário 1. Os cenários em Typescript também obtiveram velocidades parecidas com discrepâncias "
    "maiores aparecendo a partir de n=100 mil.Para n= 1 mil o cenário mais rápido foi o 1º e mais lento o 3º; "
    "para n=10 mil o mais rápido é o cenário 1 e os cenários 2 e 3 ficaram empatados com o mesmo tempo de execução; "
    "para n=100 mil o cenário 1 é o mais veloz e o cenário 3 é o mais lento; para n=1 milhão."
    
    "Para o cenário 1, C foi a linguagem com melhor performance para todos os valores de N, Java foi a pior linguagem "
    "em todos os casos. Python tem a segunda melhor performance para n<=10 mil, mas piora progressivamente conforme "
    "n aumenta. TypeScript assim como C teve uma performance estável para todos os valores de n, sendo a segunda "
    "melhor para valores de n>=100 mil. Para o Cenário 2 as linguagens têm o mesmo comportamento de performance "
    "comparado aos do cenário 1, novamente C é a melhor, Java a pior, python segunda melhor para n=1 mil porém é "
    "segunda pior para n >=100 mil, Typescript se mantém estável próximo a C. Para o Cenário 3 os comportamentos se "
    "repetem novamente e as linguagem têm os mesmos comportamentos explicitados para o cenário 1 e 2."
    
    "Comparando as linguagens entre si, C teve de longe a melhor performance das linguagens testadas para todos os "
    "valores de N e para todos os cenários, python teve uma boa performance para casos de n=1.000 mas sempre a piora "
    "sua performance para valores grandes de N; Typescript foi a segunda melhor linguagem sempre se mantendo em uma "
    "velocidade próxima de C e Java por fim em todos os cenários e para todos os valores de N foi a linguagem com "
    "execução mais lenta. Mesmo com algumas diferenças de velocidade entre as linguagens, todos os 3 cenários tiveram "
    "velocidades muito parecidas quando executados em uma mesma linguagem para um mesmo valor de N, mostrando assim "
    "que para uma mesma quantidade de valores a velocidade de ordenação é parecida para os três cenários."
)

st.title("Conclusão Geral")
st.markdown(
    "Counting sort e quick sort tiveram um tempo de execução bem similar no geral, porém a diferença só observada "
    "para valores altos, como N = 1000000, mas como estudado existe diferença na complexidade dos algoritmos e o "
    "counting sort que possui complexidade linear tem um destaque quando tende ao infinito comparado a complexidades "
    "O(n logn) e O(n²), que são respectivamente quick sort e selection sort. Em conclusão geral, a escolha entre esses "
    "algoritmos depende das características específicas do problema em questão. O Quicksort é uma boa opção para "
    "ordenação em geral, o Counting Sort é melhor quando os valores são pequenos e conhecidos, enquanto o selection "
    "é melhor para implementações simples e didáticas, visto sua simplicidade. Também a comparação de linguagem e a "
    "complexidade do algoritmo, como por exemplo python que teve o pior resultado disparado em selection sort, mas "
    "obteve resultados próximos da linguagem C no Quicksort para n = 1 mil, por isso, conhecer o problema, o conjunto "
    "de dados e os recursos de processamento disponíveis é importante para a escolha do algoritmo e a sua linguagem "
    "de implementação."
)