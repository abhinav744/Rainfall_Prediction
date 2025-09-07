# 🌧️ Rainfall Prediction

This project aims to predict rainfall using machine learning techniques. By analyzing historical weather data, the model forecasts the likelihood of rainfall, which is crucial for agriculture, water resource management, and disaster preparedness.

## 🚀 Live Demo

Experience the model in action:

[Rainfall Prediction App](https://rainfallprediction-hi6lgfeuxlnajbs5m52cje.streamlit.app/)

## 🧠 Features

Machine Learning Model: Trained on historical weather data to predict rainfall.

User Interface: Built with Streamlit for easy interaction.

Real-time Predictions: Input weather data and get instant rainfall predictions.

## 📂 Project Structure
```
📁 Rainfall_Prediction
 ┣ 📄 app.py              # Streamlit application script
 ┣ 📄 requirements.txt    # Python dependencies
 ┣ 📄 Rainfall.csv        # Dataset of historical weather data
 ┣ 📄 rainfall_prediction_model.pkl  # Trained machine learning model
 ┗ 📄 README.md           # Project documentation
```

## ⚙️ Installation & Setup
```
# Clone the repository
git clone https://github.com/abhinav744/Rainfall_Prediction.git
cd Rainfall_Prediction

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📊 Dataset

The project utilizes a dataset containing historical weather data, including features such as:

Temperature

Humidity

Wind Speed

Pressure

These features are used to predict the likelihood of rainfall.

## 🧪 Model Details

Preprocessing: Data cleaning and feature engineering.

Model Type: Machine learning model (Random Forest).

Evaluation: Model performance metrics (e.g., accuracy, precision, recall).

## 🌐 Usage

Launch the app with:
```
streamlit run app.py
```

Or use the live app directly:

[👉 Rainfall Prediction App](https://rainfallprediction-hi6lgfeuxlnajbs5m52cje.streamlit.app/)

Input weather data and get a Rainfall Prediction.
