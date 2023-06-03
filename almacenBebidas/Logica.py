from tkinter import *
import sqlite3
import bcrypt
from tkinter import messagebox

class controladorBD:

    def __init__(self):
        pass

   #Metodo oara crear conexion
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C://Users//Gregorio//Documents//GitHub//POOS182//almacenBebidas")
            print("Conectado a la base de datos")
            return conexion
        except sqlite3.OperationalError:
             print("Conectado a la base de datos")

    #Metodo oara guardar usuarios
    def guardarproducto(self,nom,pre,cla,mar,):

        #usamos una conexion
        conx = self.conexionBD()

        #validar paratros vacios
        if(nom=="" or pre=="" or cla=="" or mar==""):
            messagebox.showwarning("Formulario incompleto")
        else:
            cursor=conx.cursor()
            datos=(nom,pre,cla,mar)
            qrInsert = "insert into Bebidas(Nombre,Precio,Clasificacion,Marca)  values(?,?,?,?)"

            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showwarning("Usuario guardado")
    
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode()
        sal= bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        return conHa
    
    def consultarUsuario(self,id):
        conx=self.conexionBD()
        
        if (id==""):
            messagebox.showwarning("Cuidad","ID vacia")
        else:
            try:

                cursor=conx.cursor()
                selectQry="Select * from TBRegistrados where id="+id

                cursor.execute(selectQry)
                rsUsuario= cursor.fetchall()
                conx.close()
                return rsUsuario

            except sqlite3.OperationalError:
                print("Error Consulta")

    def consultarBase(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        selectQry="Select * from Bebidas"
        cursor.execute(selectQry)

        return cursor.fetchall()
    
    def editasrProducto(self,id2,nombre,precio,clasificacion,marca):
        conx=self.conexionBD()
        cursor=conx.cursor()
        cursor.execute("UPDATE Bebidas SET Nombre=?, Precio=?, Clasificacion=? WHERE ID=?", (nombre, precio, clasificacion,marca,id2))
        conx.commit()
        conx.close()

    def eliminarUsuario (self,id3):
        conx=self.conexionBD()
        cursor=conx.cursor()
        cursor.execute("DELETE FROM TBRegistrados WHERE ID=?", (id3,))
        conx.commit()
        conx.close()