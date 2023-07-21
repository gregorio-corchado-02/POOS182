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
    curSelect= mysql.connection.cursor()
    curSelect.execute('select * from albums')
    consulta= curSelect.fetchall()
    print(consulta)
    return render_template('index.html',listAlbums=consulta)

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

@app.route('/editar/<id>')
def editar(id):
    cursoeditar = mysql.connection.cursor()
    cursoeditar.execute('select * from albums where ID=%s', (id, ))
    consulId = cursoeditar.fetchone()
    return render_template('EditarAlbum.html', album = consulId)



@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        año= request.form['txtAño']
        curactualizar = mysql.connection.cursor()
        curactualizar.execute('update albums set Titulo=%s, Artista=%s, Año=%s where ID=%s', (titulo,artista,año,id))
        mysql.connection.commit()

    flash('Album Modificado Correctamente bro')
    return redirect(url_for('index'))
 


@app.route('/eliminar')
def eliminar():
    return "Se elimino el album"

if __name__== '__main__':
    app.run(port= 5000, debug=True)

#Lineas que ejecutan el servidor    
