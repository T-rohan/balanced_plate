import os, streamlit as st
import google.generativeai as genai
Secret_Key = st.secrets["Secret_Key"]
genai.configure(api_key=Secret_Key)
model = genai.GenerativeModel('gemini-2.5-flash')

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #3CA55C, #B5AC49);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.markdown(
#     "<h2 style='color: #F5F5F5; text-align: center; font-weight: bold;margin-top: 0.0em;'>Balanced Plate</h2>",
#     unsafe_allow_html=True
# )
# st.markdown(
#     "<div style='font-size:16px; color: #F5F5F5; text-align: center; font-weight: 600;margin-bottom:3.0em;'>"
#     "Fuel your goals with the right nutrition"
#     "</div>",
#     unsafe_allow_html=True
# )
st.markdown("""
    <h1 style='text-align: center; color: white; font-size: 32px; margin-top: -1.0em;'>
    Balanced Plate
    </h1>
    <div style='text-align: center; color: white; font-size: 19px; font-weight: 600; margin-bottom: 3.0em;margin-top:-0.5em'>
        Fuel your goals with right nutrition
    </div>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Enter your age:</label>
    """,
    unsafe_allow_html=True)
age = st.number_input('Enter your age: ',min_value=0.0,label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Please select your gender:</label>
    """,
    unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Target radio button labels */
    div[role="radiogroup"] label {
        color: #F5F5F5 !important;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)
gender = st.radio('Please select your gender:',["👨 Male", "👩 Female", "⚧️ Other"],label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Enter your current weight (kg):</label>
    """,
    unsafe_allow_html=True)
weight = st.slider('Enter your current weight(kg): ',label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Enter your goal:</label>
    """,
    unsafe_allow_html=True)
goal = st.text_input('Enter your goal: ',placeholder = 'e.g. Loose weight, Gain weight, Muscle building',label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Preferred diet:</label>
    """,
    unsafe_allow_html=True)
diet = st.multiselect('Diet: ',['Vegetarian','Vegan','Non-vegetarian'],label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Allergies if any(optional):</label>
    """,
    unsafe_allow_html=True)
allergy = st.text_input(
    label = 'Allergies if any(optional): ',label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">How many meals are preferable per day:</label>
    """,
    unsafe_allow_html=True)
frequency = st.number_input('How many meals are preferable per day: ',min_value=0.0,label_visibility="collapsed")
st.markdown(
    """
    <style>
    .custom-label {
        color: #F5F5F5;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    <label class="custom-label">Enter the plan duration in days:</label>
    """,
    unsafe_allow_html=True)
duration = st.number_input('Enter the plan duration in days: ',min_value=0,label_visibility="collapsed")

if st.button('Plan my diet'):
    ask = (f'Generate a {duration} day {diet} diet plan for a {age} year old {gender}, weighing {weight} kgs, who wants to {goal}. He is allergic to {allergy}. Suggest a {frequency} meal per day option with portion sizes.')
    response = model.generate_content(ask)
    st.write(response.text)
