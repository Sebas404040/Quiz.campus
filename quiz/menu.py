from quiz.acciones import definir_gemelo, definir_palindromo
def menu():
    while True:
        print ("MENU PRINCIPAL")
        print ("""
            Ingrese una opcion
               
            1.pares de numeros primos gemelos
            2.numeros primos palindromicos
            3.salir
               """)
        decision=int(input("opcion: "))

        if decision==1:
            print("pares de numeros primos")
            definir_gemelo()
        elif decision==2:
            print("numeros primos palindromicos")
            definir_palindromo
        elif decision==3:
            print("salir")
            break

menu()
    
