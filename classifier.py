# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:47:10 2024

@author: matta
"""

import pickle
import streamlit as st

# Load the model (assuming the vectorizer is bundled inside the model file)
loaded_model = pickle.load(open("classifier.sav", 'rb'))

# Define function for tweet classification
def custom_input_prediction(text):
    # Convert the input text to a list (or format required by the model)
    text = [text]
    
    # Predict the class using the loaded model
    prediction = loaded_model.predict(text)
    prediction = prediction[0]

    # Define interpretation mappings
    interpretations = {
        0: "Age",
        1: "Ethnicity",
        2: "Gender",
        3: "Not Cyberbullying",
        4: "Other Cyberbullying",
        5: "Religion"
    }

    # Return the corresponding interpretation
    return interpretations[prediction]

# Main function to create the web app
def main():
    st.title("Tweet Cyberbullying Classifier")
    
    # Input tweet for classification
    tweet_text = st.text_input('Enter the tweet text:')
    
    # Available for prediction
    classification_result = ''
    
    if st.button('Classify Tweet'):
        classification_result = custom_input_prediction(tweet_text)
    
    st.success(f"Classification: {classification_result}")

if __name__ == '__main__':
    main()