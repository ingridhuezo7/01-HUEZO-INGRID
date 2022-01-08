import pandas as pd
#%%
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

#3a opción Valor total de importaciones y exportaciones

synergy_dataframe3 = pd.read_csv('synergy_logistics_database.csv',
                                index_col=0, encoding='utf-8', parse_dates=[4, 5])

#Definimos variables de imp. y exp.
exports=synergy_dataframe3[synergy_dataframe3['direction']=='Exports']
imports=synergy_dataframe3[synergy_dataframe3['direction']=='Imports']

#Función para obtener el porcentaje acumulado y países pertenecientes
#al 85%
def sol_3 (df,p):
    total_value_origin=df.groupby('origin').sum()['total_value'].reset_index()
    total_value_percent=total_value_origin['total_value'].sum()    
    total_value_origin['percent']=100*total_value_origin['total_value']/total_value_percent
    total_value_origin.sort_values(by='percent',ascending=False,inplace=True)
    total_value_origin['cumsum']=total_value_origin['percent'].cumsum()
    lista=total_value_origin[total_value_origin['cumsum']<p]
    return lista

res_exports=sol_3(exports, 85)
res_imports=sol_3(imports, 85) 

#Se grafican en un pie chart acorde a su número de índice
plot=res_exports.plot.pie(y='total_value')
#print (plot)
plot2=res_imports.plot.pie(y='total_value')
#print (plot2)

#Definimos apartados y realizamos sumatoria por país incluyendo
#imp. y exp.
combinaciones3=(synergy_dataframe3.groupby(by=['origin'])
                .sum().groupby(level=[0]).cumsum())
#print (combinaciones3)

plot3=combinaciones3.plot.pie(y='total_value')
#print (plot3)