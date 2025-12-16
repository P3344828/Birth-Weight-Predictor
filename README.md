# Baby Birth Weight Predictor 👶⚖️

A Machine Learning powered web application that predicts a baby's birth weight based on maternal factors.

## 🚀 Features

- **Accurate Predictions**: Uses a trained Machine Learning model to estimate birth weight.
- **User-Friendly Interface**: Modern, responsive design that works on mobile and desktop.
- **Real-time Results**: Instant prediction display without page reloads (simulated via rapid server response).
- **Secure**: Input validation ensures data quality.

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3 (Custom Responsive Design)
- **Machine Learning**: Scikit-learn, Pandas, Pickle
- **Data Processing**: Pandas

## 📂 Project Structure

```
├── app.py                 # Main Flask application
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Custom CSS styling
├── templates/
│   └── index.html        # Web interface
└── dataset/              # (Optional) Source data
```

## ⚙️ Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone https://github.com/P3344828/Birth-Weight-Predictor.git
    cd Birth-Weight-Predictor
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python app.py
    ```

4.  **Access the App**
    Open your browser and navigate to: `http://127.0.0.1:5000/`

## 📝 Input Parameters

To get a prediction, you need to provide:
- **Gestation**: Duration of pregnancy in days.
- **Parity**: Number of previous births.
- **Age**: Mother's age in years.
- **Height**: Mother's height in inches.
- **Weight**: Mother's weight in pounds.
- **Smoking Status**: 0 (Non-smoker) or 1 (Smoker).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
