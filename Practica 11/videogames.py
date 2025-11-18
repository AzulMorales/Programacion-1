import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#fuente 1: Ventas internas
sales_data={
    "GameID":["G1","G2","G3","G4","G5","G6"],
    "Title": ["Super Mario 64","Sonic Adventure 2","Mystic Messenger","Super Mario Odyssey",
              "South Park, Retaguardia en peligro","Deltarune"],
    "Genre": ["Platform","adventure","otome","adventure","action","rpg"],
    "Publisher":["Nintendo","Sega","Cheritz","Nintendo","Ubisoft","Toby Fox"],
     "Units_Sold_Millions":[15.6,17.5,9.0,18.8,16.8,21.1],
}

sales_df= pd.DataFrame(sales_data)

#fuentes 2: Reseñas de criticos
reviews_data={
    "GameID":["G1","G2","G3","G4","G5","G6","G7",], 
    "Critic_Score":[7.5,9.5,8.8,9.7,6.1,8.0],
    "User_Score":[5.1,9.1,8.5,9.2,np.nan,7.5]
}
reviews_df=pd.DataFrame(reviews_data)

print("----Datos de Venta----")
print(sales_df)
print("----Datos de Reseñas----")
print(reviews_df)

#limpieza de datos y preparacion
#decision: rellenaremos el User_Score que falta con el promedio (South Park, Retaguardia en peligro)
mean_user_score= reviews_df["User_Score"].mean()
reviews_df["User_Score"]= reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n---- Reseñas (limías,Nan rellenando con {mean_user_score}) ----")
print(reviews_df)

#Fusion de tablas (merge)
#fusionar tabla de ventas con reseñas, GAMEID como llave
#INNER JOIN. Nos quedamos con los juegos queexisten en ambas tablas
#G6 va a desaparacer, G7 desaparecer
df= pd.merge(sales_df, on="GAMEID", how="inner") 

print("\n---- Tabla fusionada de ventas+reseñas ----")
print(df)

#crear nuevas columnas que nos den mas informacion
#columna estimacion de ingresos (asimiendo que valen $50 cada juego)
df["Revenue_Estimate_Billions"]= (df["Units_Sold_Millions"]*50)/1000

#columna brecha que hay entre reseñas criticos y la de usuarios
df["Score_Gap"]=df["Critic_Score"]- df["User_Score"]

#columna del estandar de la puntuacion de los criticos  (a 100)
df["Critic_Score_100"]= df["Critic_Score"]*10 
print("\n---- Tabla transformada (Con nuevas Columnas) ----")
print(df)