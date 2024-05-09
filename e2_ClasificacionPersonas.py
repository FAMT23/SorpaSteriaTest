import pandas as pd
import random

SEXO=["MASCULINO","FEMENINO"]
EDAD_MAX=84
EDAD_MIN=1
N_PERSONAS=50
MAYOR_EDAD=18

def leerPersonas(n_Personas):
    df=pd.DataFrame(columns=["Sexo","Edad"])
    
    for i in range(n_Personas):
        fila={"Sexo":SEXO[random.randint(0,1)],"Edad":random.randint(EDAD_MIN,EDAD_MAX)}
        df=df._append(fila, ignore_index=True)
    return df

def generarResultados():
    PERSONAS=leerPersonas(N_PERSONAS)
    print(PERSONAS)
    
    mayores_edad=PERSONAS[PERSONAS["Edad"]>=18]
    menores_edad=PERSONAS[PERSONAS["Edad"]<18]
    print("Mayores de edad son :",len(mayores_edad))
    print("Menores de edado son: ",len(menores_edad))
    
    masc_mayor_edad=mayores_edad[mayores_edad["Sexo"]=="MASCULINO"]
    fem_menor_edad=menores_edad[menores_edad["Sexo"]=="FEMENINO"]
    
    print("Masculinos mayores de edad son :",len(masc_mayor_edad))
    print("Femeninas menores de edad son: ",len(fem_menor_edad))
    
    sexo_femenino=PERSONAS[PERSONAS["Sexo"]=="FEMENINO"]
    print("La proporción de mayores de edad en la muestra es del :",len(mayores_edad)/len(PERSONAS)*100,"%")
    print("La proporción del sexo femenino en la muestra es del :",len(sexo_femenino)/len(PERSONAS)*100,"%")
    
generarResultados()
    