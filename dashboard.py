import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("EDA/creditcard.csv")

# Titre de l'application
st.title("Tableau de bord interactif : Analyse des transactions bancaires")

# Affichage des données
if st.checkbox("Afficher les données brutes", key="data_checkbox"):
    st.write(data.head())

# Statistiques univariées
st.header("Statistique Univariée")
variable = st.selectbox("Choisissez une variable :", data.columns, key="univariate_variable")
fig, ax = plt.subplots()
sns.histplot(data[variable], kde=True, ax=ax)
st.pyplot(fig)

# Analyse multivariée : Scatter plot
st.header("Analyse Multivariée")
x_var = st.selectbox("Choisissez la variable X :", data.columns, key="multivariate_x")
y_var = st.selectbox("Choisissez la variable Y :", data.columns, key="multivariate_y")
hue_var = st.selectbox("Choisissez la variable de couleur :", ["Class"], key="multivariate_hue")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_var, y=y_var, hue=hue_var, ax=ax, palette={0: 'blue', 1: 'red'})
st.pyplot(fig)

# Statistiques descriptives globales
st.header("Statistiques descriptives globales")
# Nombre total de transactions
st.write(f"Nombre total de transactions : {data.shape[0]}")

# Nombre de transactions par classe
st.write("Répartition des classes :")
st.write(data['Class'].value_counts())

# Statistiques de base
st.write("Statistiques descriptives des variables :")
st.write(data.describe())

# Comparaison des distributions par classe
st.header("Comparaison des distributions par classe")
variable_compare = st.selectbox("Choisissez une variable pour la comparaison :", data.columns, key="compare_variable")
fig, ax = plt.subplots()
sns.histplot(data, x=variable_compare, hue="Class", kde=True, palette={0: 'blue', 1: 'red'}, ax=ax)
st.pyplot(fig)

# Matrice de corrélation
st.header("Matrice de corrélation")
corr_matrix = data.corr()
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Transactions suspectes
st.header("Transactions suspectes")
suspectes = data[(data['V17'] < -10) | (data['V14'] < -10)]
st.write(f"Nombre de transactions suspectes : {suspectes.shape[0]}")
st.write(suspectes)

# Comparaison multivariée
st.header("Analyse multivariée : Comparaison de deux variables")
x_var_compare = st.selectbox("Choisissez la variable X :", data.columns, key="compare_multivariate_x")
y_var_compare = st.selectbox("Choisissez la variable Y :", data.columns, key="compare_multivariate_y")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_var_compare, y=y_var_compare, hue="Class", palette={0: 'blue', 1: 'red'}, ax=ax)
st.pyplot(fig)

# Évolution dans le temps
st.header("Évolution des transactions dans le temps")
time_var = st.selectbox("Choisissez une variable pour analyser son évolution temporelle :", data.columns, key="time_analysis")
fig, ax = plt.subplots()
sns.lineplot(data=data, x="Time", y=time_var, hue="Class", palette={0: 'blue', 1: 'red'}, ax=ax)
st.pyplot(fig)

# Filtrer les transactions
st.header("Filtrer les transactions")
min_amount = st.slider("Montant minimum :", float(data['Amount'].min()), float(data['Amount'].max()), 0.0, key="min_amount")
max_amount = st.slider("Montant maximum :", float(data['Amount'].min()), float(data['Amount'].max()), 1000.0, key="max_amount")
filtered_data = data[(data['Amount'] >= min_amount) & (data['Amount'] <= max_amount)]
st.write(f"Nombre de transactions après filtre : {filtered_data.shape[0]}")
st.write(filtered_data)
