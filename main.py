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


def print_comparative(amount: str):
    # Create a Matplotlib figure and axis
    plt.figure(figsize=(10, 6))

    # Plot the data from each DataFrame as lines
    plt.plot(c[amount],  label='C')
    plt.plot(java[amount], label='Java')
    plt.plot(python[amount], label='Python')
    plt.plot(typescript[amount],  label='Typescript')

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

print_comparative("1000")
print_comparative("10000")
print_comparative("100000")
print_comparative("1000000")
