from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import tkinter

class Ficha():
    def __init__(self,info):
        self.__perfil= Toplevel()
        self.__perfil.resizable(False,False)

        #Se guarda la informacion del perfil en un atributo privado
        self.__informacion=info

        #Inicializacion de los widgets
        self.__nombre=Label(self.__perfil,text="Nombre")
        self.__apellido1=Label(self.__perfil,text="Primer apellido")
        self.__apellido2=Label(self.__perfil,text="Segundo apellido")
        self.__direccion=Label(self.__perfil,text="Dirección")
        self.__ident=Label(self.__perfil,text="Cod. Ident. : "+str(self.__informacion[4]))

        self.__nombrein=Entry(self.__perfil,width=30)
        self.__apellidoin1=Entry(self.__perfil,width=30)
        self.__apellidoin2=Entry(self.__perfil,width=30)
        self.__direccionin=Entry(self.__perfil,width=30)
        
        self.__nombrein.insert(0,self.__informacion[0])
        self.__apellidoin1.insert(0,self.__informacion[1])
        self.__apellidoin2.insert(0,self.__informacion[2])
        self.__direccionin.insert(0,self.__informacion[3])

        self.__modi=Button(self.__perfil,text="Modificar perfil", width=20, command= lambda: self.Mod(self.__nombrein.get(),self.__apellidoin1.get(),self.__apellidoin2.get(),self.__direccionin.get(),self.__informacion[4]))
        self.__delet=Button(self.__perfil,text="Borrar perfil", width=20, command= lambda: self.Delete(self.__informacion))

        #Se ejecuta la ventana del perfil
        self.Lobby()

    def Lobby(self):

        #Caracteristicas de las ventanas
        self.__perfil.title("Perfil: "+self.__informacion[0]+" "+self.__informacion[1]+" "+self.__informacion[2])
        self.__perfil.iconbitmap("Icono.ico")
        self.__perfil.geometry("400x330")

        #Inicializar los widgets en la ventana
        self.__ident.grid(row=0,column=0,columnspan=2,pady=(20,10))
        self.__nombre.grid(row=1,column=0,sticky="w",padx=(50,10),pady=10)
        self.__apellido1.grid(row=2,column=0,sticky="w",padx=(50,10),pady=10)
        self.__apellido2.grid(row=3,column=0,sticky="w",padx=(50,10),pady=10)
        self.__direccion.grid(row=4,column=0,sticky="w",padx=(50,10),pady=10)

        self.__nombrein.grid(row=1,column=1,padx=(0,50),pady=10)
        self.__apellidoin1.grid(row=2,column=1,padx=(0,50),pady=10)
        self.__apellidoin2.grid(row=3,column=1,padx=(0,50),pady=10)
        self.__direccionin.grid(row=4,column=1,padx=(0,50),pady=10)
        
        self.__modi.grid(row=5,column=0,columnspan=2,pady=10)
        self.__delet.grid(row=6,column=0,columnspan=2,pady=10)

        self.__perfil.mainloop()
    
    def Mod(self,nom,ad1,ad2,adr,id):

        #Sentencia sqlite para actualizar la tupla seleccionada mediante la oid
        orden="UPDATE addresses SET nombre='"+nom+"', apellido_1='"+ad1+"', apellido_2='"+ad2+"', direccion='"+adr+"' WHERE addresses.oid="+str(id)
        
        #Sentencias que ejecutan las ordenes en la base de datos
        conn=sqlite3.connect("Perfiles_Sqlite.db")
        c=conn.cursor()
        c.execute(orden)
        conn.commit()
        conn.close()

        #Se notifica la modificacion
        messagebox.showinfo("Perfil actualizado","El perfil se ha actualizado correctamente")

    def Delete(self,info):

        #Sentencia sqlite para borrar la tupla seleccionada mediante la oid
        orden="DELETE FROM addresses WHERE addresses.oid="+str(info[4])
        
        #Sentencias que ejecutan las ordenes en la base de datos
        conn=sqlite3.connect("Perfiles_Sqlite.db")
        c=conn.cursor()
        c.execute(orden)
        conn.commit()
        conn.close()

        #Se notifica la eliminacion del perdil
        messagebox.showwarning("Perfil eliminado","El perfil se ha eliminado correctamente")

        #Se borra la ventana
        self.__perfil.destroy()
