# 📊 Projeto: Análise de Risco de Evasão Escolar

Este projeto aplica técnicas de **Data Science** e **Análise de Comportamento** para identificar alunos com maior probabilidade de desistência. Utilizei uma base de dados simulada para criar um modelo de pontuação (score) que ajuda na tomada de decisão preventiva.

## 📁 Estrutura do Repositório
* **data/**: Contém a base de dados `basealunosscoreevasao.xlsx` utilizada nas análises.
* **sql/**: Scripts para criação de tabelas e consultas de taxas de evasão por faixa de pontuação.
* **python/**: Script para limpeza de dados (Regex), automação do cálculo de risco e geração de gráficos.

## 🛠️ Tecnologias
* **SQL**: Estruturação e extração de KPIs de negócio.
* **Python (Pandas & Matplotlib)**: Tratamento de dados e visualização.
* **VS Code**: Ambiente de desenvolvimento.

## 📉 Resultado da Análise
O gráfico abaixo demonstra que alunos na faixa de **Baixo Score** possuem uma taxa de evasão significativamente superior, validando a necessidade de intervenção imediata para perfis de "Alto Risco" (Score < 400).

![Gráfico de Evasão](imagens/grafico.png)

---
**Desenvolvido por Bruno** *Estudante de Data Science e Análise de Comportamento - UniCesumar*
