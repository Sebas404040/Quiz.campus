def definir_gemelo():
    global limite
    gemelos= []
    numeros=[]
    limite=int(input("ingrese hasta que numero primo quiere llegar"))
    espacio=1 
    for k in range(espacio):
        for i in range(2, limite):
            if i % 2 !=0:
                gemelos[k]=numeros[i]
            


def definir_palindromo():
    palindromo=[]
    limite=int(input("ingrese el limite superior"))
    for i in range(10, limite):
            if i % 2 !=0:
                primo=i
                palindromo= palindromo[i]
    print (palindromo)
    return palindromo


        
        


