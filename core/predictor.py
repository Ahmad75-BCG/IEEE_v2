import joblib
import os

def get_prediction(occupancy, temp):
    model_path = 'models/energy_v1.pkl'
    if not os.path.exists(model_path):
        return "Model not trained yet."
    
    model = joblib.load(model_path)
    prediction = model.predict([[occupancy, temp]])
    return prediction[0]