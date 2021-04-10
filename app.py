from flask import Flask
from flask import request, render_template, url_for, redirect, flash
#import sqlite3
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True #Permite ir actualizando constantemente los cambios que vayamos haciendo en el codigo sin tener que reiniciar el servidor.

#Settings
app.secret_key = 'mysecretkey'


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
print ('\nEquipos de la liga: ',clubes)
print('Número de equipos:',len(clubes),'\n')
#print(datos[['Local','Visitante']])


#Ejemplo de interfaz con html.
@app.route('/')
def diseno():
	return render_template ('index.html')

@app.route('/add/Resultado', methods=['GET','POST'])
def resultado():
  return render_template ('resultado.html')

@app.route('/add', methods=['GET','POST'])
def add():
  if request.method == 'POST':
    local = request.form['local']
    visitante = request.form['visitante']
    print(local)
    print(visitante)
    if local == visitante:
      flash('Error, por favor elija equipos distintos')
      return redirect(url_for('diseno'))
  print(local+' : '+visitante)
  print(request.form['Comentarios'])
  return redirect(url_for('resultado'))

'''
def envuelveCadenaenHTML():

    nombreArchivo = '/templates/index.html'
    #'index.html'
    f = open(nombreArchivo,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    todo = wrapper % (programa, ahora, url, url, body)
    f.write(todo)
    f.close()
   ''' 

#return redirect(url_for('diseno'))
#'<h1>EL equipo ganador es el real madrid</h1>'

app.run()

#https://www.youtube.com/watch?v=IgCfZkR8wME
#https://www.youtube.com/watch?v=D1W8H4Rkb9A&t=133s&ab_channel=FaztCode

