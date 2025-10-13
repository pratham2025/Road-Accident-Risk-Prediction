# app.py

import streamlit as st
import pandas as pd
import random
from time import sleep

PAGE_TITLE = "Safer Road Challenge"
RISK_COLUMN_NAME = "accident_risk"

st.set_page_config(page_title=PAGE_TITLE, layout="wide")

def initialize_game():
    if 'game_initialized' not in st.session_state:
        st.session_state.game_initialized = True
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.road_one_details = None
        st.session_state.road_two_details = None
        st.session_state.feedback_message = ""
        st.session_state.answer_submitted = False
        st.session_state.road_data = None

@st.cache_data
def load_road_data(uploaded_file):
    try:
        data = pd.read_csv(uploaded_file)
        data.columns = data.columns.str.strip().str.lower()
        
        if RISK_COLUMN_NAME not in data.columns:
            st.error(f"Fatal Error: The CSV must contain a column named '{RISK_COLUMN_NAME}'.")
            return None
        return data
    except Exception as e:
        st.error(f"Oops! There was a problem reading the file: {e}")
        return None

def select_new_pair():
    if st.session_state.road_data is not None:
        if len(st.session_state.road_data) > 1:
            pair_indices = random.sample(range(len(st.session_state.road_data)), 2)
            st.session_state.road_one_details = st.session_state.road_data.iloc[pair_indices[0]]
            st.session_state.road_two_details = st.session_state.road_data.iloc[pair_indices[1]]
            st.session_state.answer_submitted = False
            st.session_state.feedback_message = ""
        else:
            st.warning("Not enough data. The CSV needs at least two rows to compare.")

def check_answer(user_choice):
    st.session_state.total_questions += 1
    st.session_state.answer_submitted = True

    road1 = st.session_state.road_one_details
    road2 = st.session_state.road_two_details

    safer_road_num = 1 if road1[RISK_COLUMN_NAME] <= road2[RISK_COLUMN_NAME] else 2

    if user_choice == safer_road_num:
        st.session_state.score += 1
        st.session_state.feedback_message = f"✅ Correct! Road {safer_road_num} was indeed the safer option."
    else:
        st.session_state.feedback_message = (
            f"❌ Not quite. Road {safer_road_num} was the safer choice. "
            f"(Risk for Road 1: {road1[RISK_COLUMN_NAME]:.2f}, Risk for Road 2: {road2[RISK_COLUMN_NAME]:.2f})"
        )

def display_road_card(column, road_attributes, road_number):
    with column:
        st.subheader(f"🛣️ Road {road_number}")
        st.write(f"**Road Type:** {road_attributes.get('road_type', 'N/A')}")
        st.write(f"**Lanes:** {int(road_attributes.get('num_lanes', 0))}")
        st.write(f"**Speed Limit:** {int(road_attributes.get('speed_limit', 0))} km/h")
        st.write(f"**Lighting:** {str(road_attributes.get('lighting', 'N/A')).capitalize()}")
        st.write(f"**Weather:** {str(road_attributes.get('weather', 'N/A')).capitalize()}")

initialize_game()

st.title("🚦 Safer Road Challenge")
st.markdown("""
Welcome to the game! Your mission, should you choose to accept it, is to test your intuition against real-world data.

Pick the road you think is **safer**. Let's see how you do!
""")
st.divider()

if st.session_state.road_data is None:
    st.session_state.road_data = load_road_data("/workspaces/Road-Accident-Risk-Prediction/train.csv")

if st.session_state.road_data is not None:
    st.header("Your Score")
    score_col, total_col = st.columns(2)
    score_col.metric("Correct Answers", st.session_state.score)
    total_col.metric("Total Rounds Played", st.session_state.total_questions)
    st.divider()

    if st.session_state.road_one_details is None:
        select_new_pair()

    road1, road2 = st.session_state.road_one_details, st.session_state.road_two_details

    left_col, right_col = st.columns(2)
    if road1 is not None and road2 is not None:
        display_road_card(left_col, road1, 1)
        display_road_card(right_col, road2, 2)

    st.write("")

    if not st.session_state.answer_submitted:
        b1, b2 = st.columns(2)
        if b1.button("🚗 Road 1 is Safer", use_container_width=True, key="road1_button"):
            check_answer(1)
            st.rerun()

        if b2.button("🚙 Road 2 is Safer", use_container_width=True, key="road2_button"):
            check_answer(2)
            st.rerun()
    else:
        if "✅" in st.session_state.feedback_message:
            st.success(st.session_state.feedback_message)
        else:
            st.error(st.session_state.feedback_message)

        sleep(0.4)

        if st.button("➡️ Play Next Round", use_container_width=True, type="primary"):
            select_new_pair()
            st.rerun()