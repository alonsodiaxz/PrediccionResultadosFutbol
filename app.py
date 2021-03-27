from flask import Flask
from flask import request, render_template, url_for, redirect, flash
#import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True #Permite ir actualizando constantemente los cambios que vayamos haciendo en el codigo sin tener que reiniciar el servidor.

#Settings
app.secret_key = 'mysecretkey'

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
    if local == visitante:
      flash('Error, por favor elija equipos distintos')
      return redirect(url_for('diseno'))
  print(local+' : '+visitante)
  return redirect(url_for('resultado'))



#return redirect(url_for('diseno'))
#'<h1>EL equipo ganador es el real madrid</h1>'

app.run()

#https://www.youtube.com/watch?v=IgCfZkR8wME
#https://www.youtube.com/watch?v=D1W8H4Rkb9A&t=133s&ab_channel=FaztCode

