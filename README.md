# 🏥 Insurance Prediction API (FastAPI)

This project is a **Machine Learning API** built using **FastAPI** that predicts medical insurance charges based on user input.

---

## 🚀 Features

* Predict insurance charges using a trained ML model
* Built with FastAPI (high-performance API framework)
* Uses Label Encoding for categorical variables
* Interactive API docs with Swagger UI
* Easy to deploy and extend

---

## 📂 Project Structure

```
├── main.py              # FastAPI application
├── format.py            # Pydantic schema
├── insurance.ipynb      # Model training notebook
├── model.pkl            # Trained ML model
├── le_sex.pkl           # Label encoder (sex)
├── le_region.pkl        # Label encoder (region)
├── le_smoker.pkl        # Label encoder (smoker)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

---

### 3️⃣ Activate Environment

#### Windows:

```
venv\Scripts\activate
```

#### Mac/Linux:

```
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### 🔹 Home

```
GET /
```

Response:

```
Welcome to the Insurance API
```

---

### 🔹 Predict Insurance Charges

```
POST /predict
```

#### Request Body:

```json
{
  "age": 19,
  "sex": "female",
  "bmi": 27.9,
  "children": 0,
  "smoker": "no",
  "region": "southwest"
}
```

#### Response:

```json
{
  "predicted_insurance_charge": 1737.376
}
```

---

## 📊 Model Details

* Algorithm: Decision Tree Regressor
* Input Features:

  * age
  * sex
  * bmi
  * children
  * smoker
  * region

---

## ⚠️ Important Notes

* Input values must match training data categories

* Example:

  * sex → male / female
  * smoker → yes / no
  * region → southeast / southwest / northeast / northwest

* If unknown values are passed, the API may throw an error

---

## 🔧 Future Improvements

* Add input validation for categories
* Use OneHotEncoder instead of LabelEncoder
* Add logging and error handling
* Deploy on cloud (AWS / Azure / Render)
* Add frontend UI

---

## 🧪 Testing

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Requirements Example

```
fastapi
uvicorn
scikit-learn
pydantic
numpy
pandas
```

---

## 👨‍💻 Author

Amritha T

---

## 📜 License

This project is open-source and free to use.


