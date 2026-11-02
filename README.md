# Predicción de Riesgo de Diabetes

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://monicafernandezm-riesgo-diabetes-app-qcxi5r.streamlit.app/)

## Descripción 
Este proyecto desarrolla un modelo de Machine Learning capaz de estimar el riesgo de diabetes a partir de variables médicas y de estilo de vida.

El objetivo es crear una herramienta de apoyo que permita identificar personas con mayor probabilidad de riesgo de forma temprana, facilitando acciones preventivas.

> *Este modelo no sustituye un diagnóstico médico, sino que actúa como sistema de evaluación preliminar.*

## Tabla de Contenidos
- [Descripción](#descripción)
- [Objetivo](#objetivo)
- [Demo en Vivo](#demo-en-vivo)
- [Instalación](#instalación)
- [Uso](#uso)
- [Dataset](#dataset)
- [Preprocesamiento de Datos](#preprocesamiento-de-datos)
- [Modelado](#modelado)
- [Optimización del Modelo](#optimización-del-modelo)
- [Métricas de Evaluación](#métricas-de-evaluación)
- [Ajuste de Punto de Decisión](#ajuste-de-punto-de-decisión)
- [Resultados](#resultados)
- [Implementación](#implementación)
- [Aplicación en el Mundo Real](#aplicación-en-el-mundo-real)
- [Limitaciones](#limitaciones)
- [Trabajo Futuro](#trabajo-futuro)
- [Contribución](#contribución)
- [Autora](#autora)

## Objetivo
Construir un modelo de clasificación que:
- Prediga el riesgo de diabetes.
- Maximice la detección de casos reales (priorizando *Recall*).
- Mantenga un equilibrio adecuado con la precisión.
- Ofrezca resultados interpretables.

## Demo en Vivo
Puedes interactuar directamente con la herramienta sin necesidad de instalar nada en tu equipo:
**[Acceder a la aplicación en Streamlit Cloud](https://monicafernandezm-riesgo-diabetes-app-qcxi5r.streamlit.app/)**

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/MonicaFernandezM/Riesgo-Diabetes.git
   ```
2. Crear y activar un entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Instalar las dependencias del proyecto:
```bash
pip install -r requirements.txt
```
4. Reproducir el análisis y entrenamiento:
   Abrir y ejecutar el notebook *01_data_cleaning_diabetes.ipynb* en Jupyter Notebook o VS Code.

## Uso 
* Abrir el notebook del proyecto.
* Ejecutar las celdas en orden.
* Explorar los resultados.

El análisis está organizado por secciones para facilitar la comprensión del flujo de trabajo.

## Dataset

El análisis utiliza el dataset [CDC Diabetes Health Indicators](https://www.kaggle.com/datasets/abdelazizsami/cdc-diabetes-health-indicators), el cual contiene 253.680 registros con información demográfica y médica.

### Variables principales:
| Variable | Categoría | Descripción |
|----------|-----------|-------------|
| `HighBP` | Salud | Presión arterial alta (`0`: No, `1`: Sí) |
| `HighChol` | Salud | Colesterol alto (`0`: No, `1`: Sí) |
| `BMI` | Salud | Índice de Masa Corporal (Body Mass Index) |
| `Smoker` | Estilo de vida | Tabaquismo (haber fumado al menos 100 cigarrillos) |
| `PhysActivity` | Estilo de vida | Actividad física en los últimos 30 días |
| `GenHlth` | Salud | Autopercepción del estado de salud general (escala 1 a 5) |
| `Age` | Demográfica | Rango de edad del paciente (categorizado de 1 a 13) |
| `Education` | Demográfica | Nivel educativo alcanzado (escala 1 a 6) |
| `Income` | Socioeconómica | Nivel de ingresos del hogar (escala 1 a 8) |
| `HeartDiseaseorAttack` | Historial médico | Historial de enfermedad coronaria o infarto |

### Variable objetivo:
- **Origen:** Creada a partir de la variable original `Diabetes_012`.
- **Clase 0:** Bajo riesgo.
- **Clase 1:** Alto riesgo (~17% del total, dataset desbalanceado).

Aproximadamente el 17% de los casos corresponden a alto riesgo, lo que implica un dataset desbalanceado.

## Preprocesamiento de Datos

- Eliminación de valores extremos en BMI (recorte entre el percentil 1 y 99).
- División train-test (80% entrenamiento / 20% prueba).
- División estratificada para conservar la proporción de clases.
- Selección adecuada de variables predictoras.
- Preparación del target para clasificación binaria.

## Modelado

Se evaluaron diferentes modelos de clasificación y se seleccionó: **Gradient Boosting Classifier**

Motivos de la elección:
- Alta capacidad para distinguir perfiles de riesgo complejos.
- Buen rendimiento general en datasets desbalanceados.
- Resultados estables tras el proceso de validación.

## Optimización del Modelo 

Para mejorar el rendimiento se aplicaron:
* Validación cruzada (5-fold)
* Randomized Search para el ajuste fino de hiperparámetros
* Métrica principal de optimización: ROC-AUC

 
## Métricas de Evaluación

El modelo fue evaluado utilizando métricas clave adaptadas al contexto médico:
- Recall (Sensibilidad): ¿Cuántos casos reales de diabetes es capaz de detectar? (Métrica priorizada).
- Precision: Cuando el modelo predice riesgo, ¿cuántas veces acierta?
- F1-score: Equilibrio ponderado entre precision y recall.
- ROC-AUC: Capacidad global del modelo para distinguir entre clases.

Dado el contexto médico, se priorizó el Recall para maximizar la detección temprana.

## Ajuste de Punto de Decisión

El modelo genera probabilidades continuas de riesgo. En lugar de utilizar el umbral estándar de 0.5, se optimizó el punto de decisión para maximizar el F1-score, logrando un equilibrio óptimo adaptado a la escasez de falsos negativos críticos.

## Resultados 

* ROC-AUC: ~0.81
* Capacidad de detección: Detecta aproximadamente el 66% de los casos reales de riesgo.
* Control de errores: Mantiene un nivel controlado de falsas alarmas.

El modelo demuestra una sólida capacidad para generalizar y distinguir perfiles de riesgo en datos no vistos.

## Implementación

El modelo fue desplegado mediante una aplicación interactiva en Streamlit, permitiendo:
- Introducir datos médicos y de estilo de vida de forma sencilla.
- Calcular automáticamente el BMI (opcional).
- Obtener la probabilidad estimada de riesgo de forma instantánea.
- Visualizar una interpretación clara del resultado.

## Aplicación en el Mundo Real

El sistema diseñado puede desempeñar un rol útil como:
- Herramienta de apoyo en centros de salud de atención primaria.
- Sistema de cribado preventivo rápido.
- Aplicación digital orientada al autocuidado y autoevaluación.
- Sistema de priorización y alerta temprana de pacientes.

## Limitaciones

- Basado en datos históricos y de carácter auto-reportado.
- No incluye analíticas clínicas avanzadas u hospitalarias directas.
- Posibilidad latente de generar falsos positivos o falsos negativos.
- No sustituye en ningún caso un diagnóstico médico profesional.

## Trabajo Futuro 

- Incorporar variables clínicas y analíticas de mayor profundidad.
- Realizar una validación externa con nuevas poblaciones o fuentes de datos.
- Comparar el rendimiento frente a otros modelos avanzados de Ensemble.
- Implementar una monitorización continua del rendimiento del modelo en producción.

## Contribución 

Las contribuciones son bienvenidas. Si deseas mejorar el análisis o añadir visualizaciones:
1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/mejora).
3. Realiza tus cambios y haz commit (git commit -m 'Añadir mejora').
4. Abre un Pull Request. 

### Autora
Mónica María Fernández Mirás
