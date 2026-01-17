# backend/agents/resume_agent.py

from typing import List
import re

# Canonical skill vocabulary
SKILL_VOCAB = [
    "python",
    "sql",
    "machine learning",
    "statistics",
    "data analysis",
    "react",
    "javascript",
    "html",
    "css",
    "fastapi",
    "git",
    "docker"
]

# Skill aliases (VERY IMPORTANT)
SKILL_ALIASES = {
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "data analytics": "data analysis",
    "stats": "statistics",
}

def normalize_text(text: str) -> str:
    text = text.lower()
    for alias, canonical in SKILL_ALIASES.items():
        text = re.sub(r"\b" + re.escape(alias) + r"\b", canonical, text)
    return text

def extract_skills(resume_text: str) -> List[str]:
    """
    Extracts and normalizes skills from resume text.
    """

    resume_text = normalize_text(resume_text)
    found_skills = []

    for skill in SKILL_VOCAB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            found_skills.append(skill)

    return list(set(found_skills))
