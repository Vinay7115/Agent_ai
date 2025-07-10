import streamlit as st
from research.utils import fetch_insight

st.set_page_config(page_title="Agentic AI: Deep Research", layout="wide")
st.title("🔍 Agentic AI – Deep Company Research")
st.caption("Powered by Gemini DeepResearch API")

company = st.text_input("Enter a company name", placeholder="e.g., Tesla, Infosys, Google")

if company:
    st.header(f"📊 Research on {company}")
    with st.spinner("Researching via Gemini..."):
        for section in ["About", "News", "Financials", "Competitors", "Outlook"]:
            st.subheader(section)
            insight = fetch_insight(company, section)
            st.write(insight)
            st.markdown("---")
else:
    st.info("Please enter a company name to start.")
