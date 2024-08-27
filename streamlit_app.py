import streamlit as st
import pickle
import numpy as np

# Load your model (adjust the path accordingly)
model_path = 'modeltask.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Diabetes Model Prediction")

# Input features
pregnancies = st.text_input("Enter Pregnancies:")
Glucose = st.text_input("Enter Glucose :")
insulin = st.text_input("Enter Insulin :")
bmi = st.text_input("Enter BMI :")
diabetesPedigreeFunction = st.text_input("Enter DiabetesPedigreeFunction :")
age = st.text_input("Enter Age :")

# Button for prediction
if st.button("Predict"):
    # Convert features to a numpy array
    features = np.array([[float(pregnancies), float(Glucose), float(insulin),float(bmi),float(diabetesPedigreeFunction),float(age)]])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Display the prediction
    st.write(f" Diabetes Prediction is : {prediction[0]}")
