from tkinter import *
import random
import customtkinter as ctk
"""
jeu de pierre feuille ciseau
fait avec tkinter

"""

def ordinateur(user):
    a=random.randrange(1,4)
    users=user
    if a==1 and users=="pierre":
        result['text']="vous avez tous choisit pierre"
    else:
        result['text']="vous avez perdu"
    


fen =Tk()
fen['bg']="white"
fen.geometry("+500+500")
BPierre=Button(fen,text="pierre",bg="skyblue",command=lambda:ordinateur("pierre"))
BPierre.grid(row=1,column=1)
BFeuille=Button(fen,text="feuille",command=lambda:ordinateur("feuille"))
BFeuille.grid(row=1,column=2)
BCiseau=Button(fen,text="ciseau",command=lambda:ordinateur("ciseau"))
BCiseau.grid(row=1,column=3)
ULabel=Label(fen,text="utilisateur",bg="white")
ULabel.grid(row=2,column=0,padx=15, pady=15)
PcLabel=Label(fen,text="ordinateurs",bg="white")
PcLabel.grid(row=2,column=4)
result=Label(fen,text="il vous reste ",bg="white")
result.grid(row=3,column=2)

#il faut toujour lancer le main loop

fen.mainloop()




