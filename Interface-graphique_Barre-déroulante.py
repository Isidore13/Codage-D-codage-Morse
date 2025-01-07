
# importation de la bibliothèque
from tkinter import *


# création et configuration de la fenêtre
fenetre = Tk()
fenetre.title("Morse Discovery")
fenetre.minsize(800, 1000)
fenetre.maxsize(800, 1000)
fenetre.iconbitmap("Logo-morse.ico")
fenetre.config(background='#add8e6')


# création du canvas
canvas = Canvas(fenetre, width=500, height=500, bg='#add8e6')
canvas.pack(side=LEFT, fill=BOTH, expand=True)


# définition de la fonction du défilement avec la molette
def scroll_canvas(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

# création de la barre de défilement
scrollbar = Scrollbar(fenetre, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# configuration du canvas pour utiliser la barre de défilement
canvas.config(yscrollcommand=scrollbar.set)

# gestion du défilement avec la molette de la souris
canvas.bind_all("<MouseWheel>", scroll_canvas)


# création d'un titre et d'un sous-titre
canvas.create_text(400, 0, text="Bienvenue sur votre application pour apprendre le Morse !", font=('Constantia 20 bold'))
canvas.create_text(400, 100, text="Ici, vous allez donc trouver tout le necessaire pour apprendre le morse,\n"
                    "c'est_à_dire connaître et retenir toutes les lettres de l'albabet :\n", font=('Century 15 bold'))

# ajout d'une image
image = PhotoImage(file="Code-morse.png")
canvas.create_image(400, 300, image=image)
canvas.pack(expand=YES)

# création de texte suplémentaire
canvas.create_text(400, 650, text="\nÀ présent, voici un tableau permettant d'associer chaque lettre à un mot\n"
                        "dans le but de les mémoriser plus facilement (et surtout de s'en souvenir) \n", font=("Century", 15))

# ajout d'une deuxième image
image2 = PhotoImage(file="Tableau-mnemotechnique.png")
canvas.create_image(600, 1200, image=image2)
canvas.pack(expand=YES)


# mise en application du programme
fenetre.mainloop()
