import streamlit as st
import joblib  # or pickle if you're using that

# App title
st.title("💊 Medical Recommendation System")

# Load your trained model (update with correct path and library)
model = joblib.load('your_model_file.pkl')  # Replace with your actual model file path

# Input fields for symptoms
symptoms = st.text_input("Enter symptoms (comma-separated):")

if st.button("Get Recommendation"):
    # Preprocess the input (make sure it matches what your model expects)
    symptom_list = symptoms.lower().split(",")  # Adjust based on your model's requirement
    # Convert to model input format (e.g., vectorize if necessary)
    # X = your_preprocessing_function(symptom_list)

    # Get prediction from model (replace this with your model's prediction logic)
    prediction = model.predict([symptom_list])  # Modify based on your model's input structure

    # Display the result
    st.success(f"Recommended Medicine: {prediction[0]}")  # Replace with actual model output
