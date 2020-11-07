c0=int(input("Ingrese numero: "))
counter=0
resultado=0
while c0!=1:
    if c0%2==0:
        resultado= c0//2
        print(resultado)
    else:
        c0=resultado
        resultado=3*c0+1
        print(resultado)
    counter+=1
    
        
print("Pasos: ", counter)
