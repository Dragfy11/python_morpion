import sys


class morpion:
    def __init__(self):
        self.jeu   = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.joueur = ""
        self.ordi   = ""

        print("\n\t Jeu Morpion")
        print("\t--------------------")
        print("\n\n")

    def choix_pion(self):

        print("Choisissez entre X et 0 pour décider qui commence (O)")

        while (self.joueur != "O" and self.joueur != "X"):
            self.joueur = input("Est-ce que vous jouez O ou X ? ==>  ").upper()

        if self.joueur == "O":
            self.ordi = "X"
        else:
            self.ordi = "O"
            # L'ordinateur joue son premier coup
            self.jeu_ordi()

    def tour_de_jeu(self):
        jeu_en_cours = True

        while(jeu_en_cours):
            self.affiche_jeu()
            self.jeu_joueur()
            if self.jeu_termine(self.joueur):
                jeu_en_cours = False
            else:
                self.affiche_jeu()
                self.jeu_ordi()
                if self.jeu_termine(self.ordi):
                    jeu_en_cours = False

    def affiche_jeu(self):
        print ("  " + self.jeu[1] + " | " + self.jeu[2] + " | " + self.jeu[3] + "")
        print (" -----------")
        print ("  " + self.jeu[4] + " | " + self.jeu[5] + " | " + self.jeu[6] + "")
        print (" -----------")
        print ("  " + self.jeu[7] + " | " + self.jeu[8] + " | " + self.jeu[9] + "")

    def cherche_position_gagnante(self, pion):
        if (self.jeu[1] == pion and self.jeu[2] == pion and self.jeu[3] == "3" ):
            return 3
        if (self.jeu[1] == pion and self.jeu[2] == "2"  and self.jeu[3] == pion ):
            return 2
        if (self.jeu[1] == "1"  and self.jeu[2] == pion and self.jeu[3] == pion ):
            return 1
        if (self.jeu[4] == "4"  and self.jeu[5] == pion and self.jeu[6] == pion ):
            return 4
        if (self.jeu[4] == pion and self.jeu[5] == "5"  and self.jeu[6] == pion ):
            return 5
        if (self.jeu[4] == pion and self.jeu[5] == pion and self.jeu[6] == "6" ):
            return 6
        if (self.jeu[7] == "7" and self.jeu[8] == pion and self.jeu[9] == pion ):
            return 7
        if (self.jeu[7] == pion and self.jeu[8] == "8" and self.jeu[9] == pion ):
            return 8
        if (self.jeu[7] == pion and self.jeu[8] == pion and self.jeu[9] == "9" ):
            return 9
        if (self.jeu[1] == "1" and self.jeu[4] == pion and self.jeu[7] == pion ):
            return 1
        if (self.jeu[1] == pion and self.jeu[4] == "4" and self.jeu[7] == pion ):
            return 4
        if (self.jeu[1] == pion and self.jeu[4] == pion and self.jeu[7] == "7" ):
            return 7
        if (self.jeu[2] == "2" and self.jeu[5] == pion and self.jeu[8] == pion ):
            return 2
        if (self.jeu[2] == pion and self.jeu[5] == "5" and self.jeu[8] == pion ):
            return 5
        if (self.jeu[2] == pion and self.jeu[5] == pion and self.jeu[8] == "8" ):
            return 8
        if (self.jeu[3] == "3" and self.jeu[6] == pion and self.jeu[9] == pion ):
            return 3
        if (self.jeu[3] == pion and self.jeu[6] == "6" and self.jeu[9] == pion ):
            return 6
        if (self.jeu[3] == pion and self.jeu[6] == pion and self.jeu[9] == "9" ):
            return 9
        if (self.jeu[1] == "1" and self.jeu[5] == pion and self.jeu[9] == pion ):
            return 1
        if (self.jeu[1] == pion and self.jeu[5] == "5" and self.jeu[9] == pion ):
            return 5
        if (self.jeu[1] == pion and self.jeu[5] == pion and self.jeu[9] == "9" ):
            return 9
        if (self.jeu[7] == "7" and self.jeu[5] == pion and self.jeu[3] == pion ):
            return 7
        if (self.jeu[7] == pion and self.jeu[5] == "5" and self.jeu[3] == pion ):
            return 5
        if (self.jeu[7] == pion and self.jeu[5] == pion and self.jeu[3] == "3" ):
            return 3
        return 0

    def jeu_ordi(self):
        """
        Ici l'IA du jeu ordinateur
        """
        print("\n À moi de jouer")
        # L'ordi cherche d'abord une position gagnante pour lui
        coup_ordi = self.cherche_position_gagnante(self.ordi)
        if coup_ordi == 0:
            # ensuite il vérifie que le joueur n'est pas en position de gagner
            coup_ordi = self.cherche_position_gagnante(self.joueur)
            if coup_ordi == 0:
                # reste à voir si le centre est encore libre
                if self.jeu[5] == "5":
                    coup_ordi = 5
                else :
                    # Sinon cherche le premier endroit libre
                    for i in range(10):
                        if (self.jeu[i]== str(i)):
                            coup_ordi = i
                            break
        self.jeu[coup_ordi] = self.ordi
        print("Je pose mon pion en " + str(coup_ordi))
        return

    def jeu_joueur(self):
        """
        gestion du coup du joueur, question et vérifications
        """
        coup_joueur = 0
        while (coup_joueur <= 0 or coup_joueur >9):
            coup_joueur = int(input("Où est-ce que vous placez votre pion ?  "))
            if  self.jeu[coup_joueur] != str(coup_joueur):
                print("Coup invalide, la case est prise")
                coup_joueur = 0
        self.jeu[coup_joueur] = self.joueur
        return

    def jeu_termine(self, pion):
        """
        On teste si position gagnante
        """

        if ((self.jeu[1] == pion and self.jeu[2] == pion and self.jeu[3] == pion )
        or (self.jeu[4] == pion and self.jeu[5] == pion and self.jeu[6] == pion )
        or (self.jeu[7] == pion and self.jeu[8] == pion and self.jeu[9] == pion )
        or (self.jeu[1] == pion and self.jeu[4] == pion and self.jeu[7] == pion )
        or (self.jeu[2] == pion and self.jeu[5] == pion and self.jeu[8] == pion )
        or (self.jeu[3] == pion and self.jeu[6] == pion and self.jeu[9] == pion )
        or (self.jeu[1] == pion and self.jeu[5] == pion and self.jeu[9] == pion )
        or (self.jeu[7] == pion and self.jeu[5] == pion and self.jeu[3] == pion )):
            if pion == self.joueur:
                print("\n\t Félicitation !!! Vous avez gagné !")
            else:
                print("\n\t L'ordi à gagné !!! Vous avez perdu !! ")
            return True
        else:
            for i in range(10):
                if self.jeu[i] == str(i):
                    return False
            print("\n\t Match nul...")
            return True

# JEU:

if __name__ == "__main__":
    partie = morpion()
    partie.choix_pion()

    partie.tour_de_jeu()

    print("\n Partie terminé \n")
    partie.affiche_jeu()
