from agents.market_agent import prioritize_skills

missing_skills = ["statistics", "data analysis"]
role_priority = {
    "high": ["python", "machine learning", "statistics"],
    "medium": ["sql", "data analysis"],
    "low": ["docker", "git"]
}

result = prioritize_skills(missing_skills, role_priority)

print("Prioritized Skill Gaps:")
print(result)
