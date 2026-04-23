import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👩‍💻", layout="wide")

import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #111827, #1e293b);
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    color: #e2e8f0;
    font-weight: 800;
    letter-spacing: 1px;
    text-shadow: 0px 0px 15px rgba(59,130,246,0.3);
}

.card {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 18px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
    border: 1px solid rgba(255,255,255,0.1);
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(59,130,246,0.25);
    border: 1px solid rgba(59,130,246,0.4);
}

.card h3 {
    color: #60a5fa;
    margin-bottom: 12px;
    font-weight: 600;
}

.card p {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.7;
}

.quote {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    font-style: italic;
    color: #94a3b8;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 20px;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

st.title("👩‍💻 About Me")

st.markdown("""
<div class="card">
    <h3>✨ Who Am I?</h3>
    <p>
        I am a dedicated Computer Science student at DEBESMSCAT with a strong passion for technology, creativity, and innovation.  
        I enjoy learning new programming skills, designing user-friendly systems, and building projects that solve real problems.
    </p>
    <p>
        Outside academics, I am also exploring entrepreneurship through my small business journey, while continuously improving myself in both personal and professional growth.
    </p>
    <p>
        I believe in building a balanced life—where ambition, peace, and purpose work together to shape a meaningful future.
    </p>
</div>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🎓 Education</h3>
        <p>📘 Bachelor of Science in Computer Science</p>
        <p>💡 Continuously learning programming, UI design, and system development</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎯 Goals</h3>
        <p>✔ Become financially successful</p>
        <p>✔ Build a peaceful and stable future</p>
        <p>✔ Travel and live a life full of purpose</p>
    </div>
    """, unsafe_allow_html=True)
