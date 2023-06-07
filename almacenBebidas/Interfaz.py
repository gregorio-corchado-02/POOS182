from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Logica import controladorBD
import Logica as controlador
 
controlador = controladorBD()
 
def ejecutaInsert():
    controlador.guardarproducto(nombre.get(),precio.get(),clasificacion.get(),marca.get())

def ejecutaselectu():
    usuario= controlador.consultarUsuario(varBus.get())
    for usu in usuario:
        cadena=str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    if(usuario):
        txtenc.insert(tk.INSERT,cadena)
    else:
        messagebox.showinfo("usuario no encontrado","usuario no existe en la BD")

def ejecutaconsult():
    bebidas= controlador.consultarBase()
    for i in bebidas:
        elemets = bebidas
        if(bebidas):
            tree.insert('', tk.END, text=i)
        else:
            messagebox.showinfo("usuarios no encontrados","no hay registros")

def ejecutaEdit():
    controlador.editasrProducto(idBuscada.get(), nombre2.get(), precio2.get(), clasificacion2.get(), marca2.get())

def ejecutaEliminar():
    controlador.eliminarUsuario(id3.get())

def ejecutaprom():
    datos = controlador.sacaprom()
    messagebox.showinfo("El promedio es",datos) 

ventana = tk.Tk()
ventana.title("Crud de usuarios")
ventana.geometry("500x300")
 
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')
 
pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
pestaña5 = ttk.Frame(panel)
 
titulo = tk.Label(pestaña1, text='Registro de producto', fg='blue', font=('modern',18))
titulo.pack()
 
nombre = tk.StringVar()
lblNom = tk.Label(pestaña1, text="Nombre").pack()
txtNom = tk.Entry(pestaña1, textvariable=nombre).pack()

precio = tk.StringVar()
lblPre = tk.Label(pestaña1, text="Precio").pack()
txtPre = tk.Entry(pestaña1, textvariable=precio).pack()

clasificacion = tk.StringVar()
lblCla = tk.Label(pestaña1, text="Clasificacion").pack()
txtCla = tk.Entry(pestaña1, textvariable=clasificacion).pack()
 
marca = tk.StringVar()
lblMar = tk.Label(pestaña1, text="Marca").pack()
txtMar = tk.Entry(pestaña1, textvariable=marca).pack()

btnGuardar = tk.Button(pestaña1, text="Registrar mercancia", command=ejecutaInsert)
btnGuardar.pack()

titulo2 = tk.Label(pestaña2, text='Buscar usuarios', fg='blue', font=('modern',18))
titulo2.pack()

varBus=tk.StringVar()
lblid = tk.Label(pestaña2, text="Identificador de susarios")
lblid.pack()
txtid = tk.Entry(pestaña2, textvariable=varBus)
txtid.pack()

btnBus = tk.Button(pestaña2, text="Buscar", command=ejecutaselectu).pack()
btBus = tk.Button(pestaña2, text="Promedio", command=ejecutaprom).pack()

subBus = tk.Label(pestaña2, text="Encontrado",fg="blue",font=("Modern",15)).pack()
txtenc=tk.Text(pestaña2,height=5,width=52)
txtenc.pack()

titulo3 = tk.Label(pestaña3, text='Consultar Productos', fg='blue', font=('modern',18))
titulo.pack()

tap=tk.StringVar()
txtconsul = tk.Label(pestaña3, text="Mostrar todos los productos de la base de datos")
txtconsul.pack()
btnConsult = tk.Button(pestaña3, text="Mostrar", command=ejecutaconsult).pack()
tree=ttk.Treeview(pestaña3)
tree.pack()

titulo4 = tk.Label(pestaña4, text='Editar registro', fg='blue', font=('modern',18))
titulo4.pack()

idBuscada = tk.StringVar()
lblid2 = tk.Label(pestaña4, text="Ingrese la id del producto que desee modificar")
lblid2.pack()
txtid2 = tk.Entry(pestaña4, textvariable=idBuscada)
txtid2.pack()

nombre2 = tk.StringVar()
lblNom2 = tk.Label(pestaña4, text="Nuevo Nombre")
lblNom2.pack()
txtNom2 = tk.Entry(pestaña4, textvariable=nombre2)
txtNom2.pack()
 
precio2 = tk.StringVar()
lblCon2 = tk.Label(pestaña4, text="Nueva Marca")
lblCon2.pack()
txtCon2 = tk.Entry(pestaña4, textvariable=precio2)
txtCon2.pack()

clasificacion2 = tk.StringVar()
lblCor2 = tk.Label(pestaña4, text="Nueva Clasificacion")
lblCor2.pack()
txtCor2 = tk.Entry(pestaña4, textvariable=clasificacion2)
txtCor2.pack()
 
marca2 = tk.StringVar()
lblCon2 = tk.Label(pestaña4, text="Nueva Marca")
lblCon2.pack()
txtCon2 = tk.Entry(pestaña4, textvariable=marca2)
txtCon2.pack()
 
btnGuardar2 = tk.Button(pestaña4, text="Agregar nuevos datos", command=ejecutaEdit)
btnGuardar2.pack()

titulo5 = tk.Label(pestaña5, text='Elimina Producto', fg='blue', font=('modern',18))
titulo5.pack()
id3 = tk.StringVar()
lblNom2 = tk.Label(pestaña5, text="Ingresa ID del producto a Eliminar")
lblNom2.pack()
txtCor2 = tk.Entry(pestaña5, textvariable=id3)
txtCor2.pack()
btnGuardar2 = tk.Button(pestaña5, text="Eliminar producto", command=ejecutaEliminar)
btnGuardar2.pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar Usuarios')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar Usuarios')
panel.add(pestaña5, text='Eliminar Usuario')

 
ventana.mainloop()
