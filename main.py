pip install keras streamlit pillow numpy
import streamlit as st
import keras
from PIL import Image, ImageOps
import numpy as np

siteHeader = st.beta_container()
with siteHeader:
    st.title('Modelo de reconocimiento de frutas y verduras')
    st.markdown(""" En este proyecto se busca poder subir una imagen de una fruta o verdura y dejar que el modelo identifique qué es entre las siguientes frutas y verduras:""")
    

#Quitar la notación científica para claridad
#np.set_printoptions(suppress=True)

#Cargar el modelo hecho en Teachable Machine con data de Kaggle
def teachable_machine_classification(img, weights_file):
    model= keras.models.load_model(weights_file)
    st.title('Modelo ok')
    #Crear un array del tamaño correcto para cargar al modelo de keras
    #El largo de las imágenes que se pueden poner en el array está determinado por la primera posición de la tupla de forma.

    data= np.ndarray(shape=(1,224,224,3), dtype=np.float32)
    
    image = img
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    #ejecuta la inferencia
    prediction=model.predict(data)
    np.argmax(prediction)

def resultado_modelo():
    resultado= np.argmax(prediction)
    if resultado ==0:
        print('Sandía')
    elif resultado ==1:
        print('Tomate')
    elif resultado ==2:
        print('Papa')
    elif resultado ==3:
        print('Piña')
    elif resultado ==4:
        print('Pera')
    elif resultado ==5:
        print('Naranja')
    elif resultado ==6:
        print('Cebolla')
    elif resultado ==7:
        print('Mango')
    elif resultado ==8:
        print('Limón')
    elif resultado ==9:
        print('Uvas')
    elif resultado ==10:
        print('Gengibre')
    elif resultado ==11:
        print('Ajo')
    elif resultado ==12:
        print('Berenjena')
    elif resultado ==13:
        print('Pepino')
    elif resultado ==14:
        print('Elote')
    elif resultado ==15:
        print('Chiles')
    elif resultado ==16:
        print('Coliflor')
    elif resultado ==17:
        print('Zanahoria')
    elif resultado ==18:
        print('Pimiento')
    elif resultado ==19:
        print('Col')
    elif resultado ==20:
        print('Betabel')
    elif resultado ==21:
        print('Plátano')
    elif resultado ==22:
        print('Manzana')
    else:
        print('No te pases, ¿qué es eso?')

resultado_modelo()
