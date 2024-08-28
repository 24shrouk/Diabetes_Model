
import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load('model (3).pkl')  # Replace with your model path

def predict_diabetes(pregnancies, glucose, insulin, bmi, pedigree, age):
    # Create a DataFrame with the input features
    features = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [pedigree],
        'Age': [age]
    })
    
    # Ensure the input DataFrame has the correct columns
    expected_columns = ['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    if list(features.columns) != expected_columns:
        raise ValueError(f"Input DataFrame columns do not match. Expected: {expected_columns}, but got: {list(features.columns)}")
    
    # Predict using the model
    prediction = model.predict(features)
    return prediction[0]

st.title("Diabetes Prediction")

# Input fields
pregnancies = st.number_input('Enter Pregnancies', min_value=0, value=0)
glucose = st.number_input('Enter Glucose', min_value=0.0, value=0.0)
insulin = st.number_input('Enter Insulin', min_value=0.0, value=0.0)
bmi = st.number_input('Enter BMI', min_value=0.0, value=0.0)
pedigree = st.number_input('Enter Diabetes Pedigree Function', min_value=0.0, value=0.0)
age = st.number_input('Enter Age', min_value=0, value=0)

if st.button('Predict'):
    try:
        # Call the predict function and display the result
        prediction = predict_diabetes(pregnancies, glucose, insulin, bmi, pedigree, age)
        st.write(f'Prediction: {"Diabetic" if prediction == 1 else "Not Diabetic"}')
    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


