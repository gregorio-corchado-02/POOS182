from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicialiazacion del servidor flask
app= Flask(__name__)

#Configuracion para base de datos
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"
app.secret_key='mysecretkey'

mysql= MySQL(app)



#Declaramos una ruta
#Declaramos ruta index http://localhost:5000
#Ruat se compone de nombre y la funcion
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        año= request.form['txtAño']
        #print(titulo,artista,año)
        CS = mysql.connection.cursor()
        CS.execute('insert into albums(Titulo,Artista,Año) values(%s,%s,%s)',(titulo,artista,año))
        mysql.connection.commit()
        

    flash('Album Agregado Correctamente bro')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino el album"

#Lineas que ejecutan el servidor    
if __name__== '__main__':
    app.run(port= 5000, debug=True)