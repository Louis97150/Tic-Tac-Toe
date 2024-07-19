import turtle
import math

dessin = turtle.Turtle()
annonce = turtle.Turtle()

#fonction dessinant la grille
def grille():
    #dessiner les lignes horizontales
    for i in range(2):
        dessin.penup()
        dessin.goto(-300, 100 - 200 * i)
        dessin.pendown()
        dessin.forward(600)

    dessin.right(90)

    #dessiner les lignes verticales
    for i in range(2):
        dessin.penup()
        dessin.goto(100 - 200 * i, 300)
        dessin.pendown()
        dessin.forward(600)

    #écrire des nombres dans chaque cases
    num = 1
    for i in range(3):
        for j in range(3):
            dessin.penup()
            dessin.goto(-290 + 200 *j, 280 - 200 * i)
            dessin.pendown()

            dessin.write(num, font = ('Arial',12))
            num += 1


    #mettre l'écran a jour
    ecran.update()

#fonction écrivant le X
def X(x,y):
    #aller a la bonne place
    dessin.penup()
    dessin.goto(x,y)
    dessin.pendown()

    #dessiner le X
    dessin.setheading(60)
    for i in range(2):
        dessin.forward(75)
        dessin.backward(150)
        dessin.forward(75)
        dessin.left(60)

    # mettre l'écran a jour
    ecran.update()

#fonction essayant de mettre un X
def essayer_X(ligne,colonne):
    #enlever les annonces
    annonce.clear()

    #verifier si l'espace est occupé
    if tableau[ligne][colonne] == "x" or tableau[ligne][colonne] == "o":
        #envoie un message le cas échéant
        annonce.write("On ne peut pas en mettre la", font=("Arial", 25))
        ecran.update()
    else:
        #dessiner un X au bon endroit
        X(-200 + 200 * colonne, 200 - 200 * ligne)

        #ajouter un X sur le tableau du bot
        tableau[ligne][colonne] = "x"

    #vérifier si le nouveau X fait gagner X
    if won("x"):
        #Nous dire que l'on a gagné
        annonce.goto(-97,0)
        annonce.write("Tu as gagné", font=("Arial", 25))

        #mettre l'ecran a jour et desactiver
        ecran.update()
        desactivation()

    else:
        #si X ne gagne pas on ajoute un O
        addO()

        #verifier si O gagne
        if won("o"):
            #Nous dire que l'on a perdu
            annonce.goto(-97, 0)
            annonce.write("Tu as perdu", font=("Arial", 25))

            #mettre a jour l'ecran et desctiver
            ecran.update()
            desactivation()

        #vérifier s'il y a une égalité
        elif egalite():
            # Nous dire qu'il y a égalité
            annonce.goto(-97, 0)
            annonce.write("Égalité", font=("Arial", 25))

            # mettre a jour l'ecran et desctiver
            ecran.update()
            desactivation()

def case1():
    essayer_X(0,0)
def case2():
    essayer_X(0,1)
def case3():
    essayer_X(0,2)
def case4():
    essayer_X(1,0)
def case5():
    essayer_X(1,1)
def case6():
    essayer_X(1,2)
def case7():
    essayer_X(2,0)
def case8():
    essayer_X(2,1)
def case9():
    essayer_X(2,2)

#créer une liste avec les 9 fonctions d'au-dessus
liste=[case1, case2, case3, case4, case5, case6, case7, case8, case9]

# fonction écrivant le O
def O(x,y):
    # aller a la bonne place
    dessin.penup()
    dessin.goto(x, y + 75)
    dessin.pendown()

    #dessiner le cercle
    dessin.setheading(0)
    for i in range(180):
        dessin.forward((150 * math.pi)/180)
        dessin.right(2)

    # mettre l'écran a jour
    ecran.update()

#fonction vérifiant si on gagne
def won(lettre):

    #verification horizontale ou verticale
    for i in range(3):
        if tableau[i][0] == tableau[i][1] and tableau[i][1] == tableau[i][2] and tableau[i][0] == lettre:
            return True
        if tableau[0][i] == tableau[1][i] and tableau[1][i] == tableau[2][i] and tableau[0][i] == lettre:
            return True

    #verification diagonale vers le bas
    if tableau[0][0] == tableau[1][1] and tableau[1][1] == tableau[2][2] and tableau[0][0] == lettre:
        return True

    # verification diagonale vers le bas
    if tableau[0][2] == tableau[1][1] and tableau[1][1] == tableau[2][0] and tableau[0][2] == lettre:
        return True

    else:
        #quand ce n'est pas le cas on renvoie faux
        return False

#fonction vérifiant s'il y a une égalité
def egalite():
    #compter le nombre de X dans le tableau
    compte = 0
    for i in range(3):
        for j in range(3):
            if tableau[i][j] == "x":
                compte += 1
    #vérifier les valeurs de compte
    if compte > 5:
        return True
    else:
        return False

#cette fonction ajoute un O au meilleur endroit
def addO():
    #verifier si on peut mettre un O pour gagner
    for i in range(3):
        for j in range(3):
            if tableau[i][j] == " ":
                tableau[i][j] = "o"
                if won("o"):
                    O(-200 + 200 * j, 200 - 200 * i)
                    return
                tableau[i][j] = " "
    # verifier si on peut mettre un O pour empecher X
    for i in range(3):
        for j in range(3):
            if tableau[i][j] == " ":
                tableau[i][j] = "o"
                if won("x"):
                    O(-200 + 200 * j, 200 - 200 * i)
                    return
                tableau[i][j] = " "

    #mettre un O dans un angle
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if tableau[i][j] == " ":
                tableau[i][j] = "o"
                O(-200 + 200 * j, 200 - 200 * i)
                return

    #placer un O a n'importe quelle place
    for i in range(3):
        for j in range(3):
            if tableau[i][j] == " ":
                tableau[i][j] = "o"
                O(-200 + 200 * j, 200 - 200 * i)
                return

#fonctions activant les micros-fonctions
def activation(liste):
    for i in range(9):
        ecran.onkey(liste[i], str(i + 1))

#fonctions désactivant les micros-fonctions
def desactivation():
    for i in range(9):
        ecran.onkey(None, str(i + 1))

#créer le tableau
tableau = []
for i in range(3):
    ligne = []
    for j in range(3):
        ligne.append(" ")
    tableau.append(ligne)

#Créer turtle
dessin.pensize(10)
dessin.ht()

annonce.penup()
annonce.ht()
annonce.goto(-200,0)
annonce.color("red")

#Créer l'écran
ecran = turtle.Screen()
ecran.tracer(0)

#dessiner le dessin
grille()

essayer_X(0,2)
essayer_X(1,1)
essayer_X(1,0)
# essayer_X(1,2)
print(tableau)
#dessiner X
# X(0,1)

#dessiner O
# O(0,0)

activation(liste)
ecran.listen()

turtle.done()