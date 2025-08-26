# pip install pandas
# pip install -U pydantic
# pip install fastapi

from typing import Annotated, Literal
from fastapi.responses import JSONResponse
import pandas as pd
from fastapi import FastAPI
import pickle
from pydantic import BaseModel, Field, computed_field

# Import the model
with open('insurancemodel.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# Pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
    annual_income: Annotated[float, Field(..., gt=0, description='Annual salary of the user in SGD')]
    smoker: Annotated[bool, Field(..., description='Is user a smoker')]
    city: Annotated[str, Field(..., description='The city where the user is living')]
    residency_status: Annotated[Literal['Citizen', 'PR', 'Foreigner'], Field(..., description='Living status in Singapore')]
    occupation: Annotated[Literal['retired', 'business_owner', 'student', 'freelancer','government_job', 'private_job', 'unemployed'], Field(..., description='Occupatin of the user')]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high'
        elif self.smoker or self.bmi > 27:
            return 'medium'
        else:
            return 'low'
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
@app.post('/predict')
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city': data.city,
        'Annual_income': data.annual_income,
        'Residency_status': data.residency_status,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})

