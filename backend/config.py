import pyodbc
from flask import Flask, jsonify

app = Flask(__name__)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-JCTSONC\MSSQLSERVER01;Database=renave_db;Trusted_Connection=yes;')
#cnxn = pyodbc.connect('DRIVER=sqlServerDb;SERVER=DESKTOP-JCTSONC\MSSQLSERVER01;Trusted_Connection=yes;')


@app.route("/act1")
def act1():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 e.nombre 'Estados con mayor número de vehiculos', Count(e.cve_estados) as num_vehiculos
    From vehiculos as v
            Inner join personas as p on p.cve_personas=v.cve_personas
            Inner join estados as e on e.cve_estados=p.cve_estados
    Group by e.nombre
    Order by  Count(e.cve_estados) desc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'estado': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

#Act2

@app.route("/act3")
def act3():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 m.nombre as 'Marcas' , Count(m.cve_marcas) as num_vehiculos
    From marcas as m
            Inner join modelos as mo on mo.cve_marcas=m.cve_marcas
            Inner join vehiculos as v on v.cve_modelos=mo.cve_modelos
    Group by m.nombre
    Order by Count(m.cve_marcas)  desc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'marca': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

@app.route("/act4")
def act4():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 c.nombre as 'Colores' , Count(c.cve_colores) 
    From colores as c
            Inner join vehiculos as v on v.cve_colores=c.cve_colores
    Group by c.nombre
    Order by  Count(c.cve_colores) desc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'color': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

#Act5

@app.route("/act6") # Revisar
def act6():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 DATENAME(YEAR, fecha_fabricacion) as 'Año en el que más vehículos se fabricaron', count(fecha_fabricacion) as 'Número de vehículos'
    From vehiculos as v
    Group by DATENAME(YEAR, fecha_fabricacion) 
    Order by DATENAME(YEAR, fecha_fabricacion) desc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'year': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

@app.route("/act7")
def act7():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 e.nombre 'Estados con menor número de vehiculos', Count(e.cve_estados) as num_vehiculos
    From vehiculos as v
            Inner join personas as p on p.cve_personas=v.cve_personas
            Inner join estados as e on e.cve_estados=p.cve_estados
    Group by e.nombre
    Order by  Count(e.cve_estados) asc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'estado': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

#   Act8

@app.route("/act9")
def act9():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 m.nombre as 'Marcas' , Count(m.cve_marcas) as num_vehiculos
    From marcas as m
            Inner join modelos as mo on mo.cve_marcas=m.cve_marcas
            Inner join vehiculos as v on v.cve_modelos=mo.cve_modelos
    Group by m.nombre
    Order by Count(m.cve_marcas) asc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'marca': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

@app.route("/act10")
def act10():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select top 10 c.nombre as 'Colores' , Count(c.cve_colores) as num_vehiculos
    From colores as c
            Inner join vehiculos as v on v.cve_colores=c.cve_colores
    Group by c.nombre
    Order by  Count(c.cve_colores) asc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'color': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)

#   act 11

@app.route("/act12") # Revisar
def act12():
    cursor = cnxn.cursor()
    autos = cursor.execute("""
    Select TOP 10 DATENAME(YEAR, fecha_fabricacion) as 'Año en el que más vehículos se fabricaron', count(fecha_fabricacion) as 'Número de vehículos'
    From vehiculos as v
    Group by DATENAME(YEAR, fecha_fabricacion) 
    Order by DATENAME(YEAR, fecha_fabricacion) asc
    """).fetchall()
    autosList = []
    for auto in autos:
        autosList.append(
            {
                'year': auto[0],
                'num_autos': auto[1],
            }
        )
    return jsonify(autosList)
