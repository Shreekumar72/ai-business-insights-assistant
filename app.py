import streamlit as st
from ai_query_engine import get_business_insight
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

st.set_page_config(page_title="Business Insights Assistant", layout="centered")
st.title("📊 AI-Powered Business Insights Assistant")
st.markdown("Ask your strategic business questions and get structured, actionable insights.")

query = st.text_area("Enter your business question:")

def save_to_pdf(content):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp_file.name, pagesize=letter)
    width, height = letter

    y = height - 40
    for line in content.split('\n'):
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    return temp_file.name

if st.button("Generate Insight"):
    if query.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Generating insight..."):
            result = get_business_insight(query)

        st.success("Done!")
        st.markdown("### 🔍 AI Insight")
        st.markdown(result)

        pdf_path = save_to_pdf(result)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Download as PDF", f, file_name="insight.pdf", mime="application/pdf")
