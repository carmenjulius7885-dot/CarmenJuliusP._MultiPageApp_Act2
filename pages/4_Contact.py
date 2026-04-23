import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📞", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #9FCB98, #79AE6F);
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    color: #0f172a;
    font-weight: 800;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.12);
}

input, textarea {
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
}

div.stButton > button {
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 20px rgba(37,99,235,0.3);
}

.social {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06);
    border: 1px solid #e2e8f0;
    text-align: center;
}

.social p {
    color: #334155;
    margin: 8px 0;
}

hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


st.markdown("<h1>📞 Contact Me</h1>", unsafe_allow_html=True)

st.write("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📩 Send a Message")

    name = st.text_input("👤 Name")
    email = st.text_input("📧 Email")
    message = st.text_area("💬 Message")

    colA,= st.columns(1)

    with colA:
        if st.button("Send Message"):
            if name and email and message:
                st.success("Message sent successfully ✅")
            else:
                st.error("Please fill in all fields")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="social">
        <h3>🌐 Connect With Me</h3>
        <p>💻 GitHub</p>
        <p>📘 Facebook</p>
        <p>📧 Email</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
