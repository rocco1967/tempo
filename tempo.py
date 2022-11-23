import requests
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from dataframe_to_image import dataframe_to_image
st.set_option('deprecation.showPyplotGlobalUse', False)
image1 = Image.open('gdynia.JPG')
image2= Image.open('milano.JPG')
#st.image(image1)
#st.image(image2)
#st.set_page_config(layout="center")
st.markdown(
    """
    <style>
    textarea {
        font-size: 3rem !important;
    }
    input {
        font-size: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
dati1=[]
url_list=('https://wttr.in/Gdynia?m&format=%t&period=5','https://wttr.in/Gdynia?format=%h&period=5','https://wttr.in/Gdynia?m&format=%f&','https://wttr.in/Gdynia?format=%s',
          'https://wttr.in/Gdynia?format=%S',
          
         'https://wttr.in/Milan?m&format=%t&period=5','https://wttr.in/Milan?format=%h&period=5','https://wttr.in/Milan?m&format=%f','https://wttr.in/Milan?format=%s',
         'https://wttr.in/Milan?format=%S')
for url_list in url_list:
    dati=((requests.get(url_list,timeout=2,headers={'Connection':'close'}).text))
    #requests.close()
    np.array(dati1.append(dati))
    #np.append(print(requests.get(dati).text))
#b=pd.DataFrame(np.array(dati1),columns=['TEMP','TEMP-PERCEPITA'])#,'UMIDITA^','ORA-LOCALE-DATI'])
#requests.close()
#a=((pd.DataFrame((np.array(dati1).reshape(2,-1)),columns=['TEMP','UMIDITA^'])).T)#,columns=['Gdynia','Milano'])
a=pd.DataFrame((np.array(dati1).reshape(-1,5)),columns=['temperatura','umidita^','temp-percepita','Sunset','Sunrise'],index=['Gdynia','Milano'])
b=(a.T)
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;"</p>'
#st.markdown(new_title, unsafe_allow_html=True)
#st.dataframe(b,300,200)########  originale
b=(b.reset_index()).rename(columns={'index': 'dati'})##  nuovo
b1=b['dati','Gdynia']
b2=b[['Milano']]
#kwargs=dict{figsize:10,5}#(figsize=(10,5))
#b1=dataframe_to_image.convert(b,visualisation_library='matplotlib')

col1, col2 = st.columns(2)
with col1:
   st.header("Gdynia")
   image1=image1.resize((400,300))
   st.image(image1)
   st.pyplot(dataframe_to_image.convert(b1,visualisation_library='matplotlib'))####   originale
with col2:
   st.header("Milano")
   image2=image2.resize((400,300)) 
   st.image(image2)
   st.pyplot(dataframe_to_image.convert(b2,visualisation_library='matplotlib'))####   originale
    

#st.pyplot(dataframe_to_image.convert(b1,visualisation_library='matplotlib'))####   originale
#st.pyplot(dataframe_to_image.convert(b2,visualisation_library='matplotlib'))####   originale
#st.plotly_chart(dataframe_to_image.convert(b,visualisation_library='matplotlib'))####   originale








