import streamlit as st


st.set_page_config(page_title="Data Portfolio Showcase", layout="wide")

st.title("Data Skills Vitrine")
st.caption("Always-on showcase optimized for a 2 vCPU / 4 GB VPS")

st.markdown(
    """
### How to read this showcase
- **Live Interactive**: endpoint is currently running.
- **Artifacts Interactive**: charts and outputs are precomputed.
- **Static Case Study**: architecture, trade-offs, and outcomes.
"""
)
