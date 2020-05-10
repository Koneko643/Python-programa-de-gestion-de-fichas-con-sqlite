from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import tkinter
from Perfiles import Ficha
from Init_BD import iniciarbd

#Elimina los espacios en blanco del str recibido y lo devuelve
def spdel(subject):
    palabra=subject.split()
    palabra="".join(palabra)
    return palabra

class Menu():
    def __init__(self):
        self.__menu=Tk()

        #Inicializacion de los widgets

        self.__wellcome=Label(self.__menu,text="Gestion simple de perfiles en Pyton con tkinter y sqlit3")

        self.__addbtn=Button(self.__menu,text="Añadir perfil",width=20, command=self.Add)
        self.__inspbtn=Button(self.__menu,text="Inspeccionar perfiles",width=20,command=self.Insp)

        self.__nuevo=Label(self.__menu,text="Nuevo perfil")
        self.__select=Label(self.__menu,text="Selección de perfil")
        self.__nombre=Label(self.__menu,text="Nombre")
        self.__apellido1=Label(self.__menu,text="Primer apellido")
        self.__apellido2=Label(self.__menu,text="Segundo apellido")
        self.__direccion=Label(self.__menu,text="Dirección")

        self.__cod=Label(self.__menu,text="Codigo de perfil")

        self.__nombrein=Entry(self.__menu,width=30)
        self.__apellidoin1=Entry(self.__menu,width=30)
        self.__apellidoin2=Entry(self.__menu,width=30)
        self.__direccionin=Entry(self.__menu,width=30)

        self.__codin=Entry(self.__menu,width=30)

        self.__crea=Button(self.__menu,text="Crear perfil",width=20, command=lambda: self.BDadd(self.__nombrein.get(),self.__apellidoin1.get(),self.__apellidoin2.get(),self.__direccionin.get()))
        self.__volver=Button(self.__menu,text="Volver al menu",width=20,command=self.Inicio)

        self.__selec=Button(self.__menu,text="Buscar", command=lambda: self.BDselect(self.__nombrein.get(),self.__apellidoin1.get(),self.__apellidoin2.get(),self.__direccionin.get(),self.__codin.get()))
        self.__visu=Button(self.__menu,text="Visualizar perfil",width=20, command=self.Perfil)

        self.__VarCheck=StringVar()
        self.__drop=OptionMenu(self.__menu,self.__VarCheck,[])
        
        #Se inicializa la base de datos si no se ha creado previamente
        iniciarbd()

        #Se inicia la ventana de inicio
        self.Inicio()

    def Inicio(self):

        #Caracteristicas de las ventanas
        self.__menu.title("Menu control de perfiles")
        self.__menu.iconbitmap("Icono.ico")
        self.__menu.geometry("500x150")

        #Despejar la ventade de los anteriores widgets
        self.__nuevo.grid_forget()
        self.__nombre.grid_forget()
        self.__apellido1.grid_forget()
        self.__apellido2.grid_forget()
        self.__direccion.grid_forget()
        self.__cod.grid_forget()

        self.__nombrein.grid_forget()
        self.__apellidoin1.grid_forget()
        self.__apellidoin2.grid_forget()
        self.__direccionin.grid_forget()
        self.__codin.grid_forget()

        self.__crea.grid_forget()
        self.__volver.grid_forget()

        self.__select.grid_forget()
        self.__visu.grid_forget()

        self.__selec.grid_forget()
        self.__drop.grid_forget()

        #Se reinician los valores predeterminados de los widgets
        self.__drop["menu"].delete(0,"end")
        self.__VarCheck.set("Fichas")
        self.__nombrein.delete(0,"end")
        self.__apellidoin1.delete(0,"end")
        self.__apellidoin2.delete(0,"end")
        self.__direccionin.delete(0,"end")
        self.__codin.delete(0,"end")

        #Inicializar los widgets en la ventana
        self.__wellcome.grid(row=0,column=0,columnspan=2,padx=100,pady=(40,15),sticky="ew")

        self.__addbtn.grid(row=1,column=0,padx=20)
        self.__inspbtn.grid(row=1,column=1,padx=20)
        
        self.__menu.mainloop()

    def Add(self):

        #Caracteristicas de la ventana
        self.__menu.title("Añadir perfil")
        self.__menu.geometry("400x350")

        #Despejar la ventana de los anteriores widgets
        self.__wellcome.grid_forget()

        self.__addbtn.grid_forget()
        self.__inspbtn.grid_forget()

        #Inicializan los widgets en la ventana
        self.__nuevo.grid(row=0,column=0,columnspan=2,pady=(20,10))
        self.__nombre.grid(row=1,column=0,sticky="w",padx=(50,10),pady=10)
        self.__apellido1.grid(row=2,column=0,sticky="w",padx=(50,10),pady=10)
        self.__apellido2.grid(row=3,column=0,sticky="w",padx=(50,10),pady=10)
        self.__direccion.grid(row=4,column=0,sticky="w",padx=(50,10),pady=10)
 
        self.__nombrein.grid(row=1,column=1,padx=(0,50),pady=10)
        self.__apellidoin1.grid(row=2,column=1,padx=(0,50),pady=10)
        self.__apellidoin2.grid(row=3,column=1,padx=(0,50),pady=10)
        self.__direccionin.grid(row=4,column=1,padx=(0,50),pady=10)

        self.__crea.grid(row=5,column=0,columnspan=2,pady=10)
        self.__volver.grid(row=6,column=0,columnspan=2,pady=(10,50))

    def Insp(self):

        #Caracteristicas de la venata
        self.__menu.title("Inspeccionar perfiles")
        self.__menu.geometry("400x410")

        #Despejar la ventana de los anteriores widgets
        self.__wellcome.grid_forget()

        self.__addbtn.grid_forget()
        self.__inspbtn.grid_forget()

        #Inicializar los widgets en la ventana
        self.__select.grid(row=0,column=0,columnspan=2,pady=(20,10))
        self.__nombre.grid(row=1,column=0,sticky="w",padx=(50,10),pady=10)
        self.__apellido1.grid(row=2,column=0,sticky="w",padx=(50,10),pady=10)
        self.__apellido2.grid(row=3,column=0,sticky="w",padx=(50,10),pady=10)
        self.__direccion.grid(row=4,column=0,sticky="w",padx=(50,10),pady=10)
        self.__cod.grid(row=5,column=0,sticky="w",padx=(50,10),pady=10)

        self.__nombrein.grid(row=1,column=1,padx=(0,50),pady=10)
        self.__apellidoin1.grid(row=2,column=1,padx=(0,50),pady=10)
        self.__apellidoin2.grid(row=3,column=1,padx=(0,50),pady=10)
        self.__direccionin.grid(row=4,column=1,padx=(0,50),pady=10)
        self.__codin.grid(row=5,column=1,padx=(0,50),pady=10)

        self.__selec.grid(row=6,column=0,sticky="we",padx=(50,10),pady=(1,0))
        self.__drop.grid(row=6,column=1,sticky="we",padx=(0,50))

        self.__visu.grid(row=7,column=0,columnspan=2,pady=10)

        self.__volver.grid(row=8,column=0,columnspan=2,pady=(0,50))

    def BDadd(self,nom,ap1,ap2,dire):
        nom=spdel(nom)
        ap1=spdel(ap1)
        ap2=spdel(ap2)
        dire=spdel(dire)

        #Comprueba si se han insertado datos previamente, en caso contrario se ejecuta una notificacion
        if "" == nom or "" == ap1 or "" == ap2 or "" == dire:
            messagebox.showwarning("Faltan datos","Ingrese todos los campos porfavor")
        else:

            #Sentencias que ejecutan las ordenes en la base de datos para insertar una tupla (perfil) nuevo
            conn=sqlite3.connect("Perfiles_Sqlite.db")
            c=conn.cursor()
            c.execute("INSERT INTO addresses VALUES (:nombre, :apellido_1, :apellido_2, :direccion)",
                    {
                        "nombre": nom,
                        "apellido_1": ap1,
                        "apellido_2": ap2,
                        "direccion": dire,
                    })
            conn.commit()
            conn.close()

            #Se ejecuta una notificacion para informar de la ejecucion del procedimiento
            messagebox.showinfo("Perfil creado","El perfil se ha creado correctamente")
        
    def BDselect(self,nom,ap1,ap2,dire,ident):
        nom=spdel(nom)
        ap1=spdel(ap1)
        ap2=spdel(ap2)
        dire=spdel(dire)
        ident=spdel(ident)

        #Comprueba si se han insertado todos datos previamente, en caso contrario se ejecuta una notificacion
        if "" == nom and "" == ap1 and "" == ap2 and "" == dire and ""==ident:
            messagebox.showwarning("Faltan datos","Ingrese almenos uno de los campos porfavor")
        else:

            #Dependiendo de los datos introducidos se establece la sentencia de ejecucion de la base de datos
            orden="SELECT *, oid FROM addresses WHERE"
            varios=False
            if ""!=nom:
                orden+=" addresses.nombre='"+nom+"'"
                varios=True
            if ""!=ap1:
                if varios:
                    orden+=" and"
                orden+=" addresses.apellido_1='"+ap1+"'"
                varios=True
            if ""!=ap2:
                if varios:
                    orden+=" and"
                orden+=" addresses.apellido_2='"+ap2+"'"
                varios=True
            if ""!=dire:
                if varios:
                    orden+=" and"
                orden+=" addresses.direccion='"+dire+"'"
                varios=True
            if ""!=ident:
                if varios:
                    orden+=" and"
                orden+=" addresses.oid="+ident

            #Sentencias que ejecutan las ordenes en la base de datos para buscar la tupla (perfil) seleccionado
            conn=sqlite3.connect("Perfiles_Sqlite.db")
            c=conn.cursor()
            c.execute(orden)
            records=c.fetchall()
            conn.commit()
            conn.close()

            #Actualiza el menu dropbox mostrando los resultados de la busqueda en la base de datos
            self.__drop["menu"].delete(0,"end")
            for a in records:
                selection=str(a[4])+"| "+a[0]+" "+a[1][0]+". "+a[2][0]+"."
                self.__drop["menu"].add_command(label=selection, command=tkinter._setit(self.__VarCheck, selection))
            if records:
                self.__VarCheck.set(len(records))
            else:
                self.__VarCheck.set("Sin resultados")

    def Perfil(self):

        #Se selecciona la identificacion del perfil escogido en el menu dropbox
        info=self.__VarCheck.get().split("|")
        if len(info)==2:

            #Sentencias que ejecutan las ordenes en la base de datos para mostrar la informacion de la tupa (perfil) seleccionada
            orden="SELECT *, oid FROM addresses WHERE addresses.oid="+info[0]
            conn=sqlite3.connect("Perfiles_Sqlite.db")
            c=conn.cursor()
            c.execute(orden)
            records=c.fetchall()[0]
            conn.commit()
            conn.close()

            #Se crea la ventana del perfil seleccionado previamente
            tperfil=Ficha(records)

        else:

            #En caso de error al seleccionar el perfil se muestra una notificacion
            messagebox.showwarning("Perfil inexistente","Se ha de seleccionar primero un perfil")

An=Menu()
