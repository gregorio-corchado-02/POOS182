from flask import Flask, render_template, request


#Inicialiazacion del servidor flask
app= Flask(__name__)

#Configuracion para base de datos
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"



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
        año= request.form['txtAnio']
        print(titulo,artista,año)

    return "La info del Album se ha guardado"

@app.route('/eliminar')
def eliminar():
    return "Se elimino el album"

#Lineas que ejecutan el servidor    
if __name__== '__main__':
    app.run(port= 5000, debug=True)