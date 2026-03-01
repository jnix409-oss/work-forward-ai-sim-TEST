import streamlit as st

st.title("Organizational Restructure Simulation")

managers = st.slider("Number of Managers", 3, 15, 10)
employees = st.slider("Number of Employees", 20, 200, 80)

if st.button("Run Simulation"):
    baseline, reorg = run_compare()
    
    st.write("Baseline Results", baseline)
    st.write("Reorg Results", reorg)

!streamlit run app.py
