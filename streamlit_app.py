
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
import pickle
import numpy as np

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
diabetesPedigreeFunction = st.text_input("Enter Diabetes Pedigree Function:", "0.0")
age = st.text_input("Enter Age:", "0")

# Button for prediction
if st.button("Predict"):
    try:
        # Convert inputs to the correct numeric types
        pregnancies = int(float(pregnancies.strip()))
        glucose = int(float(glucose.strip()))
        insulin = int(float(insulin.strip()))
        bmi = float(bmi.strip())
        diabetesPedigreeFunction = float(diabetesPedigreeFunction.strip())
        age = int(float(age.strip()))

        # Ensure all values are non-negative numbers
        if pregnancies < 0 or glucose < 0 or insulin < 0 or bmi < 0 or diabetesPedigreeFunction < 0 or age < 0:
            st.write("Please enter positive numeric values for all inputs.")
        else:
            # Prepare the input array
            features = np.array([[pregnancies, glucose, insulin, bmi, diabetesPedigreeFunction, age]])
            prediction = model.predict(features)

            # Display the prediction
            result = "Diabetes" if prediction[0] == 1 else "No Diabetes"
            st.write(f"Diabetes Prediction is: {result}")
            
    except ValueError as e:
        # Show an error message if conversion fails
        st.write(f"Error in input conversion: {e}")
        st.write("Please enter valid numeric values for all inputs.")
