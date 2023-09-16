# import packages
import streamlit as st
import pandas as pd

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
    2. Números inteiros/reais aleatórios 95% ordenados;
    3. Números inteiros/reais aleatórios em ordem decrescente;
    
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
    """
)

st.header("Resultados")

st.subheader("C")
st.subheader("Java")
st.subheader("Python")
st.subheader("Typescript")

st.header("Comparativo")
