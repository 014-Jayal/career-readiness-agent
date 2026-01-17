# backend/agents/readiness_agent.py

from typing import Dict, List

def calculate_readiness_score(
    matched_skills: List[str],
    role_priority: Dict[str, List[str]]
) -> int:
    """
    Calculates a readiness score (0–100) based on weighted skill match.
    """

    total_score = 0
    max_score = 0

    for priority, skills in role_priority.items():
        if priority == "high":
            weight = 3
        elif priority == "medium":
            weight = 2
        else:
            weight = 1

        for skill in skills:
            max_score += weight
            if skill in matched_skills:
                total_score += weight

    if max_score == 0:
        return 0

    readiness_percentage = int((total_score / max_score) * 100)
    return readiness_percentage
