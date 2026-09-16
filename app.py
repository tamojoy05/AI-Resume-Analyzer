import streamlit as st

from resume_parser import extract_text
from skill_extractor import (
    extract_skills,
    compare_skills,
    extract_keywords,
    compare_keywords
)
from job_matcher import calculate_similarity
from resume_info_extractor import extract_resume_info
from recommendations import generate_recommendations


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.markdown(
    """
    ### Analyze your resume against a job description
    Get insights into your skills, job match, experience, projects,
    certifications, and areas for improvement.
    """
)

st.divider()


# =============================
# Input Section
# =============================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📄 Resume")

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"]
    )

with col2:

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste the Job Description",
        height=180,
        placeholder="Paste the job description here..."
    )


# =============================
# Analyze Button
# =============================

st.divider()

analyze_button = st.button(
    "🔍 Analyze Resume",
    type="primary",
    use_container_width=True
)

if analyze_button:

    if uploaded_file is None:

        st.warning("Please upload a resume first.")

    elif not job_description.strip():

        st.warning("Please enter a job description.")

    else:

        # =============================
        # Extract Resume Text
        # =============================

        resume_text = extract_text(uploaded_file)

        # =============================
        # Extract Resume Information
        # =============================

        resume_info = extract_resume_info(resume_text)

        # =============================
        # Extract Skills
        # =============================

        skills = extract_skills(resume_text)

        # =============================
        # Compare Skills
        # =============================

        matching_skills, missing_skills = compare_skills(
            resume_text,
            job_description
        )
        
        matching_keywords, missing_keywords, keyword_match_score = compare_keywords(
            resume_text,
            job_description
        )

        # =============================
        # Skill Match Score
        # =============================

        job_skill_count = (
            len(matching_skills) +
            len(missing_skills)
        )

        if job_skill_count > 0:

            skill_match_score = round(
                (len(matching_skills) / job_skill_count) * 100,
                2
            )

        else:

            skill_match_score = 0

        # =============================
        # AI Semantic Match
        # =============================

        match_score = calculate_similarity(
            resume_text,
            job_description
        )
        
        overall_match_score = round(
            (match_score * 0.60) +
            (skill_match_score * 0.40),
            2
        )
        
        # =============================
        # Generate Recommendations
        # =============================

        recommendations = generate_recommendations(
            resume_text,
            job_description,
            matching_skills,
            missing_skills,
            resume_info
        )

        # =============================
        # Success
        # =============================

        st.success(
            "Resume analyzed successfully!"
        )
        
        # =============================
        # Analysis Summary
        # =============================

        st.subheader("📌 Analysis Summary")

        st.write(
            f"Your resume has a **{match_score}% semantic match** "
            f"with the provided job description and a "
            f"**{skill_match_score}% skill match**."
        )

        st.write(
            f"**{len(skills)} skills** were detected in your resume, "
            f"with **{len(matching_skills)} matching skills** and "
            f"**{len(missing_skills)} missing job-relevant skills**."
        )
        
        
        
        # =============================
        # Candidate Information
        # =============================


        # =============================
        # Resume Quality Calculation
        # =============================

        quality_checks = {
            "Professional Email": resume_info["email"] != "Not found",
            "Phone Number": resume_info["phone"] != "Not found",
            "Education Section": bool(resume_info["education"]),
            "Projects Section": bool(resume_info["projects"]),
            "Experience Section": bool(resume_info["experience"]),
            "Certifications Section": bool(resume_info["certifications"]),
            "Skills Detected": len(skills) > 0
        }

        quality_score = round(
            (sum(quality_checks.values()) / len(quality_checks)) * 100,
            2
        )



        # =============================
        # Analysis Tabs
        # =============================

        tab1, tab2, tab3 = st.tabs(
            [
                "📊 Overview",
                "🛠️ Skills",
                "📄 Resume Details"
            ]
        )


        # =============================
        # Overview Tab
        # =============================

        with tab1:

            st.subheader("📌 Analysis Summary")

            st.write(
                f"Your resume has a **{match_score}% semantic match** "
                f"with the provided job description and a "
                f"**{skill_match_score}% skill match**."
            )

            st.write(
                f"**{len(skills)} skills** were detected in your resume, "
                f"with **{len(matching_skills)} matching skills** and "
                f"**{len(missing_skills)} missing job-relevant skills**."
            )

            # =============================
            # Scores
            # =============================
        st.subheader("📊 Resume Analysis Score")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🎯 Overall Match",
                f"{overall_match_score:.2f}%"
            )

        with col2:
            st.metric(
                "🤖 AI Semantic Match",
                f"{match_score:.2f}%"
            )

        with col3:
            st.metric(
                "🛠️ Skill Match",
                f"{skill_match_score:.2f}%"
            )

        with col4:
            st.metric(
                "📚 Skills Detected",
                len(skills)
            )


        st.progress(
            min(skill_match_score / 100, 1.0)
        )
        
        
        
        


        if match_score >= 75:

            st.success(
                "🎯 Strong semantic match between the resume "
                "and job description."
            )

        elif match_score >= 50:

            st.info(
                "📌 Moderate semantic match. Consider tailoring "
                "the resume more closely to the job description."
            )

        else:

            st.warning(
                "⚠️ Low semantic match. Consider adding relevant "
                "experience, projects, and skills if they accurately "
                "reflect your background."
            )
            
        
        st.subheader("🎯 Overall Match")

        st.progress(
            min(overall_match_score / 100, 1.0)
        )

        if overall_match_score >= 75:

            st.success(
                "🎯 Strong overall match with the job description."
            )

        elif overall_match_score >= 50:

            st.info(
                "📌 Moderate overall match. Consider tailoring "
                "your resume to the job description."
            )

        else:

            st.warning(
                "⚠️ Several areas could be improved to better "
                "align your resume with this job."
            )
        


        # =============================
        # Resume Quality
        # =============================

        st.subheader("✅ Resume Quality Checks")

        for check, status in quality_checks.items():

            if status:
                st.markdown(
                    f"✅ {check}"
                )
            else:
                st.markdown(
                    f"❌ {check}"
                )

        st.metric(
            "📈 Resume Quality Score",
            f"{quality_score:.2f}%"
        )

        st.progress(
            quality_score / 100
        )


        # =============================
        # Recommendations
        # =============================

        st.subheader(
            "💡 Resume Improvement Suggestions"
        )

        for recommendation in recommendations:

            st.markdown(
                f"💡 {recommendation}"
            )


        # =============================
        # Skills Tab
        # =============================

        with tab2:

            st.subheader("🛠️ Skill Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(
                    "### ✅ Matching Skills"
                )

                if matching_skills:

                    st.write(
                        " • ".join(
                            skill.title()
                            for skill in matching_skills
                        )
                    )

                else:

                    st.info(
                        "No matching skills found."
                    )

            with col2:

                st.markdown(
                    "### ❌ Missing Skills"
                )

                if missing_skills:

                    st.write(
                        " • ".join(
                            skill.title()
                            for skill in missing_skills
                        )
                    )

                else:

                    st.success(
                        "No missing skills detected!"
                    )

            st.subheader(
                "📚 All Detected Resume Skills"
            )

            if skills:

                st.write(
                    f"**{len(skills)} skills detected**"
                )

                st.write(
                    " • ".join(
                        skill.title()
                        for skill in skills
                    )
                )

            else:

                st.warning(
                    "No known skills detected."
                )
            
            
            st.divider()

            st.subheader("🔑 ATS Keyword Analysis")

            st.metric(
                "📊 Keyword Match",
                f"{keyword_match_score:.2f}%"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Matching Keywords")

                if matching_keywords:
                    st.write(
                        " • ".join(
                            keyword.title()
                            for keyword in matching_keywords
                        )
                    )
                else:
                    st.info("No matching keywords found.")

            with col2:
                st.markdown("### ❌ Missing Keywords")

                if missing_keywords:
                    st.write(
                        " • ".join(
                            keyword.title()
                            for keyword in missing_keywords
                        )
                    )
                else:
                    st.success("No missing keywords detected!")


        # =============================
        # Resume Details Tab
        # =============================

        with tab3:

            # =============================
            # Candidate Information
            # =============================

            st.subheader(
                "👤 Candidate Information"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Name:** {resume_info['name']}"
                )

                st.write(
                    f"**Email:** {resume_info['email']}"
                )

            with col2:

                st.write(
                    f"**Phone:** {resume_info['phone']}"
                )

            # =============================
            # Education
            # =============================

            st.subheader("🎓 Education")

            if resume_info["education"]:

                for item in resume_info["education"]:

                    st.write(
                        f"- {item}"
                    )

            else:

                st.info(
                    "Education information not detected."
                )

            # =============================
            # Projects
            # =============================

            st.subheader("📂 Projects")

            if resume_info["projects"]:

                for item in resume_info["projects"]:

                    st.write(
                        f"- {item}"
                    )

            else:

                st.info(
                    "Project information not detected."
                )

            # =============================
            # Experience
            # =============================

            st.subheader("💼 Experience")

            if resume_info["experience"]:

                for item in resume_info["experience"]:

                    st.write(
                        f"- {item}"
                    )

            else:

                st.info(
                    "Experience information not detected."
                )

            # =============================
            # Certifications
            # =============================

            st.subheader("📜 Certifications")

            if resume_info["certifications"]:

                for item in resume_info["certifications"]:

                    st.write(
                        f"- {item}"
                    )

            else:

                st.info(
                    "Certification information not detected."
                )

            # =============================
            # Extracted Resume Text
            # =============================

            with st.expander(
                "📄 View Extracted Resume Text"
            ):

                st.text_area(
                    "Resume",
                    resume_text,
                    height=300
                )