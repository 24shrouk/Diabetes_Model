from sklearn.tree import DecisionTreeClassifier
import numpy as np
import streamlit as st
import pickle

# Load the model
with open('model (3).pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_diabetes(pregnancies, glucose, insulin, bmi, pedigree, age):
    features = np.array([[
        int(pregnancies), int(glucose), int(insulin),
        float(bmi), float(pedigree), int(age)
    ]])
    prediction = model.predict(features)
    return prediction[0]

# Streamlit app
st.title('Diabetes Prediction App')

st.write("Enter the following details:")

pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0)
glucose = st.number_input('Glucose', min_value=0, max_value=200, value=0)
insulin = st.number_input('Insulin', min_value=0, max_value=1000, value=0)
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=0.0)
pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.0)
age = st.number_input('Age', min_value=0, max_value=120, value=0)

if st.button('Predict'):
    result = predict_diabetes(pregnancies, glucose, insulin, bmi, pedigree, age)
    if result == 1:
        st.write("The model predicts: **Diabetic**")
    else:
        st.write("The model predicts: **Not Diabetic**")

