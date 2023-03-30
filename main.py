tableau = [["p", "i", "t", "p", "i"],
           ["a", "x", "m", "g", "d"],
           ["h", "g", "p", "m", "p"],
           ["a", "g", "h", "d", "i"],
           ["p", "x", "g", "h", "v"]]
mot = ''


def recherche_horizontale_avant(a_chercher):
    if (len(a_chercher) <= len(tableau[0])):
        trouver = {}
        cpt = 0
        for i in range(0, len(tableau)):
            mot = ''
            for j in range(0, len(tableau[0])):
                mot += "{}".format(tableau[i][j])
                if (a_chercher.lower() in mot.lower()):
                    trouver[mot+str(i)+str(j)] = {'message': {"Le mots existe dans la matrice"}, 'sens': {
                        "Horizontale à l'avant"}, "coordone": [i, j-len(a_chercher)+1, i, j]}
                    cpt += 1
                    mot = ''
        if cpt == 0:
            print("Mot inexistant dans la matrice")
        return trouver
    else:
        print("Mot inexistant dans la matrice")


def recherche_horizontale_ariere(a_chercher):
    if (len(a_chercher) <= len(tableau[0])):
        trouver = {}
        cpt = 0
        for i in range(len(tableau)-1, -1, -1):
            mot = ''
            for j in range(len(tableau[0])-1, -1, -1):
                mot += "{}".format(tableau[i][j])
                if (a_chercher.lower() in mot.lower()):
                    trouver[mot+str(i)+str(j)] = {'message': {"Le mots existe dans la matrice"}, 'sens': {
                        "Horizontale à l'arrière"}, "coordone": [i, j+len(a_chercher)-1, i, j]}
                    cpt += 1
                    mot = ''
        if cpt == 0:
            print("Mot inexistant dans la matrice")
        return trouver
    else:
        print("Mot inexistant dans la matrice")


def recherche_verticale_haut(a_chercher):
    if (len(a_chercher) <= len(tableau)):
        trouver = {}
        cpt = 0
        for i in range(len(tableau[0])-1, -1, -1):
            mot = ''
            for j in range(len(tableau)-1, -1, -1):
                mot += "{}".format(tableau[j][i])
                if (a_chercher.lower() in mot.lower()):
                    trouver[mot+str(i)+str(j)] = {'message': {"Le mots existe dans la matrice"}, 'sens': {
                        "Verticale haut"}, "coordone": [i, j+len(a_chercher)-1, i, j]}
                    cpt += 1
                    mot = ''
        if cpt == 0:
            print("Mot inexistant dans la matrice")
        return trouver
    else:
        print("Mot inexistant dans la matrice")


def recherche_verticale_bas(a_chercher):
    if (len(a_chercher) <= len(tableau)):
        trouver = {}
        cpt = 0
        for i in range(len(tableau[0])):
            mot = ''
            for j in range(len(tableau)):
                mot += "{}".format(tableau[j][i])
                if (a_chercher.lower() in mot.lower()):
                    trouver[mot+str(i)+str(j)] = {'message': {"Le mots existe dans la matrice"}, 'sens': {
                        "Verticale bas"}, "coordone": [i, j-len(a_chercher)+1, i, j]}
                    cpt += 1
                    mot = ''
        if cpt == 0:
            print("Mot inexistant dans la matrice")
        return trouver
    else:
        print("Mot inexistant dans la matrice")


def recherche_diagonale_haut_bas_droite(a_chercher):
    trouver = {}
    cpt = 0
    for i in range(len(tableau)-1, -1, -1):
        mot = ''
        indice = 0
        for u in range(i, len(tableau[0])):
            mot += "{}".format(tableau[u][indice])
            indice += 1
            if (a_chercher.lower() in mot.lower()):
                trouver[mot+str(i)+str(indice)] = {'message': {
                    "Le mots existe dans la matrice"}, 'sens': {"Verticale bas"}}
                cpt += 1
                mot = ''
    for w in range(1, len(tableau[0])):
        mot = ''
        i = 0
        for u in range(w, len(tableau[0])):
            mot += "{}".format(tableau[i][u])
            i += 1
            if (a_chercher.lower() in mot.lower()):
                trouver[mot+str(i)+str(indice)] = {'message': {
                    "Le mots existe dans la matrice"}, 'sens': {"Verticale bas"}}
                cpt += 1
                mot = ''
    if cpt == 0:
        print("Mot inexistant dans la matrice")
    return trouver



def main():
    resultat = recherche_diagonale_haut_bas_droite("px")
   # resultat = recherche_diagonale_haut_bas_droite("ag")
    print(resultat)


main()
