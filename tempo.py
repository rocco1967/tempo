import requests
import pandas as pd
import numpy as np
import streamlit as st
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
url_list=('https://wttr.in/Gdynia?m&format=%t','https://wttr.in/Gdynia?format=%h','https://wttr.in/Gdynia?format=%f',
         'https://wttr.in/Milan?m&format=%t','https://wttr.in/Milan?format=%h','https://wttr.in/Milan?format=%f')
for url_list in url_list:
    dati=((requests.get(url_list).text))
    np.array(dati1.append(dati))
    #np.append(print(requests.get(dati).text))
#b=pd.DataFrame(np.array(dati1),columns=['TEMP','TEMP-PERCEPITA'])#,'UMIDITA^','ORA-LOCALE-DATI'])

#a=((pd.DataFrame((np.array(dati1).reshape(2,-1)),columns=['TEMP','UMIDITA^'])).T)#,columns=['Gdynia','Milano'])
a=pd.DataFrame((np.array(dati1).reshape(-1,3)),columns=['temperatura','umidita^'],index=['Gdynia','Milano'])
b=(a.T)
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;"</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.dataframe(b['Gdynia'],400,100)
st.markdown('-----')
st.dataframe(b['Milano'],400,100)
#print(b)
#st.subheader((b['Gdynia']))
             
#st.subheader((b['Milano']))
