
from sklearn.tree import DecisionTreeClassifier

   
     import streamlit as st
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load your model (adjust the path accordingly)
model_path = 'model (3).pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Diabetes Model Prediction")

# Input features
pregnancies = st.text_input("Enter Pregnancies:")
glucose = st.text_input("Enter Glucose:")
insulin = st.text_input("Enter Insulin:")
bmi = st.text_input("Enter BMI:")
diabetesPedigreeFunction = st.text_input("Enter DiabetesPedigreeFunction:")
age = st.text_input("Enter Age:")

# Button for prediction
if st.button("Predict"):
    try:
        # Convert features to a numpy array and ensure they are numeric
        features = np.array([[
            int(pregnancies), int(glucose), int(insulin),
            float(bmi), float(diabetesPedigreeFunction), int(age)
        ]])
        prediction = model.predict(features)
        
        # Display the prediction
        st.write(f"Diabetes Prediction is: {prediction[0]}")
    except ValueError:
        st.write("Please enter valid numeric values for all inputs.")
