import streamlit as st
from sklearn.svm import SVC
from pickle import dump, load
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def predict(df):
    std_df=StandardScaler().fit_transform(df)
    classifier=load(open("pickle\classifier.pkl",'rb'))
    predicted=classifier.predict(std_df)
    return predicted

def main():
    x=[st.text_input('enter col1')]
    y=[st.text_input('enter col2')]
    data=['col1','col2']
    df=pd.DataFrame(columns=data)
    df.col1=x
    df.col2=y
    click=st.button('SUBMIT')
    if click:
        predict(df)
        if predict==0:
            st.write('zero')
        else:
            st.write('one')


if(__name__ == '__main__'):
    main()
