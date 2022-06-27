import streamlit as st
from zipfile import ZipFile, Path
import pandas as pd
# Import des fichier page
import mes_analyses
import a_propos
import classement

st.set_page_config(layout="wide", page_title='UBER EAT')

# Sidebar Intro
las_file=None
st.sidebar.write('# Dites bonjour à vos données UBER EAT 🚲')
st.sidebar.write("Je travaille avec Yann le plus beau !")

# Sidebar Navigation
options = st.sidebar.radio('Parcourir :', 
    ['Mes analyses', 'Classement', 'A propos'])

if options == 'Mes analyses':
    mes_analyses.mes_analyses()
elif options == 'Classement':
    classement.classement()
elif options == 'A propos':
    a_propos.a_propos()

