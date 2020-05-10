from tkinter import *
from PIL import ImageTk, Image
import sqlite3

#Se crea la base de datos si no esta creada y se inserta una tabla nueva si no existe previamente
def iniciarbd():
        conn=sqlite3.connect("Perfiles_Sqlite.db")
        c=conn.cursor()
        c.execute ("""CREATE TABLE if not exists addresses (
                nombre text,
                apellido_1 text,
                apellido_2 text,
                direccion text
                )""")
        conn.commit()
        conn.close()