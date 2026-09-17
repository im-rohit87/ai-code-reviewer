
import streamlit as st
from reviewer import review_code

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Reviewer")
st.markdown(
    "Paste your code below and let AI find bugs, security issues, "
    "style problems, and optimization opportunities."
)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "TypeScript",
            "C",
            "PHP",
            "SQL",
            "HTML",
            "CSS"
        ]
    )

    st.info(
        "The AI reviewer analyzes your code and provides "
        "suggestions and an improved version."
    )

# Code input
st.subheader("📝 Your Code")

default_code = """def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)
"""

code = st.text_area(
    "Paste your code here:",
    value=default_code,
    height=350,
    placeholder="Paste your code..."
)

# Review button
if st.button("🔍 Review Code", type="primary"):

    if not code.strip():
        st.warning("Please enter some code first.")
    else:

        with st.spinner("AI is reviewing your code..."):

            try:
                result = review_code(code, language)

                st.success("Code review completed!")

                st.divider()

                st.subheader("📊 AI Code Review")

                st.markdown(result)

            except Exception as e:
                st.error(f"Error: {str(e)}")