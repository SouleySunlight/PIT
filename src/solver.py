#-*-coding: utf8-*-
from grid import SudokuGrid


class SudokuSolver:
    """Cette classe permet d'explorer les solutions d'une grille de Sudoku pour la résoudre.
    Elle fait intervenir des notions de programmation par contraintes
    que vous n'avez pas à maîtriser pour ce projet."""

    def __init__(self, grid):
        """À COMPLÉTER
        Ce constructeur initialise une nouvelle instance de solver à partir d'une grille initiale.
        Il construett les ensembles de valeurs possibles pour chaque case vide de la grille,
        en respectant les contraintes définissant un Sudoku valide.
        :param grid: Une grille de Sudoku
        :type grid: SudokuGrid
        """
        self.grid=grid
        self.dico={}
        for i in grid.get_empty_pos():
            liste=[1,2,3,4,5,6,7,8,9]
            self.dico[i]=liste


    def is_valid(self):
        """À COMPLÉTER
        Cette méthode vérifie qu'il reste des possibilités pour chaque case vide
        dans la solution partielle actuelle.
        :return: Un booléen indiquant si la solution partielle actuelle peut encore mener à une solution valide
        :rtype: bool
        """
        ok = True
        liste=self.grid.get_empty_pos()
        for i in liste : 
            if self.dico[i]==True:
                ok=False
        return ok

    def is_solved(self):
        """À COMPLÉTER
        Cette méthode vérifie si la solution actuelle est complète,
        c'est-à-dire qu'il ne reste plus aucune case vide.
        :return: Un booléen indiquant si la solution actuelle est complète.
        :rtype: bool
        """
        fini=True
        for i in self.dico.values():
            if not i==True:
                fini=False
        return fini

    def reduce_all_domains(self):
        """À COMPLÉTER
        Cette méthode devrait être appelée à l'initialisation
        et élimine toutes les valeurs impossibles pour chaque case vide.
        *Indication: Vous pouvez utiliser les fonction ``get_row``, ``get_col`` et ``get_region`` de la grille*
        """
        for i, j in self.dico.items():
            for a in self.grid.get_row(i[0]):
                if a in j:
                    j.remove(a)
            for b in self.grid.get_col(i[1]):
                colonne= self.grid.get_col(i[1])
                if b in j:
                    j.remove(b)
            for c in self.grid.get_region(i[0]//3,i[1]//3):
                zone=self.grid.get_region(i[0]//3,i[1]//3)
                if c in j:
                    j.remove(c)

    def reduce_domains(self, last_i, last_j, last_v):
        """À COMPLÉTER
        Cette méthode devrait être appelée à chaque mise à jour de la grille,
        et élimine la dernière valeur affectée à une case
        pour toutes les autres cases concernées par cette mise à jour (même ligne, même colonne ou même région).
        :param last_i: Numéro de ligne de la dernière case modifiée, entre 0 et 8
        :param last_j: Numéro de colonne de la dernière case modifiée, entre 0 et 8
        :param last_v: Valeur affecté à la dernière case modifiée, entre 1 et 9
        :type last_i: int
        :type last_j: int
        :type last_v: int
        """
        for i,j in self.dico.items():
            if i[0]==last_i:
                if last_v in j:
                    j.remove(last_v)
            if i[1]==last_j:
                if last_v in j:
                    j.remove(last_v)
            if last_i//3==i[0]//3 and last_j//3==i[1]//3:
                if last_v in j:
                     j .remove(last_v)



	

    def commit_one_var(self):
        """À COMPLÉTER
        Cette méthode cherche une case pour laquelle il n'y a plus qu'une seule possibilité.
        Si elle en trouve une, elle écrit cette unique valeur possible dans la grille
        et renvoie la position de la case et la valeur inscrite.
        :return: Le numéro de ligne, de colonne et la valeur inscrite dans la case
        ou ``None`` si aucune case n'a pu être remplie.
        :rtype: tuple of int or None
        """
        t=None
        for i,j in self.dico.items():
            if len(j)==1:
                self.grid.write([i[0]],[i[1]],[j[0]])
                t=(i[0],i[1],j[0])
                del j[0]
                break
        return t 





    def solve_step(self):
        """À COMPLÉTER
        Cette méthode alterne entre l'affectation de case pour lesquelles il n'y a plus qu'une possibilité
        et l'élimination des nouvelles valeurs impossibles pour les autres cases concernées.
        Elle répète cette alternance tant qu'il reste des cases à remplir,
        et correspond à la résolution de Sudokus dits «simple».
        *Variante avancée: en plus de vérifier s'il ne reste plus qu'une seule possibilité pour une case,
        il est aussi possible de vérifier s'il ne reste plus qu'une seule position valide pour une certaine valeur
        sur chaque ligne, chaque colonne et dans chaque région*
        """
        self.reduce_all_domains()
        t=self.commit_one_var()
        print(self.grid)
        while type(t) is tuple:
            self.reduce_domains(t[0],t[1],t[2])
            t=self.commit_one_var()
        print(self.grid)



    def branch(self):
        """À COMPLÉTER
        Cette méthode sélectionne une variable libre dans la solution partielle actuelle,
        et crée autant de sous-problèmes que d'affectation possible pour cette variable.
        Ces sous-problèmes seront sous la forme de nouvelles instances de solver
        initialisées avec une grille partiellement remplie.
        *Variante avancée: Renvoyez un générateur au lieu d'une liste.*
        *Variante avancée: Un choix judicieux de variable libre,
        ainsi que l'ordre dans lequel les affectations sont testées
        peut fortement améliorer les performances de votre solver.*
        :return: Une liste de sous-problèmes ayant chacun une valeur différente pour la variable choisie
        :rtype: list of SudokuSolver
        """
        b=10
        c=(0,0)
        branch=[]
        for x,y in self.dico.items():
            if len(y)>0 and len(y)<b:
                c=x
                b=len(y)
        for i in self.dico[c]:
            grille=self.grid.copy()
            grille.write(c[0],c[1],i)
            branch.append(grille)
        return branch
                
                    
        

    def solve(self):
        
        """
        Cette méthode implémente la fonction principale de la programmation par contrainte.
        Elle cherche d'abord à affiner au mieux la solution partielle actuelle par un appel à ``solve_step``.
        Si la solution est complète, elle la retourne.
        Si elle est invalide, elle renvoie ``None`` pour indiquer un cul-de-sac dans la recherche de solution
        et déclencher un retour vers la précédente solution valide.
        Sinon, elle crée plusieurs sous-problèmes pour explorer différentes possibilités
        en appelant récursivement ``solve`` sur ces sous-problèmes.
        :return: Une solution pour la grille de Sudoku donnée à l'initialisation du solver
        (ou None si pas de solution)
        :rtype: SudokuGrid or None
        """
        self.solve_step()
        if self.is_solved():
            return self.grid
        if self.is_valid() == False:
            return None
        
            
        
       
