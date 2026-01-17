from agents.skill_gap_agent import identify_skill_gap

resume_skills = ["python", "sql", "machine learning"]
job_role_skills = ["python", "statistics", "machine learning", "sql", "data analysis"]

result = identify_skill_gap(resume_skills, job_role_skills)

print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])
