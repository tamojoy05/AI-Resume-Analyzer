def generate_recommendations(
    resume_text,
    job_description,
    matching_skills,
    missing_skills,
    resume_info
):
    recommendations = []

    # Missing skills
    if missing_skills:

        recommendations.append(
            "Consider learning or highlighting these "
            "job-relevant skills: "
            + ", ".join(
                skill.title()
                for skill in missing_skills
            )
            + "."
        )

    # Projects
    if not resume_info["projects"]:

        recommendations.append(
            "Add relevant academic or personal "
            "projects to demonstrate practical experience."
        )

    # Experience
    if not resume_info["experience"]:

        recommendations.append(
            "If you have internships, training, freelance "
            "work, or relevant experience, consider adding "
            "them to your resume."
        )

    # Certifications
    if not resume_info["certifications"]:

        recommendations.append(
            "Consider adding relevant certifications, "
            "courses, or training you have completed."
        )

    # Email
    if resume_info["email"] == "Not found":

        recommendations.append(
            "Add a professional email address to your resume."
        )

    # Phone
    if resume_info["phone"] == "Not found":

        recommendations.append(
            "Add a contact phone number if appropriate."
        )

    # Matching skills
    if matching_skills:

        recommendations.append(
            "Make sure your strongest job-relevant skills "
            "are clearly visible in your Skills section."
        )

    # General recommendation
    recommendations.append(
        "Tailor your resume wording to the specific "
        "job description while keeping all information "
        "accurate and truthful."
    )

    return recommendations