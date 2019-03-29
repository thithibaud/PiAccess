from tkinter import *
from tkinter.messagebox import * # boîte de dialogue
import pyqrcode
import random
import pypng

def generation_mdp():
        reserve = "abcdefghijklmnopqrstuvwxyz0123456789"
        
        def chiffre_ou_lettre():
                nb = random.randint(0,35)
                return reserve[nb]
        
        code_utilisateur = ""
        
        compteur = 0
        while compteur < 25:
                code_utilisateur = code_utilisateur + chiffre_ou_lettre()
                compteur = compteur + 1
                
        def get_nom():
                return (nom_utilisateur.get())  
                      
        # création du QR code 
        pic = pyqrcode.create(code_utilisateur)
        pic.png(get_nom(), scale=8)
        
        
        #A TESTER
        #pic.save(get_nom())   
        #OU
        #pic.png(get_nom()".png", scale=8)
        #installer module png
        
      
        

        
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Identification requise')

# Création d'un widget Label (texte "Nom d'utilisateur")
Label1 = Label(Mafenetre, text = "Nom d'utilisateur")
Label1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
nom_utilisateur= StringVar()
Champ = Entry(Mafenetre, textvariable= nom_utilisateur, bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Générer un nouveau QR Code)
BoutonQR = Button(Mafenetre, text ='Générer un nouveau QR Code', command = generation_mdp)
BoutonQR.pack(side = LEFT, padx = 5, pady = 5)

# création d'un widget Frame dans la fenêtre principale
Frame1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT,padx=10,pady=10)


Mafenetre.mainloop()


        
        

