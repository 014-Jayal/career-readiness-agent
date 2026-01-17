from agents.readiness_agent import calculate_readiness_score

matched_skills = ["python", "machine learning", "sql"]

role_priority = {
    "high": ["python", "machine learning", "statistics"],
    "medium": ["sql", "data analysis"],
    "low": ["git", "docker"]
}

score = calculate_readiness_score(matched_skills, role_priority)
print("Career Readiness Score:", score)
