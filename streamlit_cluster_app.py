import streamlit as st
import pandas as pd
import requests
import base64

st.title("Personality Cluster Predictor")

with st.form("input_form"):
    Time_spent_Alone = st.slider("Time Spent Alone (hours/day)", 0, 11, 5)
    Stage_fear = st.selectbox("Stage Fear", ["Yes", "No"])
    Social_event_attendance = st.slider("Social Event Attendance (0–10)", 0, 10, 5)
    Going_outside = st.slider("Frequency of Going Outside (0–7)", 0, 7, 3)
    Drained_after_socializing = st.selectbox("Drained After Socializing", ["Yes", "No"])
    Friends_circle_size = st.slider("Number of Close Friends", 0, 15, 5)
    Post_frequency = st.slider("Social Media Post Frequency (0–10)", 0, 10, 5)

    submit = st.form_submit_button("Predict Cluster")

if submit:
    input_data = {
        "Time_spent_Alone": Time_spent_Alone,
        "Stage_fear": Stage_fear,
        "Social_event_attendance": Social_event_attendance,
        "Going_outside": Going_outside,
        "Drained_after_socializing": Drained_after_socializing,
        "Friends_circle_size": Friends_circle_size,
        "Post_frequency": Post_frequency
    }

    response = requests.post("http://127.0.0.1:5000/predict-cluster", json=input_data)
    if response.status_code == 200:
        # After predicting clusters, map numeric labels to meaningful names:
        cluster_labels = {
            0: "Introverted profiles",
            1: "Ambivert profiles",
            2: "Extroverted profiles"
        }

        cluster = response.json()['cluster']
        label = cluster_labels[cluster]
        st.success(f"Predicted Personality Cluster: {label}")

# Export feature summary to CSV
# if st.button("Export Cluster Summary"):
#     summary = pd.read_csv("cluster_profiles.csv")
#     csv = summary.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="cluster_profiles.csv">Download Cluster Summary</a>'
#     st.markdown(href, unsafe_allow_html=True)