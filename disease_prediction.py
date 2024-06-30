#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:46:27 2024

@author: gangarajuthellakula
"""

import pickle
import streamlit as st 
from streamlit_option_menu import option_menu


#loading saved model

diabetes_model = pickle.load(open('/Users/gangarajuthellakula/Desktop/multiple_diesease_prediction/untitled folder/diabetes_model.sav','rb'))

#sidebar for navigate

with st.sidebar:
    selected = option_menu('multiple_disease_prediction',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                           icons = ['activity','heart'],
                           default_index=0)

if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction Using ML')
    
    
    
    Pregnancies = st.text_input('Number of Pregnancies:')
    Glucose = st.text_input('Glucose level:')
    BloodPressure = st.text_input('BloodPressure level:')
    SkinThickness = st.text_input('Skin Thickness:')
    Insulin = st.text_input('Insulin level:')
    BMI = st.text_input('BMI value:')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value:')
    Age = st.text_input('Age of Patient:')
    
    
    
    
    
    diab_diagnosis = ''
    
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if diab_prediction[0]==1:
            diab_diagnosis = 'The person is diabetic'
        
        else:
            diab_diagnosis = 'The person is not diabetic ......'
            
    st.success(diab_diagnosis)
    
    
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using ML')