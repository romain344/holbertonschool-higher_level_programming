#!/usr/bin/python3
""" import SQL et SYS """
import MySQLdb
import sys

if __name__ == "__main__":
    """ recupére les arguments de la ligne de commande """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ connecte à la base de données """
    db = MYSQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cur = db.cursor()


    """ execute la requête SQL """
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """ récupère les résultats """
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    """ ferme le curseur et la connexion """
    cur.close()
    db.close()
    