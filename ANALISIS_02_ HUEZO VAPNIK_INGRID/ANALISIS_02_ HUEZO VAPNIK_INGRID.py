import pandas as pd

#1a opción Rutas de importación y exportación
synergy_dataframe = pd.read_csv('synergy_logistics_database.csv',
                                index_col=0, encoding='utf-8', parse_dates=[4, 5])

#Definir apartados
combinaciones1 = synergy_dataframe.groupby(by=['direction', 'origin',
                                               'destination','transport_mode'])

#Agregamos el apartado Total value, el cual nos servirá para filtrar las 10 
#mejores rutas de importación y exportación
descripcion = combinaciones1.describe()['total_value']
#print (descripcion)

#Ordenamos con base en el número de exportaciones e importaciones realizadas
count = descripcion['count']

#Ordenaremos la serie de mayor a menor
count_sort = count.sort_values(ascending=False)

#Transformamos la serie a un dataframe
count_sort = count_sort.to_frame().reset_index()
#print (count_sort)

#%%
import pandas as pd

#2a opción Medio de transporte utilizado
synergy_dataframe2 = pd.read_csv('synergy_logistics_database.csv',
                                index_col=0, encoding='utf-8', parse_dates=[4, 5])

#Definimos apartados, si eliminamos 'direction' podremos ver un score general
#de los medios de transporte.
combinaciones2 = synergy_dataframe2.groupby(by=['direction',
                                               'transport_mode'])

#Agregamos el apartado Total value para considerar el valor de
#las imp. y exp.
descripcion2=combinaciones2.describe()['total_value']

#Obtenemos el promedio
count2=descripcion2['mean']
count_sort2=count2.sort_values(ascending=False)
count_sort2=count_sort2.to_frame().reset_index()
#print (count_sort2)

#%%
import pandas as pd

#3a opción Valor total de importaciones y exportaciones

synergy_dataframe3 = pd.read_csv('synergy_logistics_database.csv',
                                index_col=0, encoding='utf-8', parse_dates=[4, 5])

#Definimos apartados y realizamos sumatoria por país incluyendo
#imp. y exp.
combinaciones3=(synergy_dataframe3.groupby(by=['origin'])
                .sum().groupby(level=[0]).cumsum())
#print (combinaciones3)

plot=combinaciones3.plot.pie(y='total_value')
#print (plot)