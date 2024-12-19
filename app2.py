import os
import streamlit as st
import numpy as np
from dotenv import load_dotenv
import joblib

# Load environment variables from env.txt
load_dotenv('env.txt')
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please set it in your env.txt file.")

# Load the pre-trained bowling score prediction model
model = joblib.load('best_model (8).pkl')  # Ensure the correct model file is used

def predict_and_suggest_adjustments(speed, angle, score, model):
    """Use a trained model to predict and suggest adjustments to improve bowling score."""
    current_prediction = model.predict([[speed, angle]])[0]

    if current_prediction >= score:
        return "Your predicted performance already matches or exceeds your last score! Keep it up!"

    # Generate small adjustments
    adjustments = []
    for delta_speed in [-1, 0, 1]:
        for delta_angle in np.linspace(-2, 2, 10):  # Allow larger angle adjustments
            new_speed = max(1, min(3, speed + delta_speed))
            new_angle = max(30, min(60, angle + delta_angle))
            new_prediction = model.predict([[new_speed, new_angle]])[0]

            # Log adjustments for debugging
            print(f"Speed: {new_speed}, Angle: {new_angle}, Prediction: {new_prediction}")

            if new_prediction > current_prediction:
                adjustments.append((new_speed, new_angle, new_prediction))

    # Sort adjustments by predicted score (descending), then by minimal change in inputs
    adjustments.sort(key=lambda x: (-x[2], abs(x[0] - speed) + abs(x[1] - angle)))

    if adjustments:
        best_adjustment = adjustments[0]
        return f"Try adjusting your speed to {int(best_adjustment[0])} (1=Slow, 2=Medium, 3=Fast) and your angle to {best_adjustment[1]:.2f}. Predicted score: {best_adjustment[2]:.2f}"
    else:
        return "No significant improvements found with small adjustments. Try experimenting with bigger changes."

# Streamlit App
def main():
    st.title("Bowling Advice Chatbot")

    # Adding background image for the whole app
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('./images/bowlingpin.webp');
            background-size: cover;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Input your bowling performance")

    # User inputs
    avg_speed = st.selectbox("Average Throw Speed", options=[1, 2, 3], format_func=lambda x: {1: "Slow", 2: "Medium", 3: "Fast"}[x])
    avg_angle = st.number_input("Average Throw Angle (degrees)", min_value=30.0, max_value=60.0, value=45.0, step=0.5)
    last_score = st.number_input("Last Round Score", min_value=0, max_value=10, value=5, step=1)

    if st.button("Get Advice"):
        advice = predict_and_suggest_adjustments(avg_speed, avg_angle, last_score, model)
        st.subheader("Advice to Improve:")
        st.write(advice)

if __name__ == "__main__":
    main()
