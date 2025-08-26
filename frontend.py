# pip install streamlit
# pip install requests
import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Life Insurance Premium Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
annual_income = st.number_input("Annual Salary in SGD", min_value=0.1, value=10000.0)
smoker = st.selectbox("Do you smoke?", options=[True, False])
city = st.text_input("City", value="Sengkang")
residency_status = st.selectbox("Living Status", ['Citizen', 'PR', 'Foreigner'])
occupation = st.selectbox("Occupation", ['retired', 'business_owner', 'student', 'freelancer','government_job', 'private_job', 'unemployed'])

# Inject custom CSS for background page color, text color, button color
st.markdown("""
    <style>
    /* Background for entire app and top bar */
    html, body, .stApp {
        background-color: #0b3d0b !important;
        color: white !important;
    }

    header[data-testid="stHeader"] {
        background-color: #0b3d0b !important;
    }

    /* Input field background + text */
    .stTextInput > div > div > input,
    .stNumberInput input,
    .stSelectbox > div > div > div {
        background-color: #000066 !important;
        color: white !important;
    }

    /* Fix for input labels */
    label, .stMarkdown, .css-1cpxqw2, .css-1offfwp {
        color: white !important;
        font-weight: bold;
    }

    /* Predict button styling */
    div.stButton > button:first-child {
        background-color: #1E90FF;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px grey;
        transition: background-color 0.3s ease;
    }

    div.stButton > button:first-child:hover {
        background-color: #0066CC;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("Predict Your Premium"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "annual_income": annual_income,
        "smoker": smoker,
        "city": city,
        "residency_status": residency_status,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()
        if response.status_code == 200 and "predicted_category" in result:
            # st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
            st.markdown(f"""
                <div style='
                    background-color: #003366;
                    color: #00FF99;
                    padding: 20px;
                    border-radius: 12px;
                    font-size: 22px;
                    font-weight: bold;
                    text-align: center;
                    box-shadow: 0 0 10px rgba(0,255,153,0.7);
                    margin-top: 20px;
                '>
                    Predicted Insurance Premium Category: <br>
                    <span style='font-size: 20px;'>{result['predicted_category']}</span>
                </div>
            """, unsafe_allow_html=True)
        elif response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
            with st.expander("Response body"):
                st.write(result)   
        else:
            st.warning("API responded with 200 but missing 'predicted_category'.")
            with st.expander("Raw response"):
                st.write(result)          
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure its running.")






