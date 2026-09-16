import re


SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "r",

    # AI / Machine Learning
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "large language models",
    "llm",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "keras",

    # Data
    "data analysis",
    "data science",
    "data visualization",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "power bi",
    "tableau",
    "excel",

    # Development
    "html",
    "css",
    "react",
    "node.js",
    "flask",
    "django",
    "streamlit",
    "rest api",

    # Databases
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",

    # Tools / Cloud
    "git",
    "github",
    "docker",
    "aws",
    "google cloud",
    "linux",

    # Core CS
    "data structures",
    "algorithms",
    "object-oriented programming",
    "oop",
    "problem solving",
    "computer networks",
    "operating systems",
    "dbms",
]


SKILL_ALIASES = {
    "nlp": "natural language processing",
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dsa": "data structures",
    "oop": "object-oriented programming",
    "llm": "large language models",
}


def extract_skills(text):
    """
    Extract known skills from text and normalize aliases.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):

            # Convert alias to its standard skill name
            normalized_skill = SKILL_ALIASES.get(
                skill,
                skill
            )

            found_skills.append(normalized_skill)

    return sorted(set(found_skills))


def compare_skills(resume_text, job_description):
    """
    Compare resume skills with skills required by the job.
    """

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )

    matching_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills - resume_skills
    )

    return matching_skills, missing_skills

def extract_keywords(text):
    """
    Extract meaningful ATS keywords and phrases.
    """

    text = text.lower()

    # Important multi-word phrases
    phrases = [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "natural language processing",
        "generative ai",
        "large language models",
        "data analysis",
        "data science",
        "data visualization",
        "data structures",
        "object oriented programming",
        "problem solving",
        "critical thinking",
        "computer networks",
        "operating systems",
        "database management systems",
        "rest api",
        "team leadership",
        "team management",
        "project management",
        "software development",
        "web development",
        "cloud computing",
        "version control"
    ]

    keywords = set()

    # First detect meaningful phrases
    for phrase in phrases:
        if phrase in text:
            keywords.add(phrase)

    # Then extract useful single words
    words = re.findall(
        r"\b[a-zA-Z][a-zA-Z+#.-]{2,}\b",
        text
    )

    stop_words = {
        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "from",
        "are",
        "you",
        "your",
        "our",
        "have",
        "has",
        "will",
        "can",
        "job",
        "work",
        "role",
        "years",
        "experience",
        "responsibilities",
        "requirements",
        "candidate",
        "looking",
        "including",
        "using",
        "strong",
        "good",
        "ability",
        "skills"
    }

    for word in words:

        if word not in stop_words:
            keywords.add(word)

    return sorted(keywords)


def compare_keywords(resume_text, job_description):

    resume_keywords = set(
        extract_keywords(resume_text)
    )

    job_keywords = set(
        extract_keywords(job_description)
    )

    matching_keywords = sorted(
        resume_keywords.intersection(job_keywords)
    )

    missing_keywords = sorted(
        job_keywords - resume_keywords
    )

    if job_keywords:
        keyword_match_score = round(
            (
                len(matching_keywords)
                / len(job_keywords)
            ) * 100,
            2
        )
    else:
        keyword_match_score = 0

    return (
        matching_keywords,
        missing_keywords,
        keyword_match_score
    )