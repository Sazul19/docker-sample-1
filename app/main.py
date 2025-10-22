from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="Student Grade Predictor")

model = joblib.load("app/grade_model.pkl")

class StudyHours(BaseModel):
    hours: float

@app.get("/")
def home():
    return {"message": "Student Grade Predictor API"}

@app.post("/predict")
def predict(data: StudyHours):
    prediction = model.predict([[data.hours]])[0]
    return {"hours_studied": data.hours, "predicted_grade": round(prediction, 2)}
