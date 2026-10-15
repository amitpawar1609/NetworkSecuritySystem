# 🛡️ Network Security System

An end-to-end machine learning system built in Python that detects malicious / phishing network activity. The project covers the full ML lifecycle: data ingestion, validation, transformation, model training, experiment tracking, and serving predictions through a web API.

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
<!-- TODO: add CI / Docker badges if applicable -->

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [Deployment](#-deployment)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 Overview

Cyber threats such as phishing websites and malicious traffic are growing in volume and sophistication. This project uses machine learning to classify network/URL data as **legitimate** or **malicious**, helping security teams flag threats automatically.

**Key goals:**
- Build a modular, production-style ML pipeline
- Track experiments and model versions
- Serve real-time and batch predictions through an API

---

## ✨ Features

- **ETL pipeline** – extracts raw data and loads it into a database
- **Data validation** – schema checks and data drift detection
- **Data transformation** – missing-value imputation and feature preprocessing
- **Model training** – trains and compares multiple classifiers with hyperparameter tuning
- **Experiment tracking** – logs metrics and models (e.g., MLflow)
- **Custom logging & exception handling** – for easy debugging
- **REST API** – endpoints to trigger training and make predictions
- **Containerized** – ready to run with Docker

---

## 🏗️ Architecture

```
Raw Data ──► Data Ingestion ──► Data Validation ──► Data Transformation
                                                            │
                                                            ▼
    Prediction API ◄── Model Pusher ◄── Model Evaluation ◄── Model Trainer
```

Each stage produces an **artifact** (stored in `Artifacts/`) that is consumed by the next stage.

---

## 🧰 Tech Stack

| Category            | Tools                                   |
|---------------------|-----------------------------------------|
| Language            | Python 3.14                             |
| ML / Data           | scikit-learn, pandas, NumPy             |
| Database            | MongoDB <!-- TODO: confirm -->          |
| Experiment Tracking | MLflow <!-- TODO: confirm -->           |
| API                 | FastAPI / Flask <!-- TODO: confirm -->  |
| Deployment          | Docker, GitHub Actions, AWS <!-- TODO --> |

---

## 📂 Project Structure

```
networkSecurity/
├── networksecurity/
│   ├── components/          # Pipeline stages (ingestion, validation, transformation, trainer)
│   ├── constant/            # Constants and config values
│   ├── entity/              # Config and artifact entity classes
│   ├── exception/           # Custom exception handling
│   ├── logging/             # Custom logger
│   ├── pipeline/            # Training and prediction pipelines
│   └── utils/               # Helper functions
├── data_schema/
│   └── schema.yaml          # Expected data schema
├── Network_Data/            # Raw dataset
├── final_model/             # Saved model and preprocessor
├── templates/               # HTML templates for prediction output
├── app.py                   # API entry point
├── main.py                  # Run the training pipeline
├── push_data.py             # ETL script to load data into the database
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```
<!-- TODO: update to match your actual folders -->

---

## 🚀 Getting Started

### Prerequisites
- Python 3.14
- Git
- MongoDB Atlas account (or local MongoDB)
- (Optional) Docker

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/networkSecurity.git
cd networkSecurity

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
MONGO_DB_URL=mongodb+srv://<user>:<password>@<cluster>/
MLFLOW_TRACKING_URI=<your-mlflow-uri>
MLFLOW_TRACKING_USERNAME=<username>
MLFLOW_TRACKING_PASSWORD=<token>
```

| Variable                  | Description                         |
|---------------------------|-------------------------------------|
| `MONGO_DB_URL`            | Connection string for MongoDB       |
| `MLFLOW_TRACKING_URI`     | Remote MLflow tracking server URL   |
| `MLFLOW_TRACKING_USERNAME`| MLflow / DagsHub username           |
| `MLFLOW_TRACKING_PASSWORD`| MLflow / DagsHub access token       |

> ⚠️ Never commit your `.env` file. Make sure it's listed in `.gitignore`.

---

## 💻 Usage

**1. Load data into the database**
```bash
python push_data.py
```

**2. Run the training pipeline**
```bash
python main.py
```

**3. Start the API server**
```bash
python app.py
```
Then open `http://localhost:8000/docs` for the interactive API docs.

### API Endpoints

| Method | Endpoint    | Description                                  |
|--------|-------------|----------------------------------------------|
| GET    | `/train`    | Triggers the full training pipeline          |
| POST   | `/predict`  | Upload a CSV file and get predictions back   |

---

## 📊 Model Performance

| Model               | F1 Score | Precision | Recall |
|---------------------|----------|-----------|--------|
| Random Forest       | TODO     | TODO      | TODO   |
| Gradient Boosting   | TODO     | TODO      | TODO   |
| Logistic Regression | TODO     | TODO      | TODO   |

**Best model:** TODO

---

## 🐳 Deployment

### Run with Docker
```bash
docker build -t networksecurity .
docker run -p 8000:8000 --env-file .env networksecurity
```

### CI/CD
<!-- TODO: describe your pipeline, e.g., GitHub Actions → AWS ECR → EC2 -->
On every push to `main`, GitHub Actions builds the Docker image, pushes it to a container registry, and deploys it to the cloud server.

---

## 🔮 Future Improvements
- Real-time traffic monitoring with streaming data
- Deep learning models for improved accuracy
- Dashboard for visualizing threats
- Automated retraining when data drift is detected

---

## 🤝 Contributing

Contributions are welcome!
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-profile](https://linkedin.com/in/your-profile)
- Email: your.email@example.com

⭐ If you found this project useful, please give it a star!
