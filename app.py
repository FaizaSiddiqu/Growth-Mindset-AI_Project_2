import streamlit as st

# Set page configuration
st.set_page_config(page_title='🌷 Growth Mindset AI', page_icon='🌸', layout='centered', initial_sidebar_state='auto')

# Title
st.title("Growth Mindset Challenge: Web App with Streamlit")

# Header and welcome message
st.header("🌱 Welcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you develop a growth mindset and achieve your goals.")

# Quote section
st.header('🌺 Inspirational Quote')
st.write("“The only limit to our realization of tomorrow will be our doubts of today.” - Franklin D. Roosevelt")

# Take user input
st.header("What's your challenge today?")
user_input = st.text_input("Describe a challenge you are facing:")

# Condition
if user_input:
    st.success(f"You are facing: {user_input}, keep pushing forward toward your goals! 🌟")
else:
    st.warning("Tell us about your challenge today!")

# Reflecting
st.header("Reflect on your journey")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"🌟 Great! Your {reflection} on your journey to grow and learn.")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievement
st.header("❤️ Celebrate your Achievement")
achievement = st.text_input("Share an achievement you have recently accomplished:")

if achievement:
    st.success(f"🎉 Congratulations on your achievement: {achievement}")
else:
    st.info("Big or small, achievements are worth celebrating! Share your win today. 😊")

# Footer
st.write("- - -")
st.write("Keep believing in yourself and never give up! 🌷")
st.write("**© This app is created by Faiza Siddiqui**")