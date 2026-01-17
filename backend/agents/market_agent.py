# backend/agents/market_agent.py

from typing import List, Dict

def prioritize_skills(
    missing_skills: List[str],
    role_priority: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    """
    Prioritizes missing skills based on role importance.
    """

    prioritized = {
        "high_priority": [],
        "medium_priority": [],
        "low_priority": []
    }

    for skill in missing_skills:
        if skill in role_priority.get("high", []):
            prioritized["high_priority"].append(skill)
        elif skill in role_priority.get("medium", []):
            prioritized["medium_priority"].append(skill)
        else:
            prioritized["low_priority"].append(skill)

    return prioritized
