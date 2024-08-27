import streamlit as st
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier


# Load your model
model_path = 'model (3).pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Diabetes Model Prediction")

# Input features with default empty strings
pregnancies = st.text_input("Enter Pregnancies:", "0")
glucose = st.text_input("Enter Glucose:", "0")
insulin = st.text_input("Enter Insulin:", "0")
bmi = st.text_input("Enter BMI:", "0.0")
diabetesPedigreeFunction = st.text_input("Enter DiabetesPedigreeFunction:", "0.0")
age = st.text_input("Enter Age:", "0")

# Button for prediction
if st.button("Predict"):
    try:
        # Ensure all inputs are filled and convert them
        if pregnancies and glucose and insulin and bmi and diabetesPedigreeFunction and age:
            features = np.array([[
                int(pregnancies), int(glucose), int(insulin),
                float(bmi), float(diabetesPedigreeFunction), int(age)
            ]])
            prediction = model.predict(features)
            
            # Display the prediction
            result = "Diabetes" if prediction[0] == 1 else "No Diabetes"
            st.write(f"Diabetes Prediction is: {result}")
        else:
            st.write("Please enter valid numeric values for all inputs.")
    except ValueError:
        st.write("Please enter valid numeric values for all inputs.")
