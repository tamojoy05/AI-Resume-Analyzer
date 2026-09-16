import re


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else "Not found"


def extract_phone(text):
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group() if match else "Not found"


def extract_name(text):
    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    for line in lines[:10]:

        line_lower = line.lower()

        if line_lower in [
            "resume",
            "curriculum vitae",
            "cv",
            "resume cv"
        ]:
            continue

        if "@" in line:
            continue

        if any(char.isdigit() for char in line):
            continue

        if len(line.split()) <= 5:
            return line

    return "Not found"


def extract_section(text, start_keywords, stop_keywords):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    section_data = []
    inside_section = False

    for line in lines:

        # Clean the line only for comparison
        clean_line = line.lower()

        # Remove markdown-style links
        clean_line = re.sub(
            r"\[.*?\]\(.*?\)",
            "",
            clean_line
        )

        # Remove special characters
        clean_line = re.sub(
            r"[^a-z\s&]",
            " ",
            clean_line
        )

        # Remove extra spaces
        clean_line = re.sub(
            r"\s+",
            " ",
            clean_line
        ).strip()

        # Check for section heading
        if clean_line in start_keywords:
            inside_section = True
            continue

        # Check for next section
        if inside_section:
            if clean_line in stop_keywords:
                break

            section_data.append(line)

    return section_data


def extract_education(text):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    education = []
    inside_education = False

    for line in lines:

        clean_line = line.lower().strip()

        # Remove markdown/link formatting
        clean_line = re.sub(
            r"\[.*?\]\(.*?\)",
            "",
            clean_line
        )

        # Remove extra spaces
        clean_line = re.sub(
            r"\s+",
            " ",
            clean_line
        ).strip()

        # Start Education section
        if clean_line == "education":
            inside_education = True
            continue

        # Stop at the next major section
        if inside_education and clean_line in [
            "projects",
            "professional experience",
            "experience",
            "technical skills",
            "skills",
            "certifications",
            "achievements",
            "awards"
        ]:
            break

        if inside_education:
            education.append(line)

    return education

def extract_projects(text):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    projects = []
    inside_projects = False

    for line in lines:

        clean_line = line.lower().strip()

        # Remove markdown-style links
        clean_line = re.sub(
            r"\[.*?\]\(.*?\)",
            "",
            clean_line
        )

        # Normalize spaces
        clean_line = re.sub(
            r"\s+",
            " ",
            clean_line
        ).strip()

        # Start Projects section
        if clean_line == "projects":
            inside_projects = True
            continue

        # Stop at Professional Experience
        if inside_projects and clean_line == "professional experience":
            break

        # Stop at other major sections
        if inside_projects and clean_line in [
            "achievements",
            "education",
            "certifications"
        ]:
            break

        if inside_projects:
            projects.append(line)

    return projects


def extract_experience(text):
    start_keywords = [
        "experience",
        "work experience",
        "professional experience",
        "internship",
        "internships"
    ]

    stop_keywords = [
        "education",
        "projects",
        "skills",
        "certifications",
        "achievements"
    ]

    return extract_section(
        text,
        start_keywords,
        stop_keywords
    )


def extract_certifications(text):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    certifications = []
    inside_certifications = False

    for line in lines:

        clean_line = line.lower().strip()

        # Remove markdown-style links
        clean_line = re.sub(
            r"\[.*?\]\(.*?\)",
            "",
            clean_line
        )

        # Normalize spaces
        clean_line = re.sub(
            r"\s+",
            " ",
            clean_line
        ).strip()

        # Start Certifications section
        if clean_line in [
            "certifications",
            "certificates",
            "certification"
        ]:
            inside_certifications = True
            continue

        # If there is no separate Certifications section,
        # check the Achievements section for certificate-related lines
        if clean_line == "achievements":
            inside_certifications = True
            continue

        if inside_certifications:

            if clean_line in [
                "education",
                "projects",
                "professional experience",
                "experience",
                "technical skills",
                "skills"
            ]:
                break

            # Keep only certificate-related achievement lines
            if any(keyword in clean_line for keyword in [
                "certificate",
                "certification",
                "certified"
            ]):
                certifications.append(line)

    return certifications


def extract_resume_info(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "education": extract_education(text),
        "projects": extract_projects(text),
        "experience": extract_experience(text),
        "certifications": extract_certifications(text)
    }