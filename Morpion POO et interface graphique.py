# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 12:38:52 2025

@author: pelam
"""

from tkinter import Tk, Button, messagebox


class Jeu:
    def __init__(self): # La methode qui crée la boite "jeu"
        self.plateau = [[" " for _ in range(3)] for _ in range(3)]  # Grille vide
        self.tour = 0  # Compteur à zero
        
        
    def jouer_coup(self, ligne, colonne):  # Placer un "X" ou "O"
        if self.plateau[ligne][colonne] == " ":
            if self.tour % 2 == 0:
                self.plateau[ligne][colonne] = "X"
            else:
                self.plateau[ligne][colonne] = "O"
            self.tour += 1
            return self.plateau[ligne][colonne]   # Retourne "X" ou "O"
        return None  # Sila case est déjà prise
    
    
    def verifier_gagnant(self):     # Verifier si trois symbole alignés
        # Lignes
        for ligne in self.plateau:
            if ligne[0] == ligne[1] == ligne[2] != " ":
                return ligne[0]
                                 
        # Colonnes
        for col in range(3):
            if self.plateau[0][col] == self.plateau[1][col] == self.plateau[2][col] != " ":
                return self.plateau[0][col]


        # Diagonales
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != " ":
            return self.plateau[0][0]
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != " ":
            return self.plateau[0][2]
        return None
    
    def est_terminee(self):  # Partie finie ?
        return self.verifier_gagnant() is not None or self.tour > 8
    

class Interface:
    def __init__(self):
        self.jeu = Jeu()     # Crée une instance de Jeu
        self.fenetre = Tk()
        self.fenetre.title("Morpion")
        self.fenetre.geometry("650x648")
        self.fenetre.configure(bg="lightblue")
        
        
        self.boutons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.boutons[i][j] = Button(self.fenetre, width=13, height=6, 
                                            text=" ", font=("Arial", 20),
                                            command=lambda ligne=i, colonne=j:
                                            self.clic(ligne, colonne)) 
                self.boutons[i][j].grid(row=i, column=j)  
   
    
    def clic(self, ligne, colonne):
        symbole = self.jeu.jouer_coup(ligne, colonne)
        if symbole:
            self.boutons[ligne][colonne].config(text=symbole, state="disabled")
            print(f"Clic sur {ligne}, {colonne}")
            if self.jeu.est_terminee():
                gagnant = self.jeu.verifier_gagnant()
                if gagnant:
                    messagebox.showinfo("Fin de partie", f"{gagnant} a gagné !")
                else:
                    messagebox.showinfo("Fin de partie", "Match nul !")
                self.fenetre.destroy()
                
                
    def lancer(self):
         print("Fenetre ouverte")
         self.fenetre.mainloop()
         
         
         
if __name__ == "__main__":
   interface = Interface()
   interface.lancer()   
                



















    
 ############### Test intermédiaire de la class jeu     #######################
# jeu = Jeu()
# print(jeu.plateau)    # Vérifie que cette une grille vide
# jeu.jouer_coup(0, 0)  # Place "X" en haut à gauche
# print(jeu.plateau)    # Vérifie que [0][0] est "X"
# jeu.jouer_coup(1, 1)  # Place "O" au milieu
# print(jeu.plateau)    # Verifie que [1][1] est "O"
###############################################################################