# frontend/app.py

import streamlit as st
import requests

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AI Career Readiness Agent",
    page_icon="🎯",
    layout="centered"
)

# -------------------------
# Header
# -------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>🎯 AI Career Readiness & Skill Gap Agent</h1>
    <p style='text-align: center; color: gray;'>
    Analyze your employability readiness for a target job role
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -------------------------
# Inputs Section
# -------------------------
st.subheader("📄 Resume Input")

resume_text = st.text_area(
    "Paste your resume text",
    height=180,
    placeholder="e.g. I know Python, ML, SQL, Git..."
)

target_role = st.selectbox(
    "🎯 Select Target Job Role",
    ["data_scientist", "backend_developer", "frontend_developer"]
)

st.divider()

# -------------------------
# Analyze Button
# -------------------------
analyze_clicked = st.button("🚀 Analyze Career Readiness", use_container_width=True)

# -------------------------
# API Call & Results
# -------------------------
if analyze_clicked:
    if not resume_text.strip():
        st.warning("⚠️ Please enter resume text before analyzing.")
    else:
        with st.spinner("Analyzing skills and readiness..."):
            response = requests.post(
                "http://127.0.0.1:8001/analyze-career",
                json={
                    "resume_text": resume_text,
                    "target_role": target_role
                }
            )

        if response.status_code == 200:
            data = response.json()

            st.success("✅ Analysis Complete")

            # -------------------------
            # Readiness Score (Hero Metric)
            # -------------------------
            st.markdown("## 📊 Career Readiness Score")
            st.metric(
                label="Overall Readiness",
                value=f"{data['readiness_score']} / 100"
            )

            st.divider()

            # -------------------------
            # Skills Breakdown
            # -------------------------
            st.markdown("## 🧠 Skill Breakdown")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Existing Skills")
                if data["existing_skills"]:
                    for skill in data["existing_skills"]:
                        st.markdown(f"- **{skill.title()}**")
                else:
                    st.markdown("_No matching skills found_")

            with col2:
                st.markdown("### ❌ Missing Skills")
                if data["missing_skills"]:
                    for skill in data["missing_skills"]:
                        st.markdown(f"- **{skill.title()}**")
                else:
                    st.markdown("_No missing skills_")

            st.divider()

            # -------------------------
            # Learning Roadmap
            # -------------------------
            st.markdown("## 🗺️ Personalized Learning Roadmap")

            for skill, info in data["learning_roadmap"].items():
                with st.container():
                    st.markdown(
                        f"""
                        <div style="
                            border: 1px solid #e6e6e6;
                            border-radius: 10px;
                            padding: 15px;
                            margin-bottom: 15px;
                        ">
                            <h4>📌 {skill.title()}</h4>
                            <p><b>Priority:</b> {info['priority'].replace('_', ' ').title()}</p>
                            <p><b>Beginner:</b> {info['beginner_weeks']} weeks</p>
                            <p><b>Intermediate:</b> {info['intermediate_weeks']} weeks</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:
            st.error("❌ Backend not reachable. Please ensure the API is running.")
