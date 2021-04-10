import json
import os
import pandas as pd

'''
EJEMPLO

data = {}
data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})
    '''


#CÓDIGO DEL CSV
datos = pd.read_csv('Resultados.csv', header = 0)
#print(datos)
#datos.columns = ['Jornada','Fecha','Local','Resultado','Visitante','Ganador'] Cuando se arregle el csv
datos.columns = ['Jornada','Fecha','Local','Resultado','Visitante']
#print(datos.columns)
equipos = datos['Local']
clubes = []
for equipo in equipos:
  if equipo not in clubes:
    clubes.append(equipo)
#print ('\nEquipos de la liga: ',clubes)
#print('Número de equipos:',len(clubes),'\n')
#print(datos[['Local','Visitante']])

datos = {}
datos['equipos'] = []
cont = 0
for team in clubes:
    cont += 1
    datos['equipos'].append({
    'id': "%d" % cont,
    'name': "%s" % team
    })  

dir = 'D:/Documents/3er curso/2do cuatrimestre/Integración de sistemas informaticos/Practicas/PredictorResultados'
file_name = "data.json"

with open(os.path.join(dir, file_name), 'w', encoding='utf8') as file:
    json.dump(datos, file, ensure_ascii= False, indent=4)