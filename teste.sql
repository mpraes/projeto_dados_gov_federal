-- Exemplos de como evitar uso de funções de agregação em clausulas WHERE:

--Exemplo1
SELECT coluna1, coluna2
FROM tabela
WHERE coluna1 = (SELECT MAX(coluna1) FROM tabela)

--Exemplo2
SELECT coluna1, coluna2, AVG(coluna3)
FROM tabela
GROUP BY coluna1, coluna2
HAVING AVG(coluna3) > 10

