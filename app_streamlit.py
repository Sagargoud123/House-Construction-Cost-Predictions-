import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🏠 House Cost Estimation - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "house1234":
            st.session_state.logged_in = True
            st.success("✅ Login successful! Redirecting...")
            st.rerun()  
        else:
            st.error("❌ Invalid Username or Password")

else:
    
    st.title("🏡 House Construction Cost Estimation")

    
    area = st.number_input("Area (sq. ft.)", min_value=100, step=50)
    labor = st.number_input("Labor Cost (₹)", min_value=1000, step=500)
    material = st.selectbox("Material Type", [0, 1])  # 0 = Normal, 1 = Premium
    pipes = st.number_input("Pipes (₹)", min_value=500, step=100)
    lights = st.number_input("Lights (₹)", min_value=500, step=100)
    fans = st.number_input("Fans (₹)", min_value=500, step=100)
    steel = st.number_input("Steel (₹)", min_value=1000, step=500)
    bricks = st.number_input("Bricks (₹)", min_value=1000, step=500)

    if st.button("Estimate Cost"):
        features = np.array([[area, labor, material, pipes, lights, fans, steel, bricks]])
        prediction = model.predict(features)[0]
        st.success(f"💰 Estimated Construction Cost: ₹{prediction:,.2f}")

        
        data = {
            "Labor": labor,
            "Pipes": pipes,
            "Lights": lights,
            "Fans": fans,
            "Steel": steel,
            "Bricks": bricks
        }

        fig1, ax1 = plt.subplots()
        ax1.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=90)
        ax1.axis("equal")
        st.pyplot(fig1)

        
        fig2, ax2 = plt.subplots()
        ax2.bar(data.keys(), data.values())
        plt.xticks(rotation=30)
        st.pyplot(fig2)

    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
