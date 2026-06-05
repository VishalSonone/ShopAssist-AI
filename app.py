import uuid
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Voice Bot",
    page_icon="🎙️",
    layout="wide"
)


st.title("🎙️ AI E-Commerce Customer Support Voice Bot")


status_col, control_col = st.columns([3, 1])
with status_col:
    st.markdown("---")
    st.markdown("### Conversation Status")
    st.info(st.session_state.conversation_status)
    st.write(f"**Session ID:** {st.session_state.session_id}")
    st.write(f"**Turns:** {st.session_state.turn_count}")