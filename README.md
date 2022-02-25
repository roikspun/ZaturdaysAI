# Saturdays.AI Zaragoza

# README.md
Card.io – Estimador de enfermedad cardiovascular

## OBJETIVO:
Conocer la existencia o no de enfermedad cardiovascular, de una manera rápida, deslocalizada y sin coste. 

## DESCRIPCIÓN:
Se parte de un conjunto de datos con características de personas y su diagnóstico de la existencia de enfermedad cardiovascular. Mediante algoritmos de inteligencia artificial se entrena y se crea un modelo que predice la enfermedad cardiovascular. El modelo resultante se combina con Streamlit para introducir datos individuales y devuelve la existencia o no de enfermedad cardiovascular.

## DATASET:
Obtenido de la página kaggle. El conjunto de datos consta de 70.000 registros de datos de pacientes con 11 características más un objetivo.
Los valores del conjunto de datos se recopilaron en el momento del examen médico, en 2019.
https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

## MODELOS:
Se han aplicado modelos de árbol de decisión y random forest, tanto con las variables estándar como variables modificadas para ajustarse más.

## REQUERIMIENTOS:
Se ha utilizado código Python y librerías para análisis, presentación de datos y métricas en entorno COLAB:
Pandas
Numpy
Seaborn
Matplotlib 
Sklearn
Se ha utilizado Streamlit para crear un interfaz de comunicación con el usuario en entorno ANACONDA?

# PARTICIPANTES:
* Erick René Espíndola
* César Guayara
* José Antonio Aísa




## CONCLUSIÓN:
Se generó un algoritmo de inteligencia artificial capaz de predecir la existencia de enfermedad cardiovascular. Las métricas obtenidas arrojan un valor de accuracy de 0,72.
Como mayores factores de riesgo se observan la edad, para mayores de 50 años, y una presión arterial alta. También el colesterol y el sobre peso, influyen, caso de ser valores muy altos.
Los algoritmos de IA son válidos y fiables para este tipo de diagnóstico médico basado en datos.

## PRÓXIMOS PASOS:
Respecto a los datos, conseguir un dataset local, que mejoraría la precisión al enfocarse en una población determinada con hábitos de vida más comunes.
Respecto al código, probar otros algoritmos de machine learning y comparar sus métricas para obtener mejores valores de predicción.
Respecto al interfaz Streamlit, difundirlo entre la población para que se conozca y se tome conciencia del riesgo de padecer enfermedad cardiovascular.
