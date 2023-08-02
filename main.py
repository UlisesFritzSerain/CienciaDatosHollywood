# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("HollywoodMovies.csv")
#Borramos las peliculas que no poseian genero. (ibamos a sacar historia pero al sacar genero el dato quedo bastante completo).
dfMoviesFinal = df.dropna(subset=['Genre'])

#TOP 10 peliculas de OpeningWeekend Taquilleras
primerSemana = dfMoviesFinal.sort_values(by="OpeningWeekend", ascending=False)
top10Estreno = primerSemana.head(10)
print("Peliculas con mayor exito en el fin de semana de estreno")
print(top10Estreno[["Movie","OpeningWeekend"]])

#LIMPIEZA DE DATAFRAMES TOP 10 Estudios
cantMoviesPorEstudio = dfMoviesFinal["LeadStudio"].value_counts()
estudios = cantMoviesPorEstudio.iloc[1:11] # CANTIDAD / sacamos la primera por que son proyectos independientes.
nombreEstudio = estudios.index
#peliculas que pertenecen a los estudios que mas peliculas hicieron
peliculasEstudiosTop10 = dfMoviesFinal[dfMoviesFinal["LeadStudio"].isin(nombreEstudio)] #468 peliculas
#print(peliculasEstudiosTop10)
gananciasEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['Profitability'].sum() # ganancia de cada estudio (total profitability)
gananciaPromedio= gananciasEstudios/estudios  #prodemdio de ganancias

#GANANCIA PROMEDIO ESTUDIOS TOP 10
nombreEstudio=gananciaPromedio.index
plt.barh(nombreEstudio,gananciaPromedio)
plt.ylabel('Estudios de Hollywood')
plt.xlabel('Ganancia Bruta mundial en porcentaje del presupuesto')
plt.title('Estudio de la ganancia de los 10 estudios de Hollywood mas importantes entre 2007 y 2012')
plt.show()

#BUDGET PROMEDIO:
BudgetStudios = peliculasEstudiosTop10.groupby('LeadStudio')['Budget'].sum() # estudio con mas presupuesto
BudgetStudiosPromedio= BudgetStudios/estudios
BudgetEstudio=BudgetStudiosPromedio.index
plt.barh(BudgetEstudio,BudgetStudiosPromedio, color='orange')
plt.ylabel('Estudios')
plt.xlabel(' Busget')
plt.title('Cantidad promedio invertida por los estudios')
plt.show()

#COMPARACION DE ESTUDIOS A NIVEL PRESUPUESTO/EXITO
budget_ganancia_estudios_top10 = peliculasEstudiosTop10.groupby('LeadStudio').agg({'Budget': 'mean', 'WorldGross': 'mean'})
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Budget', y='WorldGross', data=budget_ganancia_estudios_top10, marker='o', s=100)
for budget_ganancia_estudios_top10, row in budget_ganancia_estudios_top10.iterrows():
    plt.text(row['Budget'], row['WorldGross'], budget_ganancia_estudios_top10, fontsize=14, ha='left', va='bottom')

plt.xlabel('Presupuesto Promedio por Estudio')
plt.ylabel('Ganancia Mundial Promedio por Estudio')
plt.title('Diferencias de Presupuesto y Éxito por Estudio')
plt.tight_layout()
plt.show()

RottenEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['RottenTomatoes'].sum() # valoracion de rotten tomatos de cada estudio (total)
RottenPromedio= RottenEstudios/estudios  #prodemdio de rotten
AudienciaEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['AudienceScore'].sum() # valoracion de audiencia de cada estudio (total)
AudienciaPromedio= AudienciaEstudios/estudios  #prodemdio de Audience
#print(AudienciaPromedio.sort_values(ascending=False))

#DIFERENCIA ENTRE VALORACION DE ROTTEN Y AUDIENCIA 
plt.barh(nombreEstudio, RottenPromedio, color='red', label='Rotten Tomatos')
plt.barh(nombreEstudio, AudienciaPromedio, color='blue', label='Audiencia', alpha=0.7)
plt.xlabel('Valoracion')
plt.ylabel('Estudios')
plt.title('Valoracion de la audiencia y Rotten Tomatoes')
plt.legend(fontsize = 'small')
plt.show()


TaquilleraEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['OpeningWeekend'].sum() # mas taquillera de cada estudio (total)
#print(TaquilleraEstudios.sort_values(ascending=False))
TaquilleraPromedio= TaquilleraEstudios/estudios  #prodemdio de taquillera
#print(TaquilleraPromedio.sort_values(ascending=False))
DomesticEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['DomesticGross'].sum() # cant generada localmente de cada estudio (total)
DomesticPromedio= DomesticEstudios/estudios  #prodemdio de la cant generada localmente
ExtranjeroEstudios = peliculasEstudiosTop10.groupby('LeadStudio')['ForeignGross'].sum() # cant generada en el extrangero de cada estudio (total)
ExtranjeroPromedio= ExtranjeroEstudios/estudios  #prodemdio de la cant generada en el extranjero

# cuanto se genera adentro y afuera
plt.barh(nombreEstudio, ExtranjeroPromedio, color='green', label='Extranjera')
plt.barh(nombreEstudio, DomesticPromedio, color='red', label='Local', alpha=0.7)
plt.xlabel('Ganancia (Millones)')
plt.ylabel('Estudios')
plt.title('Comparacion de la ganancia generada dentro de los Estados Unidos y en el Extranjero')
plt.legend()
plt.show()

#El que gana mas localmente que en el extranjero
df_estudios = pd.DataFrame({
    'LeadStudio': DomesticEstudios.index,
    'GananciaLocal': DomesticEstudios.values,
    'GananciaExtranjera': ExtranjeroEstudios.values
    })

df_estudios['Diferencia'] = df_estudios['GananciaLocal'] - df_estudios['GananciaExtranjera']
estudio_mayor_diferencia_local = df_estudios['LeadStudio'][df_estudios['Diferencia'].idxmax()]
print("Estudio con mayor ganancia en EEUU que en el extranjero:")
print(estudio_mayor_diferencia_local)
peliculas_estudio_mayor_diferencia = dfMoviesFinal[dfMoviesFinal['LeadStudio'] == estudio_mayor_diferencia_local]

#Buscamos el mayor exito medido al presupuesto. 
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Budget', y='WorldGross', size='WorldGross', hue='WorldGross', data=dfMoviesFinal, alpha=0.7)

plt.xlabel('Presupuesto (Millones)')
plt.ylabel('Ingresos Mundiales (Millones)')
plt.title('Relación entre Presupuesto e Ingresos Mundiales de Películas')
plt.show()

peliMasGanadora = dfMoviesFinal[dfMoviesFinal['WorldGross'] == dfMoviesFinal['WorldGross'].max()]
print(peliMasGanadora[["Movie",'WorldGross']])
peliCalidadPrecio =  dfMoviesFinal[
    (dfMoviesFinal['WorldGross'] >= 1000) & (dfMoviesFinal['WorldGross'] <= 1500) &
    (dfMoviesFinal['Budget'] >= 100) & (dfMoviesFinal['Budget'] <= 150)
]
print(peliCalidadPrecio[["Movie", "WorldGross", "Budget"]]) #Segunda de mas ganancia sin estar en el top 20 de presupuestos.


#GENERO MAS ACLAMADO POR LA AUDIENCIA: 
puntajes_promedio_audiencia = dfMoviesFinal.groupby('Genre')['AudienceScore'].mean()
#print(puntajes_promedio_audiencia.sort_values(ascending=False))

#GENERO MAS ACLAMADO POR LA CRITICA: 
puntajes_promedio_critica = dfMoviesFinal.groupby('Genre')['RottenTomatoes'].mean()
#print(puntajes_promedio_critica.sort_values(ascending=False))

df_puntajes = pd.DataFrame({'Audience Score': puntajes_promedio_audiencia, 'RottenTomatoes': puntajes_promedio_critica})
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_puntajes, marker='o', markersize=8, linewidth=2)
plt.xlabel('Género')
plt.ylabel('Puntaje Promedio')
plt.title('Puntajes Promedio por Género (Audiencia vs. RottenTomatoes)')
plt.xticks(rotation=90)
plt.legend(['Audiencia', 'RottenTomatoes'])
plt.tight_layout()
plt.show()
# %%
