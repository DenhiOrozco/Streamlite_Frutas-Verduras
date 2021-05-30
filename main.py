import tensorflow.keras
from PIL import Image, ImageOps 
import numpy as np

import streamlit as st

#Quitar la notación científica para claridad
np.set_printoptions(suppress=True)

#Cargar el modelo hecho en Teachable Machine con data de Kaggle
model= tensorflow.keras.models.load_model('/content/drive/MyDrive/EpicQueen_DataScience/Avanzado/Prework Streamlit/Model Keras Frutas y Verduras/keras_model.h5')

siteHeader = st.beta_container()
with siteHeader:
    st.title('Modelo de reconocimiento de frutas y verduras')
    st.markdown(""" En este proyecto se busca poder identificar entre frutas y verduras""")
