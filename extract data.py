import pandas as pd
import random




def concat_ids(row):
    return str(row['product_name']) + '_' + str(row['department_id'])

# Leer el primer archivo CSV
order_products_1 = pd.read_csv(r'C:\Users\danyg\OneDrive\Documents\Javeriana Maestria\Primer Semestre\Metodo Analítica 1\Taller 2\order_products__train.csv')
order_products_2 = pd.read_csv(r'C:\Users\danyg\OneDrive\Documents\Javeriana Maestria\Primer Semestre\Metodo Analítica 1\Taller 2\order_products__prior.csv')

hours = pd.read_csv(r'C:\Users\danyg\OneDrive\Documents\Javeriana Maestria\Primer Semestre\Metodo Analítica 1\Taller 2\orders.csv')

# Leer el segundo archivo CSV
products = pd.read_csv(r'C:\Users\danyg\OneDrive\Documents\Javeriana Maestria\Primer Semestre\Metodo Analítica 1\Taller 2\products.csv')

order_products=pd.concat([order_products_1, order_products_2], ignore_index=True)


merged_data = pd.merge(order_products, products, on='product_id', how='left')

merged_data2 = pd.merge(merged_data, hours, on='order_id', how='left')

apriori = merged_data2[['order_id', 'department_id', 'product_name','order_dow']]


test= apriori[(apriori['department_id'] == 4)]


#test['product_name'] = test.apply(concat_ids, axis=1)

natural_apriori=test[['order_id','product_name']]

# Calcula el tamaño de la muestra basado en un porcentaje específico
porcentaje_muestra = 0.8  # porcentaje del 20%
tamaño_muestra = int(len(natural_apriori['order_id']) * porcentaje_muestra)

# Muestra aleatoriamente la lista sin reemplazo
muestra = random.sample(list(natural_apriori['order_id']), tamaño_muestra)


natural_apriori2 = natural_apriori[natural_apriori['order_id'].isin(muestra)]

natural_apriori.to_csv(r'C:\Users\danyg\OneDrive\Documents\Javeriana Maestria\Primer Semestre\Metodo Analítica 1\Taller 2\apriori.csv', index=False)
natural_apriori2.to_csv(r'C:\Users\danyg\OneDrive\Documents\Javeriana Maestria\Primer Semestre\Metodo Analítica 1\Taller 2\apriori_sample.csv', index=False)


############
#Ver los 100 productos mas comprados de produce y dairy eggs

produce_df=apriori[(apriori['department_id'] == 4)]
canned_df=apriori[(apriori['department_id'] == 15)]

produce_counts = produce_df['product_name'].value_counts().reset_index()
produce_counts.columns = ['product_name', 'total_compras_produce']
produce_150 = produce_counts.head(10)
produce_150_list = list(produce_150['product_name'])


canned_counts = canned_df['product_name'].value_counts().reset_index()
canned_counts.columns = ['product_name', 'total_compras_dairy_eggs']
canned_50 = canned_counts.head(50)
canned_50_list = list(canned_50['product_name'])
####################

#Graficar los 5 departamentos más importantes 

# import matplotlib.pyplot as plt

# # Supongamos que ya tienes un DataFrame df_sin_duplicados sin filas duplicadas y una Serie frecuencia_departamentos que contiene la frecuencia de cada departamento

# apriori_noDup = apriori.drop_duplicates(subset=['order_id', 'department_id'])

# # Diccionario que mapea identificadores de departamento a nombres de departamento
# nombres_departamentos = {
#     4: 'Productos frescos',
#     16: 'Lácteos y huevos',
#     7: 'Bebidas',
#     19: 'Snacks',
#     1: 'Congelados'
#     # Agrega más nombres de departamentos según sea necesario
# }


# frecuencia_departamentos = apriori_noDup['department_id'].value_counts()

# top4_departamentos = frecuencia_departamentos.nlargest(5)

# # Crear el gráfico de barras solo para los cuatro departamentos más frecuentes
# plt.figure(figsize=(10, 6))
# top4_departamentos.plot(kind='bar', color='skyblue')

# # Cambiar los nombres en el eje x
# plt.xticks(range(len(top4_departamentos)), [nombres_departamentos.get(dep_id, 'Desconocido') for dep_id in top4_departamentos.index], rotation=45)

# plt.title('Frecuencia de los 5 departamentos más frecuentes')
# plt.xlabel('Departamento')
# plt.ylabel('Frecuencia')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()

# # Mostrar el gráfico
# plt.show()



########################################

#Observar porcentaje de mayores compras con comida saludable
import pandas as pd

# Suponiendo que tienes un DataFrame llamado df que contiene las columnas order_id y department_id

# Filtrar las órdenes que contienen el department_id 5
df_filtered = apriori[apriori['department_id'] == 4]

# Obtener los order_id únicos que contienen el department_id 5
order_ids_with_dept_5 = df_filtered['order_id'].unique()

# Filtrar el DataFrame original para incluir solo las órdenes que tienen el department_id 5
df_with_dept_5 = apriori[apriori['order_id'].isin(order_ids_with_dept_5)]

department_counts_4 = df_with_dept_5['department_id'].value_counts()

department_total_counts = apriori['department_id'].value_counts()


# nombres_departamentos = {
#     4: 'Productos frescos',
#     16: 'Lácteos y huevos',
#     7: 'Bebidas',
#     19: 'Snacks',
#     1: 'Congelados',
#     2:'Other',
#     3:'Pastelería',
#     5:'Alcohol',
#     6:'Internacional',
#     8:'Mascotas',
#     9:'Productos de pasta',
#     10:'Productos en cantidad',
#     11:'Cuidado personal',
#     12:'Carnes y Comida de mar',
#     13:'Despensa',
#     14:'Desayuno',
#     15:'Comida enlatada',
#     17:'Hogar',
#     18:'bebes',
#     20:'delicatessen',
#     21:'NA'
#     # Agrega más nombres de departamentos según sea necesario
# }
