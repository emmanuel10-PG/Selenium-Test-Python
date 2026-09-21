# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import this


def print_identifiant():
    # afficher les information d une personnes
    nom ='ZADI'
    prenom = 'ASSA LAGE'
    proffession ='informaticien'
    annee_ancienete = 4
    localite = 'Abidjan, Ivory Coast'

    # type des vairiables
    print(type(annee_ancienete))
    print("+++++++++++++++++++++++++++++M1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # Mtd 1 puisque annee_ancienete est en int , pour l'afficher on va le convertir en chaine de caractere avec str
    print("Informations : "+nom+" "+ prenom +" "+ proffession+" "+ str(annee_ancienete) +" "+localite+" ")

    print("+++++++++++++++++++++++++++++M2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # Mtd 2 puisque annee_ancienete est en float , on peut passer par le f" test {}" sans les +
    print(f"Informations : {nom} {prenom } {proffession} {annee_ancienete} {localite}")

def print_dictionnaire_donnee():
    informations = {
    'nom': 'ZADI',
    'prenom': 'ASSA LAGE',
    'proffession': 'informaticien',
    'annee_ancienete': 4,
    'localite': 'Abidjan, Ivory Coast'
    }
    print(informations)
    # Oubien on peut faire ceci

    ########################################################################################

    print("methode 2 : affichage de dictionnaire \n")
    print({
        'nom': 'ZADI',
        'prenom': 'ASSA LAGE',
        'proffession': 'informaticien',
        'annee_ancienete': 4,
        'localite': 'Abidjan, Ivory Coast'
    })
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # definition de la fonction
    print_identifiant()
    print("\n")
    print_dictionnaire_donnee()


