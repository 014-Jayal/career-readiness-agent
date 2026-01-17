from agents.roadmap_agent import generate_learning_roadmap

prioritized_skills = {
    "high_priority": ["statistics"],
    "medium_priority": ["data analysis"],
    "low_priority": []
}

learning_time_data = {
    "statistics": {
        "beginner_weeks": 4,
        "intermediate_weeks": 6
    },
    "data analysis": {
        "beginner_weeks": 3,
        "intermediate_weeks": 4
    }
}

roadmap = generate_learning_roadmap(prioritized_skills, learning_time_data)
print("Learning Roadmap:")
print(roadmap)
