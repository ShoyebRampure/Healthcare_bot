from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
import re

app = Flask(__name__)

# Paths to your models and data (using your relative paths)
decision_tree_model_path = r'model\disease_prediction_model.pkl'
svm_model_path = r'model\svm_disease_prediction_model.pkl'
training_file = r'Data\Training.csv'

# Load models and training data with proper error handling
try:
    # Check if files exist before loading
    if not os.path.exists(decision_tree_model_path):
        raise FileNotFoundError(f"Decision tree model not found at: {decision_tree_model_path}")
    
    if not os.path.exists(svm_model_path):
        raise FileNotFoundError(f"SVM model not found at: {svm_model_path}")
    
    if not os.path.exists(training_file):
        raise FileNotFoundError(f"Training data not found at: {training_file}")
    
    # Load the models
    with open(decision_tree_model_path, 'rb') as file:
        clf = pickle.load(file)
    
    with open(svm_model_path, 'rb') as file:
        svm_model = pickle.load(file)
    
    # Load training data
    training = pd.read_csv(training_file)
    cols = training.columns[:-1]  # All columns except the last one (prognosis)
    
    # Mapping strings to numbers
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(training['prognosis'])
    
    # Create symptoms dictionary
    symptoms_dict = {symptom: index for index, symptom in enumerate(cols)}
    
    print(f"✅ Models loaded successfully!")
    print(f"✅ Available symptoms: {len(symptoms_dict)}")
    print(f"✅ Sample symptoms: {list(cols[:5])}")
    
except FileNotFoundError as e:
    print(f"❌ File Error: {e}")
    print("📁 Please ensure your folder structure is:")
    print("   your_project/")
    print("   ├── app.py")
    print("   ├── Data\\Training.csv")
    print("   ├── model\\disease_prediction_model.pkl")
    print("   └── model\\svm_disease_prediction_model.pkl")
    clf = None
    svm_model = None
    symptoms_dict = {}
    le = None
    
except Exception as e:
    print(f"❌ Error loading models or data: {e}")
    clf = None
    svm_model = None
    symptoms_dict = {}
    le = None

# Function to check for matching symptoms with better pattern matching
def check_pattern(symptoms_list, symptom_input):
    symptom_input = symptom_input.lower().strip()
    
    # Replace common separators with underscores
    symptom_input = re.sub(r'[\s\-\.]+', '_', symptom_input)
    
    matches = []
    
    # Direct match
    if symptom_input in symptoms_list:
        matches.append(symptom_input)
    
    # Partial match
    for symptom in symptoms_list:
        symptom_lower = symptom.lower()
        if symptom_input in symptom_lower or symptom_lower in symptom_input:
            if symptom not in matches:
                matches.append(symptom)
    
    # Pattern matching for variations
    pattern = re.compile(symptom_input, re.IGNORECASE)
    for symptom in symptoms_list:
        if pattern.search(symptom.replace('_', ' ')) and symptom not in matches:
            matches.append(symptom)
    
    return matches[:3]  # Return top 3 matches

# Function to predict disease based on symptoms
def predict_disease(symptoms_list):
    if not clf or not svm_model or not symptoms_dict:
        return "Model not loaded", "Model not loaded"
    
    input_vector = np.zeros(len(symptoms_dict))
    matched_symptoms = []
    
    for symptom in symptoms_list:
        matches = check_pattern(list(symptoms_dict.keys()), symptom)
        for match in matches:
            if match in symptoms_dict:
                input_vector[symptoms_dict[match]] = 1
                matched_symptoms.append(match)
    
    if not matched_symptoms:
        return "No symptoms matched", "No symptoms matched"
    
    try:
        decision_tree_prediction = clf.predict([input_vector])[0]
        svm_prediction = svm_model.predict([input_vector])[0]
        
        dt_disease = le.inverse_transform([decision_tree_prediction])[0]
        svm_disease = le.inverse_transform([svm_prediction])[0]
        
        return dt_disease, svm_disease
    except Exception as e:
        print(f"Prediction error: {e}")
        return "Prediction failed", "Prediction failed"

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        print("=== DEBUG: get_response called ===")
        data = request.get_json()
        print(f"Received data: {data}")
        
        message = data.get('message', '').strip()
        print(f"Message: '{message}'")
        
        if not message:
            return jsonify({'bot_response': 'Please provide a symptom.'})
        
        if not symptoms_dict:
            return jsonify({'bot_response': 'Sorry, the medical database is not loaded. Please check the server logs.'})
        
        # Check for matching symptoms
        matches = check_pattern(list(symptoms_dict.keys()), message)
        print(f"Found matches: {matches}")
        
        if matches:
            response = f"✅ Found matching symptom: '{matches[0]}'. This has been recorded."
        else:
            # Try to find partial matches
            partial_matches = []
            message_lower = message.lower().replace(' ', '_')
            
            for symptom in list(symptoms_dict.keys()):
                symptom_lower = symptom.lower()
                if (message_lower in symptom_lower or 
                    symptom_lower in message_lower or 
                    message.lower() in symptom.replace('_', ' ').lower()):
                    partial_matches.append(symptom)
                    if len(partial_matches) >= 3:
                        break
            
            if partial_matches:
                response = f"🔍 Found similar symptoms: {', '.join(partial_matches[:3])}. I'll use '{partial_matches[0]}' for analysis."
            else:
                # Show some available symptoms as suggestions
                sample_symptoms = list(symptoms_dict.keys())[:10]
                formatted_symptoms = [s.replace('_', ' ') for s in sample_symptoms]
                response = f"❌ Couldn't find '{message}' in our database. Try symptoms like: {', '.join(formatted_symptoms[:5])}"
        
        print(f"Response: {response}")
        return jsonify({'bot_response': response})
        
    except Exception as e:
        print(f"❌ Error in get_response: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'bot_response': 'Sorry, there was an error processing your request.'})

@app.route('/send_symptoms', methods=['POST'])
def send_symptoms():
    try:
        print("=== DEBUG: send_symptoms called ===")
        data = request.get_json()
        symptoms_list = data.get('symptoms', [])
        
        print(f"Received symptoms: {symptoms_list}")
        
        if not symptoms_list:
            return jsonify({'error': 'No symptoms provided'})
        
        if not clf or not svm_model:
            return jsonify({'error': 'Models not loaded properly'})
        
        # Predict disease
        dt_prediction, svm_prediction = predict_disease(symptoms_list)
        print(f"Predictions - DT: {dt_prediction}, SVM: {svm_prediction}")
        
        # Format the response
        response = {
            'decision_tree_prediction': dt_prediction,
            'svm_prediction': svm_prediction,
            'symptoms_processed': symptoms_list,
            'diagnosis': f"Based on your symptoms, our models suggest:\n\nDecision Tree Model: {dt_prediction}\nSVM Model: {svm_prediction}\n\nPlease consult with a healthcare professional for proper diagnosis and treatment."
        }
        
        print(f"Sending response: {response}")
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error in send_symptoms: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Error processing symptoms: {str(e)}'})

@app.route('/get_available_symptoms', methods=['GET'])
def get_available_symptoms():
    """Return list of available symptoms for frontend suggestions"""
    try:
        # Return a sample of symptoms for suggestions
        sample_symptoms = list(symptoms_dict.keys())[:50]  # First 50 symptoms
        formatted_symptoms = [symptom.replace('_', ' ').title() for symptom in sample_symptoms]
        return jsonify({'symptoms': formatted_symptoms})
    except Exception as e:
        return jsonify({'symptoms': ['headache', 'fever', 'cough', 'nausea']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)