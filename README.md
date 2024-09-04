## Simulador de Cache
Este projeto consiste em uma simulação de memória cache utilizando três algoritmos de substituição: FIFO, LRU e LFU. O objetivo é demonstrar como cada algoritmo gerencia o uso da cache com base em diferentes padrões de acesso à memória.

## Estrutura do Projeto
O projeto é implementado em Python e simula uma cache com quatro blocos, cada um com 1 byte de capacidade. A memória principal contém os caracteres A, B, C, D, E e F, armazenados nas posições 0 a 5.

## Algoritmos de Substituição Implementados
- FIFO (First-In, First-Out): Substitui o bloco que está há mais tempo na cache.
- LRU (Least Recently Used): Substitui o bloco que foi usado menos recentemente.
- LFU (Least Frequently Used): Substitui o bloco que foi usado com menor frequência.

## Cenários de Acesso à Memória
Foram simulados três cenários de acesso à memória:

- Cenário 1: A, B, C, A, A, B, B, C, A, D, E, F, B, A, B, C, D
- Cenário 2: A, D, C, B, A, B, D, C, A, D, E, F, B, A, F, C, D
- Cenário 3: A, D, C, B, A, B, D, C, A, D, E, F, B, A, F, C, D, A, B, C, A, A, B, B, C, A, D, E, F, B, C, D, C, D
  
Cada cenário foi testado com os três algoritmos de substituição para analisar o desempenho e o comportamento da cache em situações variadas.
