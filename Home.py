import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #0f0f0f, #111827, #0a0a0a)"
    accent = "#00f5ff"
else:
    bg = "linear-gradient(135deg, #e0eafc, #cfdef3)"
    accent = "#4a90e2"

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: white;
    font-family: 'Arial';
}}

.card {{
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    margin-bottom: 20px;
    transition: all 0.3s ease;
}}

.card:hover {{
    transform: translateY(-6px);
    box-shadow: 0px 12px 40px rgba(0,245,255,0.25);
    border: 1px solid {accent};
}}

h1 {{
    text-align: center;
    color: {accent};
    text-shadow: 0px 0px 15px {accent};
}}

h3 {{
    text-align: center;
    color: rgba(255,255,255,0.8);
}}

img {{
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    transition: 0.3s;
}}

img:hover {{
    transform: scale(1.03);
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h1>🌐 My Portfolio</h1>
<h3>💻 Aspiring Developer | 🚀 Creative Thinker</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
<div class="card">
<h2>👋 Hello, I'm Julius P. Carmen</h2>
<p>🎓 Computer Science student passionate about technology, design, and building meaningful digital solutions.</p>
<p>💡 I enjoy turning ideas into real systems, especially web applications and creative UI designs.</p>
<p>🚀 My goal is to grow as a developer and eventually build innovative projects that solve real-world problems.</p>
</div>
""", unsafe_allow_html=True)
    
with col2:
    st.image("pages/9a982bd3-dbba-4e0a-a286-7f74848efd01.jpg", width=260)

st.markdown("---")