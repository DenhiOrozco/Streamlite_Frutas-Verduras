import streamlit as st

siteHeader = st.beta_container()
with siteHeader:
    st.title('Modelo de reconocimiento de frutas y verduras')
    st.markdown(""" En este proyecto se busca poder subir una imagen de una fruta o verdura y dejar que el modelo identifique qué es entre las siguientes frutas y verduras:""")
    

import tensorflow.keras
from PIL import Image, ImageOps 
import numpy as np

#Quitar la notación científica para claridad
np.set_printoptions(suppress=True)

#Cargar el modelo hecho en Teachable Machine con data de Kaggle
model= tensorflow.keras.models.load_model('/saved_model.pb')

#Crear un array del tamaño correcto para cargar al modelo de keras
#El largo de las imágenes que se pueden poner en el array está determinado por la primera posición de la tupla de forma.

data= np.ndarray(shape=(1,224,224,3), dtype=np.float32)
