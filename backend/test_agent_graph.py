from graph.agent_graph import build_graph

graph = build_graph()

input_data = {
    "resume_text": """
    I am a Computer Science student.
    I know Python, SQL, Machine Learning, Git, Docker.
    """,
    "target_role": "data_scientist"
}

result = graph.invoke(input_data)

print("\nFINAL OUTPUT:\n")
print(result["learning_roadmap"])
