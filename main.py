# %%
import pandas as pd
import matplotlib.pyplot as plt

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
#print(estudios)
#peliculas que pertenecen a los estudios que mas peliculas hicieron
peliculasEstudiosTop10 = dfMoviesFinal[dfMoviesFinal["LeadStudio"].isin(nombreEstudio)] #468 peliculas
#print(peliculasEstudiosTop10)
gananciasEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['Profitability'].sum() # ganancia de cada estudio (total profitability)
#print(gananciasEstudios.sort_values(ascending=False))
gananciaPromedio= gananciasEstudios/estudios  #prodemdio de ganancias
#print(gananciaPromedio.sort_values(ascending=False))
RottenEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['RottenTomatoes'].sum() # valoracion de rotten tomatos de cada estudio (total)
#print(RottenEstudios.sort_values(ascending=False))
RottenPromedio= RottenEstudios/estudios  #prodemdio de rotten
#print(RottenPromedio.sort_values(ascending=False))
AudienciaEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['AudienceScore'].sum() # valoracion de audiencia de cada estudio (total)
#print(AudienciaEstudios.sort_values(ascending=False))
AudienciaPromedio= AudienciaEstudios/estudios  #prodemdio de Audience
#print(AudienciaPromedio.sort_values(ascending=False))
TaquilleraEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['OpeningWeekend'].sum() # mas taquillera de cada estudio (total)
#print(TaquilleraEstudios.sort_values(ascending=False))
TaquilleraPromedio= TaquilleraEstudios/estudios  #prodemdio de taquillera
#print(TaquilleraPromedio.sort_values(ascending=False))
DomesticEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['DomesticGross'].sum() # cant generada localmente de cada estudio (total)
#print(DomesticEstudios.sort_values(ascending=False))
DomesticPromedio= DomesticEstudios/estudios  #prodemdio de la cant generada localmente
#print(DomesticPromedio.sort_values(ascending=False))
ExtrangeroEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['ForeignGross'].sum() # cant generada en el extrangero de cada estudio (total)
#print(ExtrangeroEstudios.sort_values(ascending=False))
ExtrangeroPromedio= ExtrangeroEstudios/estudios  #prodemdio de la cant generada en el extrangero
#print(ExtrangeroPromedio.sort_values(ascending=False))

# ganancia promedio
nombreEstudio=gananciaPromedio.index
plt.barh(nombreEstudio,gananciaPromedio)
plt.ylabel('Estudios')
plt.xlabel(' Ganancia (millones)')
plt.title('Estudio de la ganancia de los 10 estudios mas importantes')
plt.show()

#diferencia entre valoracion audiencia y rotten
plt.barh(nombreEstudio, RottenPromedio, color='red', label='Rotten Tomatos')
plt.barh(nombreEstudio, AudienciaPromedio, color='blue', label='Audiencia', alpha=0.7)
plt.xlabel('Valoracion')
plt.ylabel('estudios')
plt.title('valoracion de la audiencia y en Rotten Tomatos')
plt.legend()
plt.show()

# cuanto se genera adentro y afuera
plt.barh(nombreEstudio, ExtrangeroPromedio, color='green', label='Extragera')
plt.barh(nombreEstudio, DomesticPromedio, color='red', label='Local', alpha=0.7)
plt.xlabel('Ganancia (Millones)')
plt.ylabel('estudios')
plt.title('Ganancia generada en el extrangero y localmente')
plt.legend()
plt.show()


# %%
