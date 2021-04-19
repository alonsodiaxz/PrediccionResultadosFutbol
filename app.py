from flask import Flask
from flask import request, render_template, url_for, redirect, flash
from random import choice
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

global equipoLocal
global equipoVisitante
global aleatorio


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
    equipoin1 = request.form['local']
    equipoin2 = request.form['visitante']
    if equipoin1 == equipoin2:
      flash('Error, por favor elija equipos distintos')
      return redirect(url_for('diseno'))
    comentarios = request.form['Comentarios']
    aleatorio = choice([equipoin1, "empate",equipoin2]) #Genera el número aleatorio.
    equipoLocal = convertirNombre(equipoin1)
    equipoVisitante = convertirNombre(equipoin2)
    envuelveCadenaenHTML(aleatorio, equipoLocal, equipoVisitante, equipoin1, equipoin2,comentarios)
    
  return redirect(url_for('resultado'))
  
 

   
def envuelveCadenaenHTML(aleatorio, equipoLocal, equipoVisitante, equipoin1, equipoin2, comentarios):
    nombreArchivo = './templates/resultado.html'
    f = open(nombreArchivo,'w')

    aleatorio = convertirNombre(aleatorio)
    equipoin1name = convertirNombre(equipoin1)
    equipoin2name = convertirNombre(equipoin2)

    auxiliar = "<div id='resul'><h1>Resultado: {0} </h1></div> <br> <div id = 'comen'> <h2 id='co'> Pronosticos: </h2><h6 id='porra'> {1} </h6> </div> ".format(aleatorio, comentarios)
    wrapper = '{%  extends '+ "'index.html'"+' %} {% block header %} <option value='+  equipoin1 +'> '+equipoin1name+'</option> {% endblock%} {% block title %} <option value= '+equipoin2+'> '+equipoin2name+' </option> {% endblock %}{% block image %} <img  id="ImagenLocal" src="../static/img/'+equipoLocal+'.png" alt="" width="120" height="120"  align = left> <img id="ImagenVisitante" src="../static/img/'+equipoVisitante+'.png" alt="" width="120" height="120"  align = right> {% endblock %} {% block content %}'+ auxiliar+ '{% endblock content %}'

    f.write(wrapper)
    f.close()

def convertirNombre(aleatorio):
  if(aleatorio == "mad"): 
    aleatorio = "Real Madrid"
  elif(aleatorio == "vale"):
    aleatorio = "Valencia CF"
  elif(aleatorio == "vallad"):
    aleatorio ="Real Valladolid CF"
  elif(aleatorio == "eibar"):
    aleatorio = "SD Eibar"
  elif(aleatorio == "realso"):
    aleatorio = "Real Sociedad"
  elif(aleatorio == "athl"):
    aleatorio = "Athletic Club Bilbao"
  elif(aleatorio == "sev"):
    aleatorio = "Sevilla FC"
  elif(aleatorio == "barce"):
    aleatorio = "FC Barcelona"
  elif(aleatorio == "get"):
    aleatorio = "Getafe CF"
  elif(aleatorio == "celta"):
    aleatorio = "RC Celta Vigo"
  elif(aleatorio == "osasu"):
    aleatorio = "CA Osasuna"
  elif(aleatorio == "levan"):
    aleatorio = "Levante UD"
  elif(aleatorio == "grana"):
    aleatorio = "Granada CF"
  elif(aleatorio == "atlma"):
    aleatorio = "Atletico Madrid"
  elif(aleatorio == "betis"):
    aleatorio = "Real Betis"
  elif(aleatorio == "espany"):
    aleatorio = "RCD Espanyol"
  elif(aleatorio == "alave"):
    aleatorio = "Deportivo Alaves"
  elif(aleatorio == "villa"):
    aleatorio = "Villarreal CF"
  elif(aleatorio == "lega"):
    aleatorio = "CD Leganes"
  elif(aleatorio == "mall"):
    aleatorio = "RCD Mallorca"
  
  return aleatorio

app.run()

#https://www.youtube.com/watch?v=IgCfZkR8wME
#https://www.youtube.com/watch?v=D1W8H4Rkb9A&t=133s&ab_channel=FaztCode

