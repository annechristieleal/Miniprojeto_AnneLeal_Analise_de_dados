# Mini-Projeto Avaliativo - Análise de Dados Varejo

**Aluno:** Anne Leal
**Turma:** Analise_de_Dados_com_Python 
**Data:** 17/08/2026

## Descrição do Projeto
Este projeto consiste em uma Análise Exploratória de Dados aplicada a uma base de dados de varejo, com o objetivo de praticar técnicas de ETL e qualidade de dados, utilizando a biblioteca Pandas em Python.

## Principais Insights:
1 - A maioria dos clientes possui entre 0 e 2 filhos;
2 - O gênero com maior volume de itens vendidos é o feminino;
3 - A categoria mais vendida é a de alimentos,
4 - As linhas duplicadas não foram removidas porque, na ausência de uma coluna de quantidade, cada linha representa uma unidade do produto. Essa decisão evita a subestimação do volume de vendas.

## Como Executar
1. Certifique-se de ter Python instalado com as bibliotecas pandas e IPython.
2. Coloque o arquivo `base_varejo.csv` no mesmo diretório do script `projeto.py`.
3. Execute `python projeto.py` no terminal (ou no VsCode/Colab).
4. O script exibirá no terminal todas as etapas de limpeza e o relatório final.

## Estrutura dos Arquivos
- `projeto.py`: Script principal com todas as etapas.
- `base_varejo.csv`: Dataset original
-  `README_AnneLeal_Analise_de_Dados.md`
  
 ## Referências
- Base de dados: [Kaggle - Base Varejo](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)
- Documentação Pandas: https://pandas.pydata.org/
   
