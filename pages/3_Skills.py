import streamlit as st

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef2f3, #d9e4f5);
    color: #1f2937;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    color: #0f172a;
    font-weight: 800;
    letter-spacing: 1px;
}

h3 {
    color: #2563eb;
    margin-top: 25px;
}

p {
    color: #374151;
    font-size: 15px;
}

.skill-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    border-left: 5px solid #3b82f6;
    transition: 0.25s ease;
}

.skill-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.12);
}

div[data-testid="stProgressBar"] > div > div > div {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    border-radius: 10px;
}

ul, li {
    color: #374151;
    line-height: 1.8;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)


st.title("🛠 Skills")

st.subheader("💻 Programming")
st.markdown('<div class="skill-card">Python</div>', unsafe_allow_html=True)
st.progress(80)

st.markdown('<div class="skill-card">JavaScript</div>', unsafe_allow_html=True)
st.progress(70)

st.markdown('<div class="skill-card">PHP</div>', unsafe_allow_html=True)
st.progress(75)

st.subheader("🎨 Design")
st.markdown('<div class="skill-card">Canva / UI Design</div>', unsafe_allow_html=True)
st.progress(85)

st.subheader("🧰 Tools")
st.markdown("""
<div class="skill-card">
<ul>
<li>GitHub</li>
<li>VS Code</li>
<li>Streamlit</li>
</ul>
</div>
""", unsafe_allow_html=True)