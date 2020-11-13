c0=int(input("Ingrese numero: "))
counter=0
resultado=0
while True:
    while c0!=1:
        
        if c0%2==0:
            resultado= c0//2
            
            print(resultado)
            
        else:
            resultado=3*c0+1
            
            print(resultado)
            
        c0=resultado
        counter+=1
    break
print("Pasos: ", counter)
