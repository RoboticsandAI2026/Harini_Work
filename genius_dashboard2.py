import os
import streamlit as st
import importlib

# === Page Config ===
st.set_page_config(page_title="GENIUS Dashboard", layout="wide")

# === Title ===
st.markdown(
    "<h1 style='font-size: 40px;'>🤖 GENIUS – Generative AI-Enabled Neural Interface for Unified Systems</h1>",
    unsafe_allow_html=True,
)

# === Sidebar: Role Selection ===
st.sidebar.header("🧑‍🏫 Select Your Role")
role = st.sidebar.radio("Choose a role:", ["Student", "Professor", "GAN Lab"])

# === Student Features (Retained + New Added) ===
student_features = {
    "personalized_content": "📚 Personalized Content Recommendation",
    "smart_study_scheduler": "📅 Smart Study Scheduler (Advanced)",
    "ask_from_image_or_text": "🖼 Ask Questions from Image or Text",  # ✅ Newly added feature
    "concept_summarization": "🧠 Concept Summarization & Explanation",
    "performance_analytics": "📊 Performance Analytics & Reports",
    "adaptive_quiz": "🎯 Adaptive Quiz Generation",
    "voice_to_notes": "🎙 Voice-to-Notes Support",
    "language_translation": "🌐 Language Translation for Global Learners",
}

# === Professor Features (Retained) ===
professor_features = {
    "student_tracking": "📍 Student Progress Tracker",
    "visualize_gaps": "🔍 Visualize Class Learning Gaps",
    "schedule_optimization": "📆 Schedule Optimization",
    "voice_commands": "🗣 Voice Command Interface",
    "syllabus_generator": "📝 Syllabus Generator",
}

# === GAN Lab Features (UPDATED) ===
ganlab_features = {
    "ai_generated_experiments": "🧪 AI-Generated Lab Experiments / Scientific Simulations",
    "ai_explainability_visualization": "🤯 GAN for AI Explainability Visualization", 
    "real_vs_generated_comparator":"🆚 Real vs Generated Lab Image Comparator",
 # ✅ New
}

# === Feature Loader Function ===
def load_feature(module_key, role):
    try:
        feature_module = importlib.import_module(f"features.{role.lower()}.{module_key}")
        feature_module.run_feature()
    except Exception as e:
        st.error("🚧 Feature under construction or missing module.")
        st.exception(e)

# === Sidebar + Center Rendering ===
if role == "Student":
    st.sidebar.subheader("🎓 Student Tools")
    selected_feature = st.sidebar.selectbox("Choose a feature:", list(student_features.values()))
    module_key = [k for k, v in student_features.items() if v == selected_feature][0]

    st.header("🎓 Student Dashboard")
    load_feature(module_key, "student")

elif role == "Professor":
    st.sidebar.subheader("👨‍🏫 Professor Tools")
    selected_feature = st.sidebar.selectbox("Choose a feature:", list(professor_features.values()))
    module_key = [k for k, v in professor_features.items() if v == selected_feature][0]

    st.header("👨‍🏫 Professor Dashboard")
    load_feature(module_key, "professor")

elif role == "GAN Lab":
    st.sidebar.subheader("🎨 GENIUS GAN Lab Tools")
    selected_feature = st.sidebar.selectbox("Choose a GAN Lab feature:", list(ganlab_features.values()))
    module_key = [k for k, v in ganlab_features.items() if v == selected_feature][0]

    st.header("🎨 GENIUS GAN Lab Dashboard")
    load_feature(module_key, "ganlab")
