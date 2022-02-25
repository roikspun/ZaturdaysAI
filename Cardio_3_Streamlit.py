import os
import pandas as pd
import numpy as np
import sklearn
import streamlit as st
# import Cardio_analisis
# Limpieza y tratamiento de datos, incluyendo el modelo

# os.system('cardio_analisis.py')

# from Cardio_analisis

st.write("""
# Card.IO 
## Predicción de Enfermedades Cardiovasculares con Inteligencia Artificial
""")

# Introduction Text
st.write('''
### ¿Qué es Card.IO?
Card.IO es un modelo de inteligencia artificial que toma datos como presión arterial, colesterol, hábitos de
consumo de tabaco y alcohol, entre otros, de forma anonima y de miles de pacientes de edades a partir de los 16 años. 
Estos datos son filtrados y procesados para alimentar el modelo, que arroja una prediccción de que tan probable 
es que el usario padezca una enfermedad cardiovascular o sea propenso a ella. 
''')

# Text that introduces the variable selection for boxplot plotting
st.write('''
## ¿Te has preguntado que afecta más a tu salud cardiovascular?
Selecciona el habito o variable que más te interese cononcer, la gráfica te dará un indicador de si puede o no ser 
relevante en el desarrollo o padecimiento de una enfermedad cardiovascular. 
''')
var_select = st.selectbox('Selecciona la variable', ("Altura","Peso","Género","Edad", "Colesterol",
                                                        "Presión Diastólica","Presión Sistólica",
                                                        "Tabaquismo","Alcoholismo"),)
st.write(var_select)

# Introduction to what kind of algorithm the user wants to implement on the data
#st.write('''
## Veamos que nos pueden contar los datos...
#Para obtener más información de los datos, podemos usar representaciones gráficas que nos cuentan acerca de la relaciones
#entre las variables y su causalidad para el desarrollo dichas enfermedades.
### Selecciona la variable a estudiar
# ''')
#algo_select = st.selectbox('Selecciona la variable a observar', ("Random Forest",))








st.write('''
### Ingresa tus datos y así el modelo podrá generar una predicción con tu perfil.
Esta predicción es solo una recomendación, no un diagnóstico, solo un médico especialista
puede diagnosticar con certeza el padecimiento de una enfermedad.
''')

def get_user_info():
    user_data = {}
    edad_user = st.text_input("Tu edad en años", '16')
    user_data['Edad']= edad_user
    altura_user = st.text_input("Tu altura en cm", '167')
    user_data["Altura"] = altura_user
    genero_user = st.text_input("Sexo", 'M/F') #  La variable se convierte a 0 si es hombre 1 si es mujer
    user_data["Genero"] = genero_user
    peso_user = st.text_input("Peso en Kg", '65')
    user_data["Peso"] = peso_user
    tabaco_u = st.text_input("Consumo de tabaco", 'S/N')
    user_data["Consumo de tabaco"] = tabaco_u
    alcohol_u = st.text_input("Consumo de alcohol", 'S/N')
    user_data["Consumo de alcohol"] = alcohol_u

    ap_hi_user = st.text_input("Ingresa la ultima medición de tu presión diastólica", '120')
    user_data["Presión diastólica"] = ap_hi_user
    ap_lo_user = st.text_input("Ingresa la ultima medición de tu presión sistólica", '80')
    user_data["Presión sistólica"]= ap_lo_user
    colesterol_user = st.text_input("Ingresa la ultima medición de tu colesterol")
    user_data["Colesterol"] = colesterol_user
    actividad_user = int(st.text_input("Nivel de Actividad física: Nula - 0, Baja - 1, Media - 2, Alta - 3", '2'))
    user_data["Actividad física"] = actividad_user
    return user_data

user_data = get_user_info()
st.write('''### Estos son tus datos, que serán ingresados al modelo''', user_data)

# Here we turn the dictionary to a DF using pandas
df_user_info = pd.DataFrame.from_dict(user_data, orient="index")


st.write('''
### Predicción basada en IA...
El uso de inteligencia artificial nos permite generar predicciones, basadas en estadísticas, acerca de algún fenomeno
observable y medible. Card.IO se basará en más de 70,000 voluntarios con o sin enfermedades cardiovasculares, para 
mostrar un indicador sobre si es pertinente que el usuario visite al médico especialista.

Recuerda, Card.IO, es solo una herramienta que puede guiarte para cuidar de tu salud cardiovascular, no es una
herramiento de diagnóstico. Si el resultado es positivo, es recomendable que acudas a tu médico para una revisión. 
''')

# predecir
# final_model.predict(df_user_info)





