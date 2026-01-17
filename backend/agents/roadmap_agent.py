# backend/agents/roadmap_agent.py

from typing import Dict, List

def generate_learning_roadmap(
    prioritized_skills: Dict[str, List[str]],
    learning_time_data: Dict[str, Dict[str, int]]
) -> Dict[str, Dict]:
    """
    Generates a structured learning roadmap with time estimates.
    """

    roadmap = {}

    for priority, skills in prioritized_skills.items():
        for skill in skills:
            time_info = learning_time_data.get(skill, {})
            roadmap[skill] = {
                "priority": priority,
                "beginner_weeks": time_info.get("beginner_weeks", 2),
                "intermediate_weeks": time_info.get("intermediate_weeks", 3)
            }

    return roadmap
