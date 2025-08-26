**InsureWise – ML-powered Insurance Premium Prediction**

**InsureWise** is an end-to-end machine learning application that predicts insurance premium categories based on user details such as Age, BMI, lifestyle, occupation, income, and Living Status in Singapore.

It provides:
- Backend: FastAPI serving the ML model
- Frontend: Streamlit interactive web app
- Model: Trained with insurance records (insurance_record.csv)
- Deployment-ready: Tested locally with Uvicorn + Streamlit

**Project Structure**
```
.
├── app.py                # FastAPI backend (prediction API)
├── frontend.py           # Streamlit frontend for user interaction
├── ml_model.ipynb        # Jupyter Notebook (EDA + model training)
├── insurancemodel.pkl    # Trained ML model (pickled)
├── insurance_record.csv  # Dataset used for training
├── requirement.txt       # Python dependencies
├── .gitignore            # Ignore unnecessary files in Git
```

**Running the Project**
1. Start the FastAPI backend
    uvicorn app:app --reload
    Open at: http://127.0.0.1:8000/predict
2. Launch the Streamlit frontend:
    streamlit run frontend.py
    Open at: http://localhost:8501

**Features**
- Auto-computes BMI, Age Group, Lifestyle Risk
- Predicts Insurance Premium Category instantly
- Modern Streamlit UI with styled results
- Clean FastAPI backend with Pydantic validation
- Easily extendable with more features/datasets

**Tech Stack**
- Python 3.12+
- FastAPI – backend API
- Streamlit – frontend UI
- scikit-learn – ML model training
- pandas – data processing
