from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import time
import random
import main
 
root = Tk()
#criacao menu
menu= Menu(root)
root.config(menu=menu)
root.title("CP4-PYTHON")
root.geometry("500x500")
root.resizable(False, False)
 
 
label = Label(root, text="LISTA GERADA = NONE")
label.grid(column=0, row=1)

botao = Button(root, text="GERAR LISTA")
botao.grid(column=0, row=0)


def criarBotao():
    btnMoverMouse = Button(root, text = 'Mover Camera')                  
    btnMoverMouse.place(x=450, y=300, anchor=CENTER)
    btnMoverMouse.configure(height=5, width=15, bg="#CADFEE")
   
 
def quemSomos():
    messagebox.showinfo("Equipe?", "RENAN BEZERRA DOS SANTOS - 553228\nLUCAS ALCÂNTARA CARVALHO - 95111\nKEVEN IKE PEREIRA DA SILVA - 553215")
 
def acessarDiretorio(diretorio):
   return os.startfile(diretorio)
   
lista = []
opcao1 = Menu(menu, tearoff=0)
opcao1.add_command(label= "Gerar Lista", command= lambda: main.gerar_dados_testes(lista, 1000, 1))
label.configure(text="opa")
 
 
sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)
 
menu.add_cascade(label = "GERAR LISTA      ", menu= opcao1)
menu.add_cascade(label = "Sair", menu= sair)
 
 
root.mainloop()