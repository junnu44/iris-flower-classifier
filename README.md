🚀 Features

- Predicts iris species: *Setosa, Versicolor, or Virginica*
- Built using Scikit-learn and Streamlit
- Lightweight, interactive UI
- Model trained using 80/20 train-test split
- Encoded labels for better performance

 📊 Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- Contains 150 samples, 4 features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Target: Species of iris (Setosa, Versicolor, Virginica)

 🧠 Model

- **Algorithm:** RandomForestClassifier (from `sklearn.ensemble`)
- **Accuracy:** Achieved >95% accuracy on test data
- Model and Label Encoder saved using `joblib`

 🖥️ Run Locally

1. Clone the repository:
  
   git clone https://github.com/junnu44/iris-flower-classifier.git
   cd iris-flower-classification
Install the dependencies:


pip install -r requirements.txt
Run the app:


streamlit run iris_app.py
The app will open at http://localhost:8501/

live app: https://iris-flower-classifier-5i8ivka8guehaufwkhalcd.streamlit.app/

📁 Project Structure

📦 iris-flower-classification
├── IRIS.csv
├── iris_app.py
├── iris_model.pkl
├── label_encoder.pkl
├── model_training.py
├── requirements.txt
└── README.md
