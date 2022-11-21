import requests
import pandas as pd
import numpy as np
import streamlit as st
#city_name = input("Enter the name of the City : ")
dati1=[]
url_list=('https://wttr.in/Gdynia?format=%m+%t','https://wttr.in/Gdynia?format=%h',
         'https://wttr.in/Milan?format=%m+%t','https://wttr.in/Milan?format=%h')
for url_list in url_list:
    dati=((requests.get(url_list).text))
    np.array(dati1.append(dati))
    #np.append(print(requests.get(dati).text))
#b=pd.DataFrame(np.array(dati1),columns=['TEMP','TEMP-PERCEPITA'])#,'UMIDITA^','ORA-LOCALE-DATI'])

#a=((pd.DataFrame((np.array(dati1).reshape(2,-1)),columns=['TEMP','UMIDITA^'])).T)#,columns=['Gdynia','Milano'])
a=pd.DataFrame((np.array(dati1).reshape(-1,2)),columns=['temperatura','umidita^'],index=['Gdynia','Milano'])
b=(a.T)

#print(b)
st.subheader((b['Gdynia']))
             
st.subheader((b['Milano']))
