from __future__ import print_function

import builtins as __builtin__

class Boite:
    def __init__(self, texte):
        self.texte = texte
        self.textComplet = ""
        self.maxTaille = 0

    def afficherLigne(self):
        for count in range(self.maxTaille):
            if(count == 0):
                self.textComplet += "+"
            self.textComplet += "-"
            if(count == (self.maxTaille - 1)):
                self.textComplet += "+"

    def afficherPartie(self,texteInterne):
        for count in range(self.maxTaille):
            if(count == 0):
                self.textComplet += "|"

            if(count < len(texteInterne)):
                self.textComplet += texteInterne[count]
            else:
                self.textComplet += " "

            if(count == (self.maxTaille - 1)):
                self.textComplet += "|"

        self.textComplet += "\n"

    def afficherTexte(self,texte):
        tab = texte.split('\n ')
        self.maxTaille = len(max(tab, key = len))
        self.afficherLigne()
        self.textComplet += "\n"
        for partie in tab:
            self.afficherPartie(partie)
        self.afficherLigne()

    def __str__(self):
        self.afficherTexte(self.texte)
        return self.textComplet


texte = "Jaime \n mon prof \n allo"

print(Boite(texte))
print(Boite("Eric fait de la merde"))
