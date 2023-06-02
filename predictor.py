
import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='My App',
    layout='wide',
    page_icon=':rocket:',
)


st.markdown("<h1 style='text-align: center; color: red;'>Disease Predictor App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Enter Details Below</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
global location , character , nausea ,family_bg , tinnitus , vomit, vertigo, age

with col1:
    st.write('Select your Symptoms')
  
    l=st.multiselect('Symtoms',['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
       'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity',
       'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
       'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
       'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
       'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
        'malaise', 'blurred_and_distorted_vision','phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region',
       'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness',
       'cramps', 'bruising', 'obesity', 'swollen_legs',
       'puffy_face_and_eyes', 'enlarged_thyroid',
       'brittle_nails', 'swollen_extremeties', 'excessive_hunger',
       'extra_marital_contacts', 'drying_and_tingling_lips',
       'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body','belly_pain', 'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma',
       'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'painful_walking',
       'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
       'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails'])


    fever=st.multiselect('Fever',('High','Mild','low'))
    Urine=st.multiselect('Urine',('Spotting Urination','Yellow Urine','Dark Urine','foul_smell_of urine'))
    joint_pain=st.multiselect('Body Pain','pain_in_anal_region','neck_pain','knee_pain','hip_joint_pain','stiff_neck','muscle_pain','belly_pain')
    Phlegm=st.multiselect('Phlegm',('mucoid_sputum', 'rusty_sputum','blood_in_sputum'))
    # itching=st.checkbox('Itching')
    # skin_rash=st.checkbox('Skin Rashes')
    # sneezing=st.checkbox('Sneezing')
    # joint_pain=st.checkbox('Jointpain')
    # stomach_pain=st.checkbox('Stomach Pain')
    # acidity=st.checkbox('Acidity')
    # vomiting=st.checkbox('Vomiting')
    # fatigue=st.checkbox('Fatigue')
    # weight_gain=st.checkbox('Weight Gain')
    # anxiety=st.checkbox('Anxiety')
    # cold_hands_and_feets=st.checkbox('Cold Hands and Feets')
    # weight_loss=st.checkbox('Weight Loss')
    # patches_in_throat=st.checkbox('Patches in Throat')
    # irregular_sugar_level=st.checkbox('Irregular Sugar Level')
    # cough=st.checkbox('Cough')
    # # high_fever=st.checkbox('High Fever')
    # sunken_eyes=st.checkbox('Sunken Eyes')
    # breathlessness=st.checkbox('Breathlessness')
    # sweating=st.checkbox('Sweating')
    # dehydration=st.checkbox('Dehydration')
    # headache=st.checkbox('Headache')
    # yellowish_skin=st.checkbox('Yellowish Skin')
    # nausea=st.checkbox('Nausea')
    # abdominal_pain=st.checkbox('Abdominal Pain')
    # diarrhoea=st.checkbox('Diarrhoea')
    # blurred_and_distorted_visions=st.checkbox('Blurred and Distorted Vission')












# try:
#     df = np.array(
#     [
#         age,
#         duration,
#         frequency,
#         location,
#         character,
#         intensity,
#         nausea,
#         vomit,
#         vertigo,
#         tinnitus,
#         family_bg,
#     ]
#     )

#     with open(r"final.pkl", "rb") as f:
#         model = pickle.load(f)

#     pred = model.predict(df.reshape(1, -1))
#     if pred == 0:
#         st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE SPORADIC HEMIPLEGIC MIGRAINE</h2>", unsafe_allow_html=True)
      
#     elif pred == 1:
#         st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE TYPICAL AURA WITHOUT MIGRAINE</h2>", unsafe_allow_html=True)
       
#     elif pred == 2:
#         st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE  MIGRAINE WITHOUT AURA</h2>", unsafe_allow_html=True)
        
#     elif pred == 3:
#         st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE BASILAR TYPE AURA MIGRAINE</h2>", unsafe_allow_html=True)
       
#     elif pred == 4:
#         st.markdown("<h2 style='text-align: center; color: green;'>You have some other type of migraine, please go to an actual medical professional.</h2>", unsafe_allow_html=True)

#     elif pred == 5:
#         st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE TYPICAL AURA WITH MIGRAINE</h2>", unsafe_allow_html=True)
        
#     elif pred == 6:
#         st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE FAMILIAL HEMIPLEGIC MIGRAINE</h2>", unsafe_allow_html=True)


# except ValueError:
#     st.error("Please enter a valid age")


