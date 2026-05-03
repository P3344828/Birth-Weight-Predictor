# Baby Birth Weight Predictor 👶⚖️

An end-to-end Machine Learning web application that predicts an infant's birth weight based on maternal health factors. Built with a strong focus on Software Engineering best practices.

## 🚀 Features

- **Accurate Predictions**: Uses a trained Scikit-Learn Machine Learning model to estimate birth weight.
- **Robust REST API**: Built using Flask Blueprints for a modular and maintainable backend architecture.
- **Dual Data Handling**: The `/predict` endpoint seamlessly handles both JSON payloads (for API integrations) and HTML form submissions.
- **Strict Input Validation**: Gracefully handles missing or invalid data, returning proper HTTP 400 Bad Request responses to ensure server stability.
- **Unit Testing**: Comprehensive unit tests written using Pytest to guarantee API reliability.
- **User-Friendly Interface**: Modern, responsive, and glassmorphism-inspired frontend design.

## 🛠️ Technology Stack

- **Backend**: Python, Flask (Blueprints)
- **Frontend**: HTML5, CSS3
- **Machine Learning**: Scikit-Learn, Pandas, Pickle
- **Testing**: Pytest

## 📂 Project Structure

```
├── app.py                 # Main Flask application entry point
├── extentions.py          # Flask extensions configuration
├── model.pkl              # Trained Machine Learning model
├── model_training.ipynb   # Jupyter Notebook for EDA & Model Training
├── requirements.txt       # Python dependencies
├── test_app.py            # Pytest Unit Tests for the API
├── routes/
│   ├── predict.py         # Prediction API Blueprint
│   └── user.py            # User operations Blueprint
├── static/
│   └── style.css          # Custom CSS styling
├── templates/
│   └── index.html         # Frontend Web UI
└── dataset/               # Source data
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

5.  **Run Unit Tests**
    To verify the API endpoints, run:
    ```bash
    pytest test_app.py
    ```

## 📝 Input Parameters

To get a prediction, you need to provide:
- **Gestation**: Duration of pregnancy in days.
- **Parity**: Number of previous births (0 or 1+).
- **Age**: Mother's age in years.
- **Height**: Mother's height in inches.
- **Weight**: Mother's weight in pounds.
- **Smoking Status**: 0 (Non-smoker) or 1 (Smoker).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check issues page or submit a Pull Request.
