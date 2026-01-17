from agents.resume_agent import extract_skills

sample_resume = """
I am a Computer Science student.
I have experience in Python, SQL, Machine Learning, and FastAPI.
I have also worked with Git and Docker.
"""

skills = extract_skills(sample_resume)
print("Extracted Skills:", skills)
