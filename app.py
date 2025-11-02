# This si the main file fo streamlit
import os
import streamlit as st
from src.core.planner import TravelPlanner 
from dotenv import load_dotenv
from src.utils.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(page_title="AI Travel Planner")
st.title("AI TRAVEL PLANNER")
st.write("Plan your day trip iternary by entring your city and intrests")
load_dotenv()
with st.form("travel_form"):
    city=st.text_input("Enter the city that you'll like to visit")
    intrests=st.text_input("Enter your intrests")
    submitted=st.form_submit_button("Generate Itenary")
    if submitted:
        if city and  intrests:
            # ensure GROQ API key is present before calling into the LLM code
            if not os.getenv("GROQ_API_KEY"):
                st.error(
                    "GROQ_API_KEY is not set. Add the key to your environment or Streamlit Secrets and restart the app."
                )
                st.stop()
            planner=TravelPlanner(city,intrests.split(","))
            planner.set_city(city)
            planner.set_intrests(intrests)
            try:
                itenary=planner.create_itenary()
                st.subheader("Generated Itenary")
                st.markdown(itenary)
            except Exception as e:
                # Log full traceback to file and show a friendly UI message
                logger.error("Error while generating itinerary", exc_info=True)
                st.error(
                    "An error occurred while generating the itinerary. The full details have been recorded to the application logs."
                )
        else:
            st.warning("Please enter both the city and instrests to move forward")

