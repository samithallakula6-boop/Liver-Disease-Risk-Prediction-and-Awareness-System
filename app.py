import streamlit as st
import pandas as pd
import joblib
best_rf = joblib.load("liver_disease_model.pkl")
st.set_page_config(
    page_title = "Liver Disease Risk Prediction and Awareness System",
    page_icon = "🩺",
    layout = "wide",
)
# Load external CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# Application Header
st.title("Liver Disease Risk Prediction and Awareness System")

st.subheader("Your Liver Health Matters")

st.write(
    "An ML-based application for liver disease risk "
    "prediction and personalized health awareness."
)

st.divider()

st.subheader(" Personal Information")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Enter your age:", min_value=0, max_value=100, value=45)
    BMI = st.number_input("Enter value of Bmi:", min_value=10.0, max_value=90.0, value=25.0)

with col2:
    Gender = st.selectbox("Enter your Gender:", ["male", "female"])

st.subheader(" Lifestyle Information")

col1, col2 = st.columns(2)

with col1:
    Smoking = st.selectbox("Do you smoke?", ["yes", "no"])
    AlcoholConsumption = st.number_input(
        "Alcohol consumption:", min_value=0.0, max_value=90.0,
        value=17.272828
    )

with col2:
    PhysicalActivity = st.number_input(
        "Physical activity:", min_value=0.0, max_value=10.0,
        value=0.658940
    )
    HeavyDrinker = st.selectbox("Are you a heavy drinker?", ["yes", "no"])
st.subheader("🩺 Health Information")


col1, col2 = st.columns(2)

with col1:
    GeneticRisk = st.selectbox(
        "Select your genetic risk level:", ["low", "medium", "high"]
    )
    Diabetes = st.selectbox("Do you have diabetes?", ["yes", "no"])

with col2:
    Hypertension = st.selectbox("Do you have hypertension?", ["yes", "no"])
    LiverFunctionTest = st.number_input(
        "Liver function test:", min_value=0.0, max_value=100.0,
        value=42.734240
    )


if Gender == "male":
    Gender_value = 0
else:
    Gender_value = 1

if Smoking == "yes":
    Smoking_value = 1
else:
    Smoking_value = 0

if GeneticRisk == "low":
    GeneticRisk_value = 0
elif GeneticRisk == "medium":
    GeneticRisk_value = 1
else:
    GeneticRisk_value = 2

if Diabetes == "yes":
    Diabetes_value = 1
else:
    Diabetes_value = 0

if Hypertension == "yes":
    Hypertension_value = 1
else:
    Hypertension_value = 0

if HeavyDrinker == "yes":
    HeavyDrinker_value = 1
else:
    HeavyDrinker_value = 0

new_patient = pd.DataFrame({
    "Age": [Age],
    "Gender": [Gender_value],
    "BMI": [BMI],
    "AlcoholConsumption": [AlcoholConsumption],
    "Smoking": [Smoking_value],
    "GeneticRisk": [GeneticRisk_value],
    "PhysicalActivity": [PhysicalActivity],
    "Diabetes": [Diabetes_value],
     "Hypertension": [Hypertension_value],
    "LiverFunctionTest": [LiverFunctionTest],
    "HeavyDrinker": [HeavyDrinker_value]
    
})


if st.button(" Predict Liver Disease Risk", use_container_width=True):

    prediction = best_rf.predict(new_patient)

    if prediction[0] == 1:

        st.error("Liver disease risk detected.")

        st.subheader("🩺 Personalized Liver Health Awareness")

        precautions = []

        if BMI >= 25:
            precautions.append(
                "⚖️ BMI: Your BMI is in a higher range. "
                "Maintaining a healthy weight may support liver health."
            )

        if AlcoholConsumption > 0:
            precautions.append(
                "🍺 Alcohol consumption: Alcohol can affect liver health. "
                "Avoid excessive alcohol consumption."
            )

        if HeavyDrinker_value == 1:
            precautions.append(
                "🍺 Heavy drinking: Heavy alcohol use can seriously affect "
                "liver health. Avoid heavy drinking."
            )

        if PhysicalActivity < 3:
            precautions.append(
                "🏃 Physical activity: Your entered activity level is relatively "
                "low. Gradually increase regular physical activity."
            )

        if Diabetes_value == 1:
            precautions.append(
                "🩸 Diabetes: Follow your healthcare professional's advice "
                "for managing diabetes."
            )

        if GeneticRisk in ["medium", "high"]:
            precautions.append(
                "🧬 Genetic/family risk: Discuss your family history and "
                "appropriate health monitoring with a healthcare professional."
            )

        with st.container(border=True):

            if len(precautions) > 0:

                st.subheader("⚠️ Factors Requiring Attention")

                for precaution in precautions:
                    st.warning(precaution)

            else:

                st.subheader("🩺 General Liver Health Information")

                st.info(
            "Continue maintaining a healthy lifestyle to support liver health. "
            "Avoid excessive alcohol consumption, maintain a healthy weight, "
            "and stay physically active."
        )
    else:
        st.success("No liver disease risk detected.")
        st.info(
            "Your inputs indicate a lower predicted risk. "
            "Continue maintaining a healthy lifestyle."
        )

# IMPORTANT DISCLAIMER 

    st.divider()
    with st.container(border=True):

                        st.subheader("⚠️ Medical Disclaimer")

                        st.write(
        "This application provides machine-learning-based "
        "risk predictions for awareness purposes only."
    )

                        st.warning(
        "The prediction is not a medical diagnosis and "
        "should not replace professional medical advice."
    )

                        st.info(
        "If you have symptoms or concerns about your liver health, "
        "consult a qualified healthcare professional."
    )
# APPLICATION FOOTER

st.divider()

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <p>🩺 Liver Disease Awareness System</p>
        <p>ML-Based Risk Prediction & Health Awareness</p>
        <p>Developed as an AI & ML Project</p>
    </div>
    """,
    unsafe_allow_html=True
)




