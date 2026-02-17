
import streamlit as st

st.title("Smart Timetable Assistant AI – Industry Edition")

st.subheader("AI Study Planner")
hours = st.number_input("Total Study Hours", min_value=1)
days = st.number_input("Days Left", min_value=1)

if st.button("Optimize Plan"):
    result = round(hours / days, 2)
    st.success(f"Recommended study time per day: {result} hours")
