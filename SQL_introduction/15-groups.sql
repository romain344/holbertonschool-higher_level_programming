-- lsite le score psa nonbre decroissant
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;