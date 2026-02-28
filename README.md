# Predicción de Riesgo de Diabetes

## Description 
Este proyecto desarrolla un modelo de Machine Learning capaz de estimar el riesgo de diabetes a partir de variables médicas y de estilo de vida.

El objetivo es crear una herramienta de apoyo que permita identificar personas con mayor probabilidad de riesgo de forma temprana, facilitando acciones preventivas.

Este modelo no sustituye un diagnóstico médico!, sino que actúa como sistema de evaluación preliminar.

## Tabla de Contenidos
- [Objectivo](#objetivo)
- [Instalación](#instalación)
- [Uso](#uso)
- [Dataset](#dataset)
- [Preprocesamiento](#preprocesamiento)
- [Modelado](#modelado)
- [Optimización](#optimizacion)
- [Metricas-de-Evaluación](#metricas-de-evaluacion)
- [Ajuste-de-punto-de-decisión](#ajuste-de-punto-de-decisión)
- [Resultados](#resultados)
- [Implementación](#implementación)
- [Aplicación-en-el-Mundo-Real](#aplicaion-en-el-mundo-real)
- [Limitaciones](#limitaciones)
- [Trabajo-Futuro](#trabajo-futuro)
- [Contribución](#contribución)

## Objetivo
Construir un modelo de clasificación que:
* Prediga el riesgo de diabetes
* Maximice la detección de casos reales (priorizando Recall)
* Mantenga un equilibrio con la precisión
* Ofrezca resultados interpretables

## Instalación
1. Clonar el repositorio: https://github.com/MonicaFernandezM/Riesgo-Diabetes
   git clone 

2. Abrir el proyecto en Jupyter Notebook.

3. Ejecutar el notebook principal para reproducir el análisis.

No es necesario instalar dependencias adicionales si ya se cuenta con un etorno estándar de ánalisis de datos en Python. 

## Uso 
* Abrir el notebook del proyecto.
* Ejecutar las celdas en orden.
* Explorar los resultados.

El análisis está organizado por secciones para facilitar la comprensión del flujo de trabajo.

## Dataset

Pulsa en [CDC Diabetes Health Indicators](https://www.kaggle.com/datasets/abdelazizsami/cdc-diabetes-health-indicators)para descargarlo en tu equipo.

El dataset contiene 253.680 registros con información demográfica y médica.

Variables principales:
* Presión arterial alta
* Colesterol alto
* Índice de Masa Corporal (BMI)
* Tabaquismo
* Actividad física
* Salud general
* Edad
* Nivel educativo
* Nivel de ingresos
* Historial cardiovascular

Variable objetivo:
* Risk_Group -> Creada apartir de Diabetes_012
* 0 → Bajo riesgo
* 1 → Alto riesgo

Aproximadamente el 17% de los casos corresponden a alto riesgo, lo que implica un dataset desbalanceado.

## Preprocesamiento de Datos

* Eliminación de valores extremos en BMI (recorte entre percentil 1 y 99)
* División train-test (80% entrenamiento / 20% prueba)
* División estratificada para conservar la proporción de clases
* Selección adecuada de variables
* Preparación del target para clasificación binaria

## Modelado

Se evaluaron diferentes modelos y se seleccionó:

**Gradient Boosting Classifier**

Motivos:
* Alta capacidad para distinguir perfiles de riesgo
* Buen rendimiento en datasets desbalanceados
* Resultados estables tras validación

## Optimización del Modelo 

Para mejorar el rendimiento se aplicaron:
* Validación cruzada (5-fold)
* Randomized Search para ajuste de hiperparámetros
* Métrica principal: ROC-AUC

Este proceso permitió seleccionar la mejor configuración del modelo.
 
# Métricas de Evaluación 
El modelo fue evaluado utilizando:
* Recall → ¿Cuántos casos reales detecta?
* Precision → Cuando predice riesgo, ¿cuántas veces acierta?
* F1-score → Equilibrio entre precision y recall
* ROC-AUC → Capacidad global para distinguir entre clases

Dado el contexto médico, se priorizó el Recall para maximizar la detección temprana.

## Ajuste del Punto de Decisión

El modelo genera probabilidad de riesgo.

En lugar de utilizar el umbral estándar de 0.5, se optimizó el punto de decisión para maximizar el F1-score, logrando un mejor equilibrio entre sensiblidad y precisión.

## Resultados 

* ROC-AUC: ~0.81
* Detecta aproximadamente el 66% de los casos reales
* Mantiene un nivel controlado de falsas alarmas

El modelo demuestra una buena capacidad para distinguir perfiles de riesgo en datos no vistos.

## Implementación

El modelo fue desplegado mediante Streamlit, permitiendo:
* Introducir datos médicos y de estilo de vida
* Calcular automáticamente el BMI (opcional)
* Obtener la probabilidad estimada de riesgo
* Visualizar una interpretación clara del resultado

## Aplicación en el Mundo Real

El sistema podría utilizarse como:
* Herramienta de apoyo en centros de salud
* Sistema de cribado preventivo
* Aplicación digital de autoevaluación
* Sistema de priorización de pacientes

## Limitaciones

* Basado en datos históricos y auto-reportados
* No incluye análisis clínicos avanzados
* Puede generar falsos positivos o negativos
* No sustituye diagnóstico profesional

## Trabajo Futuro 

* Incorporar más variables clínicas
* Validación externa en nuevas poblaciones
* Comparación con otros modelos de ensemble
* Monitorización continua del rendimiento

## Contribución 

Las contribuciones son bienvenidas.

Si deseas mejorar el análisis o añadir visualizaciones:
1. Haz un fork del repositorio
2. Crea una nueva rama 
3. Realiza tus cambios
4. Abre un Pull Request 

### Autora
Mónica María Fernández Mirás
