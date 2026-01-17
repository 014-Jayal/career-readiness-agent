# backend/agents/skill_gap_agent.py

from typing import List, Dict

def identify_skill_gap(
    resume_skills: List[str],
    role_skills: List[str]
) -> Dict[str, List[str]]:
    """
    Compares resume skills with job role skills
    and identifies missing skills.
    """

    resume_set = set(skill.lower() for skill in resume_skills)
    role_set = set(skill.lower() for skill in role_skills)

    missing_skills = list(role_set - resume_set)
    matched_skills = list(role_set & resume_set)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
