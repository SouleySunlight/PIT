from grid import SudokuGrid

fichier = str(input("Saisissez le nom du fichier : "))
ligne = int(input("Numero de ligne : "))

try : 
   sudoku= SudokuGrid.from_file(fichier, ligne);
except :
    sudoku=SudokuGrid.from_stdin()

i=0
while i == 0:
    print(sudoku)
    hor=int(input("Coordonnees de l'horizontale : "))
    ver=int(input("Coordonnees de la verticale : "))
    val=int(input("Valeur : "))
    print(hor)
    while hor<0 or  hor>8:
        print("Saisissez une valeur correcte (entre 0 et 8)")
        hor=int(input("Coordonnees de l'horizontale : "))
    while ver<0 or ver>8:
        print("Saisissez une valeur correcte (entre 0 et 8)")
        ver=int(input("Coordonnees de la verticale : "))
    while val<1 or val>9:
        print("Saisissez une valeur correcte (entre 1 et 9)")
        val=int(input("Valeur : "))

    sudoku.write(ver,hor,val)
   



