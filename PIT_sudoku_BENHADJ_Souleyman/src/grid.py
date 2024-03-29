#-*-coding: utf8-*-

class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """

    @classmethod
    def from_file(cls, filename, line):
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne contenue dans un fichier.
        Pour retourner une nouvelle instance de la classe, utilisez le premier argument ``cls`` ainsi::
            return cls(arguments du constructeur)

        :param filename: Chemin d'accès vers le fichier à lire
        :param line: Numéro de la ligne à lire
        :type filename: str
        :type line: int
        :return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
        :rtype: SudokuGrid
        """
        fichier= open(filename,"r")
        for i in range(line):
            content = fichier.readline().strip('\n')
        fichier.close()
        return cls(content)



    @classmethod
    def from_stdin(cls):
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne lu depuis l'entrée standard (saisi utilisateur).
        *Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
        :return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
        :rtype: SudokuGrid
        """
        ligne = input(" Saisissez une suite de caractere de nombrentre 0 et 9 comprenant 81 caractere")
        return cls(ligne)

    def __init__(self, initial_values_str):
        """À COMPLÉTER!
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """
        a=0
        self.tab= [[0 for x in range(9)] for i in range(9)]
        if len(initial_values_str)!=81:
            raise ValueError("La chaine ne fait pas 81 caracteres")
        for i in initial_values_str:
            i=int(i)
            try :
                assert  i>=0 and i<=9
                self.tab[a%9][a//9]=int(i)
                a=a+1
            except AssertionError : 
                print("La chaine n'est pas valide")



    def __str__(self):
        """À COMPLÉTER!
        Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
        :return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
        :rtype: str
        """
        affichage =""
        for i in range(9):
            affichage = affichage+ "\n"
            for j in range(9):
                affichage = affichage + str(self.tab[j][i])+" "
        return affichage




    def get_row(self, i):
        """À COMPLÉTER!
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: list of int
        """
        ligne= [0,0,0,0,0,0,0,0,0]
        try : 
            assert i>=0 and i<9
            for x in range(9):
                ligne[x] = self.tab[x][i]
        except TypeError:
            print("Le numero de ligne doit etre un entier")
        except AssertionError:
            print("La valeur de la ligne est incorrecte")
        return ligne


    def get_col(self, j):
        """À COMPLÉTER!
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        colonne = [0,0,0,0,0,0,0,0,0]
        try :
            assert j>=0 and j<9
            for i in range(9):
                colonne[i]=self.tab[j][i]
        except TypeError : 
            print("Le numero de ligne doit etre un entier")
        except AssertionError:
            print("La valeur de la colonne est incorrecte")
        return colonne


    def get_region(self, reg_row, reg_col):
        """À COMPLÉTER!
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        a=0
        zone = [0,0,0,0,0,0,0,0,0]
        try : 
            assert reg_row>=0 and reg_row<=2 and reg_col>=0 and reg_col<=2
            for i in range(3) : 
                for j in range(3):
                    zone[a]=self.tab[3*reg_col + j][3*reg_row + i]
                    a=a+1
        except TypeError:
                print("Les coordonnees doivent etre des entiers")
        except AssertionError:
                print("Les coordonees doivent etre comprises entre 0 et 2")
        return zone      

    def get_empty_pos(self):
        """À COMPLÉTER!
        Cette méthode renvoit la position des cases vides dans la grille de Sudoku,
        sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
        *Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of tuple of int
        """
        t=(0,0)
        liste=[]
        for i in range(9):
            for j in range(9):
                if self.tab[j][i]==0:
                    t=(i,j)
                    liste.append(t)
        return liste

    def write(self, i, j, v):
        """À COMPLÉTER!
        Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
        *Variante avancée: Levez une exception si ``i``, ``j`` ou ``v``
        ne sont pas dans les bonnes plages de valeurs*
        *Variante avancée: Ajoutez un argument booléen optionnel ``force``
        qui empêche d'écrire sur une case non vide*
        :param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
        :param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
        :param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9
        """
        if type(v) is list:
            v=v[0]
        if type(i) is list:
            i=i[0]
        if type(j) is list:
            j=j[0]
        if v<=0 and v>9 and i<0 and i>8 and j<0 and j>8:
            raise ValueError("Valeur(s) incorrecte(s)")
        else: 
            self.tab[j][i]=v


    def copy(self):
        """À COMPLÉTER!
        Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
        copie **indépendante** de la grille de Sudoku.
        Vous pouvez utiliser ``self.__class__(argument du constructeur)``.
        *Variante avancée: vous pouvez aussi utiliser ``self.__new__(self.__class__)``
        et manuellement initialiser les attributs de la copie.*
        """
        liste=""
        for i in range(9) :
            for j in range(9) :
                liste=liste+str(self.tab[j][i])
        new_grille=SudokuGrid(liste)
        return new_grille
