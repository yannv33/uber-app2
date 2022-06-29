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
st.sidebar.write('# Dis bonjour à tes données UBER EATS 🚲')
st.sidebar.write("Pour plus d'informations sur notre projet, n'hésite pas à te diriger sur l'onglet \"A propos\"")

# Sidebar Navigation
options = st.sidebar.radio('Parcourir :', 
    ['Mes données', 'Classement', 'A propos'])

if options == 'Mes données':
    mes_analyses.mes_analyses()
elif options == 'Classement':
    classement.classement()
elif options == 'A propos':
    a_propos.a_propos()

