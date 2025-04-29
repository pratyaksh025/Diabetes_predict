import streamlit as st
import joblib

model=joblib.load('diabetes.pkl')

def main():
    st.title("Diabities Predictive Model")
    glucose = st.number_input("Glucose", min_value=0, max_value=200, value=100)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
    age = st.number_input("Age", min_value=1, max_value=100, value=30)

    
    if st.button('Sumit'):
        result=model.predict([[glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        print(result)
        if result[0] == 1:
            st.success('You are diabetic')
        else:
            st.success('You are not diabetic')
        
    st.text("Developed by: Pratyaksh Yadav")



if __name__=="__main__":
    main()

