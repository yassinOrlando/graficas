import pyodbc
from flask import Flask, jsonify

app = Flask(__name__)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-JCTSONC\MSSQLSERVER01;Database=renave_db;Trusted_Connection=yes;')
#cnxn = pyodbc.connect('DRIVER=sqlServerDb;SERVER=DESKTOP-JCTSONC\MSSQLSERVER01;Trusted_Connection=yes;')


@app.route("/")
def hello_world():
    cursor = cnxn.cursor()
    colores = cursor.execute("SELECT * FROM colores").fetchall()
    coloresList = []
    for color in colores:
        coloresList.append(
            {
                'id': color[0],
                'nombre': color[1],
            }
        )
    print(colores)
    return jsonify(coloresList)
    #return colores