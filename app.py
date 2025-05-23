import streamlit as st
import PyPDF2

# ------------------------
# 🔮 Fake AI Response Logic
# ------------------------

def fake_ai_response(prompt):
    if not prompt.strip():
        return "⚠️ Please enter a valid medical query."
    if "headache" in prompt.lower():
        return "🤖 Hmm, headaches can be caused by stress, dehydration, or even screen time overload. Stay hydrated!"
    elif "fever" in prompt.lower():
        return "🤖 Fever detected. Take rest, drink fluids, and keep an eye on your temperature!"
    else:
        return "🤖 Thanks for your input. Based on your message, I suggest keeping an eye on your symptoms or visiting a doc."

# ------------------------
# 📄 PDF Text Extractor
# ------------------------

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip() or "❌ Could not extract text from this PDF. Try another file."

# ------------------------
# 🚀 Streamlit App Starts Here
# ------------------------

st.set_page_config(page_title="MediAgent Lite", page_icon="🩺")
st.title("🩺 MediAgent Lite")
st.subheader("Your local, AI-inspired health assistant")

st.markdown("---")

# ------------------------
# 📄 PDF Upload Section
# ------------------------

st.header("📄 Upload a Medical Report (PDF)")

pdf_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if pdf_file:
    with st.spinner("Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(pdf_file)
        st.success("✅ Text extracted successfully!")
        st.text_area("📋 Extracted Text:", value=extracted_text, height=300)

st.markdown("---")

# ------------------------
# ✍️ Manual Text Input
# ------------------------

st.header("📝 Describe Symptoms or Ask a Question")

user_input = st.text_area("Type your medical concern here:", placeholder="e.g. I've had a fever and body pain for 2 days...")

if st.button("Get MediAgent's Advice"):
    response = fake_ai_response(user_input)
    st.markdown("#### 🤖 MediAgent says:")
    st.write(response)

