-- liste tout le enregistrment non vide
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;