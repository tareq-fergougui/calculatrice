def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        operation = input("Entrez l'opération (+, -, *, /) : ")

        if operation == '+':
            resultat = nombre1 + nombre2
        elif operation == '-':
            resultat = nombre1 - nombre2
        elif operation == '*':
            resultat = nombre1 * nombre2
        elif operation == '/':
            if nombre2 != 0:
                resultat = nombre1 / nombre2
            else:
                print("Erreur : Division par zéro.")
                return
        else:
            print("Erreur : Opération non valide.")
            return

        print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à {resultat}")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

calculatrice()
