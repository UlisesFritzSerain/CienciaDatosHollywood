import pandas as pd
import matplotlib as plt

# QUE GENERO/ESTUDIO ES EL MAS TAQUILLERO/MAS INVIERTE/
# ESTUDIO CON MAS PRESUPUESTO/exito/
# MEJORES CRITICAS ENTRE ROTTEN TOMATOES Y AUDIENCIA (GRAFICO)
# DIFERENCIA ENTRE MEJOR PELICULA Y PEOR ( nos podemos basar en puntuacion o recaudacion)
# EJEMPLO DE MUCHO EXITO CON POCO PRESUPUESTO Y VICEVERSA. 
# COMPARACION DE SI GANAN MAS NACIONALMENTE O CON LAS VENTAS AL EXTRANJERO.
# SEGUIMIENTO DE GANANCIA POR AÑO (podemos nombrar el mas exitoso y el menos).

df = pd.read_csv("HollywoodMovies.csv")

#Borramos la columna de historia, ya que faltan muchos datos y no es posible completarla. 
#dfMovies = df.drop("Story", axis=1)
#Borramos las peliculas que no poseian genero. (ibamos a sacar historia pero al sacar genero el dato quedo bastante completo).
dfMoviesFinal = df.dropna(subset=['Genre'])
#print(dfMoviesFinal.info())


#TOP 10 peliculas de OpeningWeekend Taquilleras
primerSemana = dfMoviesFinal.sort_values(by="OpeningWeekend", ascending=False)
top10Estreno = primerSemana.head(10)
#print(top10Estreno[["Movie","OpeningWeekend"]])

#ANALISIS DE ESTUDIOS DE HOLLYWOOD
cantMoviesPorEstudio = dfMoviesFinal["LeadStudio"].value_counts()
estudios = cantMoviesPorEstudio.iloc[1:11] # CANTIDAD / sacamos la primera por que son proyectos independientes.
nombreEstudio = estudios.index
#print(nombreEstudio)
#peliculas que pertenecen a los estudios que mas peliculas hicieron
peliculasEstudiosTop10 = dfMoviesFinal[dfMoviesFinal["LeadStudio"].isin(nombreEstudio)] #468 peliculas
print(peliculasEstudiosTop10)
gananciasEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['Profitability'].sum() # ganancia de cada estudio (total profitability)
print(gananciasEstudios.sort_values(ascending=False))
