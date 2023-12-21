import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

fenetre = tk.Tk()
fenetre.attributes('-fullscreen', True)
fenetre.title("Memory game")
fenetre.configure(background='black', cursor='cross')

ClickCount = 0
selected_buttons = []
selected_images = []
found_pairs = [] 
clicked_buttons = []
clicked = 0

def Images():
    global sti, egg, nani, gantu, jumba, lilo, peakly, violet, tet, det, uet, instru, up, ice
    sti = ImageTk.PhotoImage(Image.open("image/stitch.png").resize((122, 131)))
    egg = ImageTk.PhotoImage(Image.open("image/egg.png").resize((122, 131)))
    nani = ImageTk.PhotoImage(Image.open("image/NANI.png").resize((122, 131)))
    gantu = ImageTk.PhotoImage(Image.open("image/GANTU.png").resize((122, 131)))
    jumba = ImageTk.PhotoImage(Image.open("image/JUMBA.png").resize((122, 131)))
    lilo = ImageTk.PhotoImage(Image.open("image/LILO.png").resize((122, 131)))
    peakly = ImageTk.PhotoImage(Image.open("image/PEAKLY.png").resize((122, 131)))
    violet = ImageTk.PhotoImage(Image.open("image/VIOLET.png").resize((122, 131)))
    tet= PhotoImage(file="image/3_etoiles.png")
    det= PhotoImage(file="image/deux_etoiles.png")
    uet= PhotoImage(file="image/une_etoiles.png")
    instru= ImageTk.PhotoImage(Image.open("image/Instru.png").resize((350, 350)))
    up= ImageTk.PhotoImage(Image.open("image/upside.png").resize((350, 350)))
    ice= ImageTk.PhotoImage(Image.open("image/glace.png").resize((500, 350)))

Images()

label = tk.Label(fenetre, text="Bienvenue au jeu Memory !", font=('Stencil',30, "bold"))
label.pack()
label.configure(background='brown', width=25, height=2)

def Launch_game():
    global F_Game, ClickCount, selected_buttons, selected_images, found_pairs, clicked_buttons, clicked, fenetre2, up, show_instruction

    ClickCount = 0
    selected_buttons = []
    selected_images = []
    found_pairs = []
    clicked_buttons = []
    clicked = 1
    

    F_Game = Toplevel(fenetre)
    F_Game.title("Memory game")
    F_Game.attributes('-fullscreen', True)
    F_Game.configure(background='black', cursor='cross')

    Game_I = tk.Label(F_Game, text="Cliquez sur deux cases et mémorisez !", font=('Stencil',18, "bold"))
    Game_I.place(x=500)
    Game_I.configure(background='brown')
   
    label_clicks = tk.Label(F_Game, text=f"Nombre de tours: {clicked}")
    label_clicks.configure(background='brown', width=65, height=4)
    label_clicks.place(x=20, y=150)

    reset = tk.Button(F_Game, text='Recommencer ?', command=replay_game)
    reset.configure(background='brown')
    reset.place(x=20, y=45)

    kill2 = tk.Button(F_Game, text="Quitter", command=shutdown)
    kill2.configure(background='brown')
    kill2.place(x=20, y=73)

    ups = tk.Label(F_Game, image=up)
    ups.configure(background='black')
    ups.place(x=40, y=250)

    lsg = tk.Label(F_Game, image=ice)
    lsg.configure(background='black')
    lsg.place(x=1050, y=250)

    def update_labels():
        if clicked <= 2:
            lbI = tk.Label(F_Game, text="L'Homme peut vivre sous l'eau, mais pas très longtemps", font=('Stencil',15, "bold"))
            lbI.configure(background='brown', width=115, height=4)
            lbI.place(y=770)
        elif clicked > 2 and clicked <= 4:
            lbI = tk.Label(F_Game, text="Tous les champignons sont comestibles ! Mais certains qu'une seule fois...", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 4 and clicked <=6 :
            lbI = tk.Label(F_Game, text="Les relations sexuelles brûlent 360 calories par heure.", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 6 and clicked <=8 :
            lbI = tk.Label(F_Game, text="Malheureusement tu depasses pas la minute...", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 8 and clicked <=10 :
            lbI = tk.Label(F_Game, text="L'apopathodiaphulatophobie est la peur d'être constipé.", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 10 and clicked <=12 :
            lbI = tk.Label(F_Game, text="Y'en a qui ont déja terminé à ce stade là...", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 12 and clicked <=14 :
            lbI = tk.Label(F_Game, text="Si le jeu vous plait, nous acceptons la monnaie sans modération !", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 14 and clicked <=16 :
            lbI = tk.Label(F_Game, text="Sans trop de spoil, t'auras pas trois étoiles", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 16 and clicked <=18 :
            lbI = tk.Label(F_Game, text="Le vol le plus long d'une poule est de 30 secondes.", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 18 and clicked <=20 :
            lbI = tk.Label(F_Game, text="C'est plus long que certains...", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 20 and clicked <=21 :
            lbI = tk.Label(F_Game, text="J'aime ta persévérance, mais tu peux t'arrêter.", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 21 and clicked <=22 :
            lbI = tk.Label(F_Game, text="Ma cousine de 4 ans fait mieux que toi!", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        elif clicked > 22 and clicked <=23 :
            lbI = tk.Label(F_Game, text="Abandonne ... Tu as fait de ton mieux...", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)
        else :
            lbI = tk.Label(F_Game, text="L'important c'est d'essayer", font=('Stencil',15, "bold") )
            lbI.configure(background='brown',width=110, height=4)
            lbI.place(y=770)

        
        F_Game.after(1000, update_labels)

    
    update_labels()

    Instructions1 = tk.Button(F_Game, text="Instructions", command=show_instruction)
    Instructions1.configure(background='brown')
    Instructions1.place(x=20, y=101)
    
    images = [sti, egg, nani, gantu, jumba, lilo, peakly, violet] * 2
    random.shuffle(images)
    
    # On crée une fonction pour gérer le clic sur les boutons
    def on_click(btn, image):
        global ClickCount, selected_buttons, selected_images, found_pairs, clicked
        ClickCount += 1
        label_clicks.config(text=f"Nombre de tours: {clicked}")
        btn.configure(image=image, width=131, height=125)
        btn.image = image
        selected_buttons.append(btn)
        selected_images.append(image)
        clicked_buttons.append(btn)  # Ajout de l'image sélectionnée à la liste
        for btn in selected_buttons:
            btn.configure(state=DISABLED)
        if ClickCount == 2:
            clicked = clicked + 1  
            fenetre.after(300, lambda: hide_images())
            ClickCount = 0  # Réinitialise le compteur après deux clics  
                

    # On crée une fonction pour masquer les images
    def hide_images():
        if selected_images[0] == selected_images[1] and selected_buttons[0] != selected_buttons[1]:
            found_pairs.append(selected_images[0]) # Ajout de la paire trouvée à la liste
            for btn in clicked_buttons:
                btn.configure(state=DISABLED)
            if len(found_pairs) == 8:
                victory()
        else:
            for btn in selected_buttons:
                btn.configure(image='', width=18, height=8, state=NORMAL)  # Masque l'image
                btn.image = None  # Réinitialise la référence à l'image
        
        clicked_buttons.clear()
        selected_buttons.clear()
        selected_images.clear()

    # On attache la fonction on_click à tous les boutons du jeu
    for i in range(1, 5):
        for j in range(1, 5):
            current_image = images.pop()
            btn = tk.Button(F_Game, width=18, height=8, compound='center')
            btn.configure(command=lambda b=btn, i=current_image: on_click(b, i))
            btn.grid(row=i, column=j)
            btn.configure(background='brown')
            btn.place(x=500 + (j - 1) * 131, y=150 + (i - 1) * 131)

def victory():
    global clicked, tet, det, uet
    win = Toplevel(F_Game)
    win.title('Vous avez gagné !')
    win.attributes('-fullscreen', True)
    win.configure(background='black', cursor='cross')

    clicked = clicked-1

    label_win = tk.Label(win, text="Félicitations ! Vous avez trouvé toutes les paires !" )
    label_win.configure(background='brown', height=3, font=('Stencil',20, "bold"))
    label_win.pack()

    btn_replay = tk.Button(win, text="Rejouer",command=Launch_game)
    btn_replay.configure(background='brown', width=112)
    btn_replay.pack()

    btn_quit = tk.Button(win, text="Quitter", command=shutdown)
    btn_quit.configure(background='brown',width=112)
    btn_quit.pack()

    label_click = tk.Label(win, text=f"Nombre de tours: {clicked}")
    label_click.configure(background='brown', width=44, height=3, font=('Stencil',20, "bold"))
    label_click.pack()

    if clicked <=14:
        label3 = tk.Label(win, image=tet)
        label3.configure(background='black', width=100)
        label3.pack(expand=1, fill='both')
    elif clicked >14 and clicked <=20:
        label2 = tk.Label(win, image=det)
        label2.configure(background='black', width=100)
        label2.pack(expand=1, fill='both')
    else :
        label1 = tk.Label(win, image=uet)
        label1.configure(background='black', width=100)
        label1.pack(expand=1, fill='both')

def shutdown():
    global fenetre
    fenetre.destroy()

def replay_game():
    global F_Game, clicked
    F_Game.destroy()
    Launch_game()
    clicked = 1

def show_instruction():

    global instru, fenetre2

    fenetre2 = tk.Toplevel(fenetre)
    fenetre2.attributes('-fullscreen', True)
    fenetre2.title("Instructions")
    fenetre2.configure(background='black', cursor='cross')
    
    label_Instructions1 = tk.Label(fenetre2, text="Le but est de retrouver toutes les paires ! ")
    label_Instructions1.configure(background='brown', width=90, height=2, font=40)
    label_Instructions1.pack()
    
    label_Instructions2 = tk.Label(fenetre2, text="Afin d'y arriver clic sur deux cases : si c'est une paire c'est bon, sinon mémorise et recommence !")
    label_Instructions2.configure(background='brown', width=90, height=2, font=40)
    label_Instructions2.pack()
    
    label_Instructions3 =tk.Label(fenetre2, text="Pas de limite de clic, pas de limite de temps. Mais essaye de le faire avec le moins de clics possible !")
    label_Instructions3.configure(background='brown', width=90, height=2, font=40)
    label_Instructions3.pack()
    
    pic = tk.Label(fenetre2, image=instru)
    pic.configure(background="black")
    pic.pack(expand=1, fill='both')
    
    kill = tk.Button(fenetre2, text= "Quitter le jeu", command=shutdown)
    kill.configure(background='brown')
    kill.pack(side='bottom')

    Back = tk.Button(fenetre2, text="Lancer le jeu", command=Launch_game)
    Back.configure(background='brown')
    Back.pack()

Jouer = tk.Button(fenetre, text="Jouer", command=Launch_game)
Jouer.pack()
Jouer.configure(background='brown')

Instructions = tk.Button(fenetre, text="Instructions", command=show_instruction)
Instructions.pack()
Instructions.configure(background='brown')

kill1 = tk.Button(fenetre, text='Quitter ?', command=shutdown)
kill1.configure(background='brown')
kill1.pack(side='bottom')

bg = PhotoImage(file="image/gryf.png")
label1 = Label(fenetre, image=bg)
label1.configure(background='black')
label1.pack(expand=1, fill='both')

fenetre.mainloop()