import streamlit as st
import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key = API_KEY)

st.title("BMI Calculator with AI Nutritionist")

ht = st.slider("Enter your height in meters:",min_value = 1.0,max_value = 2.5, step = 0.01)
wt = st.slider("Enter your weight in kg:",min_value = 1.0,max_value = 300.0, step = 1.0)
gender = st.selectbox("select your gender:",["Male","Female"])

bmi = wt/(ht**2)
st.write(f"your bmi is:{bmi:.2f}")

prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, and BMI as         {bmi}"


if st.button("take AI opinion"):
       response = client.models.generate_content(model="gemini-3.5-flash", contents= prompt)
       st.write(response.text)