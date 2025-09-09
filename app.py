import sys, os
import streamlit as st

# Add project folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "multi_agent_boardroom"))

from boardroom.meeting import BoardRoom

st.set_page_config(page_title="AI Startup Boardroom", layout="wide")

st.title("AI Boardroom Simulation")
st.write("Enter a startup idea and watch CEO, CTO, and CFO discuss it in real-time!")

topic = st.text_input(" Your Startup Idea", placeholder="e.g. AI-powered crop disease detection")
rounds = st.slider("Number of Discussion Rounds", 1, 5, 2)

if st.button("Run Boardroom"):
    if topic:
        board = BoardRoom(topic, rounds=rounds)
        with st.spinner("Agents are discussing..."):
            _, summary = board.run_meeting()

        # st.subheader("Boardroom Discussion")
        # for role, message in discussion:
        #     st.markdown(f"**{role}:** {message}")

        st.subheader(" Meeting Summary")
        st.markdown(summary)
    else:
        st.warning("Please enter a startup idea first!")
