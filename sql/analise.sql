-- 1. Criação da estrutura da tabela
CREATE TABLE alunos (
    id INT,
    nome VARCHAR(100),
    score INT,
    evasao INT
);

-- 2. Queries de Análise (Indicadores de Negócio)

-- Taxa de evasão geral
-- Calcula o percentual de alunos que abandonaram o curso em relação ao total
SELECT 
    COUNT(*) AS total,
    SUM(evasao) AS evadidos,
    ROUND(SUM(evasao) * 100.0 / COUNT(*), 2) AS taxa_evasao
FROM alunos;

-- Evasão por faixa de score
-- Segmenta os alunos para identificar em qual nível de pontuação a evasão é mais crítica
SELECT 
    CASE 
        WHEN score < 300 THEN 'Baixo'
        WHEN score BETWEEN 300 AND 600 THEN 'Médio'
        ELSE 'Alto'
    END AS faixa_score,
    COUNT(*) AS total,
    SUM(evasao) AS evadidos
FROM alunos;

-- Top alunos com maior risco
-- Identifica alunos específicos que possuem score crítico e já estão em estado de evasão
SELECT *
FROM alunos
WHERE score < 400 AND evasao = 1;

