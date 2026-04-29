"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias 
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: 
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
This software is for educational purposes.  
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""

import pandas as pd
import numpy as np
import streamlit as st


st.title("Hola Streamlit")

if st.button("Generar datos"):
    st.write("Datos aleatorios:")
    size = st.slider("Tamaño de los datos", 5, 50, 10)
    df = pd.DataFrame(np.random.randn(size, 2), columns = ["x", "y"])
    st.line_chart(df)
