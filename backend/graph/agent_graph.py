# backend/graph/agent_graph.py

import json
from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph

from backend.agents.resume_agent import extract_skills
from backend.agents.skill_gap_agent import identify_skill_gap
from backend.agents.market_agent import prioritize_skills
from backend.agents.roadmap_agent import generate_learning_roadmap
from backend.agents.readiness_agent import calculate_readiness_score


# -------------------------
# State Definition
# -------------------------
class CareerState(TypedDict, total=False):
    resume_text: str
    target_role: str
    resume_skills: List[str]
    skill_gap: Dict
    prioritized_skills: Dict
    learning_roadmap: Dict
    readiness_score: int


# -------------------------
# Load Static Data
# -------------------------
with open("backend/data/job_roles.json") as f:
    JOB_ROLES = json.load(f)

with open("backend/data/skill_priority.json") as f:
    SKILL_PRIORITY = json.load(f)

with open("backend/data/learning_time.json") as f:
    LEARNING_TIME = json.load(f)


# -------------------------
# Agent Nodes
# -------------------------
def resume_node(state: CareerState):
    skills = extract_skills(state.get("resume_text", ""))
    return {
        **state,
        "resume_skills": skills
    }


def skill_gap_node(state: CareerState):
    role = state["target_role"]
    role_skills = JOB_ROLES[role]["required_skills"]

    gap = identify_skill_gap(
        state["resume_skills"],
        role_skills
    )

    return {
        **state,
        "skill_gap": gap
    }


def market_node(state: CareerState):
    role = state["target_role"]
    missing = state["skill_gap"]["missing_skills"]

    priority = prioritize_skills(
        missing,
        SKILL_PRIORITY.get(role, {})
    )

    return {
        **state,
        "prioritized_skills": priority
    }


def roadmap_node(state: CareerState):
    roadmap = generate_learning_roadmap(
        state["prioritized_skills"],
        LEARNING_TIME
    )

    return {
        **state,
        "learning_roadmap": roadmap
    }


def readiness_node(state: CareerState):
    role = state["target_role"]
    matched_skills = state["skill_gap"]["matched_skills"]

    role_priority = SKILL_PRIORITY.get(role, {})

    score = calculate_readiness_score(
        matched_skills,
        role_priority
    )

    return {
        **state,
        "readiness_score": score
    }


# -------------------------
# Build LangGraph
# -------------------------
def build_graph():
    graph = StateGraph(CareerState)

    graph.add_node("resume", resume_node)
    graph.add_node("skill_gap", skill_gap_node)
    graph.add_node("market", market_node)
    graph.add_node("roadmap", roadmap_node)
    graph.add_node("readiness", readiness_node)

    graph.set_entry_point("resume")

    graph.add_edge("resume", "skill_gap")
    graph.add_edge("skill_gap", "market")
    graph.add_edge("market", "roadmap")
    graph.add_edge("roadmap", "readiness")

    graph.set_finish_point("readiness")

    return graph.compile()
