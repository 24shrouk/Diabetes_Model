
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
 features = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [pedigree],
        'Age': [age]
    })
    
    # Ensure the input DataFrame has the correct columns
    feature_columns = ['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    if not all(col in features.columns for col in feature_columns):
        raise ValueError("Input DataFrame does not have the required columns.")
    
    # Predict using the model



# Button for prediction
if st.button("Predict"):
    try:
        # Convert inputs to the correct numeric types
        pregnancies = int(pregnancies.strip())
        glucose = int(glucose.strip())
        insulin = int(insulin.strip())
        bmi = float(bmi.strip())
        diabetesPedigreeFunction = float(diabetesPedigreeFunction.strip())
        age = int(age.strip())

        # Ensure all values are non-negative numbers
        if pregnancies < 0 or glucose < 0 or insulin < 0 or bmi < 0 or diabetesPedigreeFunction < 0 or age < 0:
            st.write("Please enter positive numeric values for all inputs.")
        else:
            # Prepare the input array
                prediction = model.predict(features)
           

            # Display the prediction
            result = "Diabetes" if prediction[0] == 1 else "No Diabetes"
            st.write(f"Diabetes Prediction is: {result}")
            
    except ValueError as e:
        # Show an error message if conversion fails
        st.write(f"Error in input conversion: {e}")
        st.write("Please enter valid numeric values for all inputs.")
