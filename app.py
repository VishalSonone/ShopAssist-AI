import uuid
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Voice Bot",
    page_icon="🎙️",
    layout="wide"
)


st.title("🎙️ AI E-Commerce Customer Support Voice Bot")

def initialize_session_state():
    st.session_state.turn_count = 0
    st.session_state.session_id = str(uuid.uuid4())[:8]
    st.session_state.conversation_status = ""
    
    
def reset_conversation():
    st.session_state.turn_count = 0
    
    
initialize_session_state()
status_col, control_col = st.columns([3, 1])
with status_col:
    st.markdown("---")
    st.markdown("### Conversation Status")
    st.info(st.session_state.conversation_status)
    st.write(f"**Session ID:** {st.session_state.session_id}")
    st.write(f"**Turns:** {st.session_state.turn_count}")
    
    
with control_col:
    if st.button("Start New Conversation", key="new_conversation"):
        reset_conversation()
        st.experimental_rerun()
        
st.markdown("---")

left_col, right_col = st.columns([3, 1])

with left_col:
    st.subheader("🛒 Ecommerce Voice Chat")
    st.write("Ask ecommerce questions, and the bot will reply with text and voice.")

    suggested_questions = [
        "What is your return policy?",
        "How long does shipping take?",
        "Can I cancel my order?",
        "Do you ship internationally?",
        "What payment methods do you accept?",
        "How do I track my package?"
    ]
    
