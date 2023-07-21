from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicialiazacion del servidor flask
app= Flask(__name__)

#Configuracion para base de datos
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="db_fruteria"
app.secret_key='mysecretkey'

mysql= MySQL(app)

@app.route('/')
def index():
    return render_template('Formulario.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        nombre= request.form['txtFruta']
        temporada= request.form['txtTemporada']
        precio= request.form['txtPrecio']
        stock= request.form['txtstock']
        
        CS = mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(nombre,temporada,precio,stock))
        mysql.connection.commit()
        

    flash('Fruta Agregada Correctamente')
    return render_template('TablaRegistro.html')

@app.route('/tabla')
def tabla():
    curSelect= mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
    consulta= curSelect.fetchall()
    print(consulta)
    return render_template('TablaRegistro.html',listFruta=consulta)

if __name__== '__main__':
    app.run(port= 5000, debug=True)