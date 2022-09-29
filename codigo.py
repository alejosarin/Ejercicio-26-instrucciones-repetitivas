c = int(input("\n\nDame el valor del capital : "))

mes=0
interesT=c




while (interesT< 2*c):

    interesT=(interesT*0.05)+interesT
    mes=mes+1
    
print("La cantidad de meses necesarios para duplicar el capital de : "+str(c)+"  son : "+str(mes)+" meses")