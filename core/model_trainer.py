import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model():
    # Mock data for training
    data = pd.DataFrame({
        'occupancy': [10, 20, 30, 40, 50, 60, 20, 10],
        'temp': [22, 23, 24, 25, 26, 22, 21, 20],
        'energy_kwh': [100, 150, 200, 250, 300, 350, 140, 95]
    })
    
    X = data[['occupancy', 'temp']]
    y = data['energy_kwh']
    
    # Initialize and train the model
    trained_model = RandomForestRegressor(n_estimators=100)
    trained_model.fit(X, y)
    return trained_model

if __name__ == "__main__":
    # 1. Train the model
    model = train_model()
    
    # 2. Define the exact path the Dashboard expects
    # This creates the file in /app/core/models/energy_v1.pkl
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(script_dir, 'models')
    save_path = os.path.join(save_dir, 'energy_v1.pkl')
    
    # 3. Ensure the directory exists
    os.makedirs(save_dir, exist_ok=True)
    
    # 4. Save
    joblib.dump(model, save_path)
    print(f"✅ Success! Model trained and saved to: {save_path}")