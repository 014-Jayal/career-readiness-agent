# AI Career Readiness & Skill Gap Agent

## Project Overview

The AI Career Readiness & Skill Gap Agent is an explainable, agentic
artificial intelligence system designed to assess employability
readiness for specific job roles. The project focuses on helping
students and early-career professionals understand how their current
skills align with job market requirements, identify missing
competencies, and plan targeted upskilling.

The system emphasizes transparency, explainability, and measurable
outcomes rather than black-box predictions or career guarantees. It is
aligned with Sustainable Development Goal (SDG) 8: Decent Work and
Economic Growth.

------------------------------------------------------------------------

## Problem Statement

Despite having formal education and technical exposure, many graduates
and early professionals struggle to understand why they are not
job-ready for specific roles. Existing career guidance platforms often
rely on static keyword matching or opaque AI models, providing generic
recommendations without clear reasoning. This lack of explainability
reduces user trust and leads to inefficient skill development paths.

------------------------------------------------------------------------

## Solution Description

This project proposes an explainable AI-based solution that evaluates
career readiness in a structured and transparent manner. The system: -
Accepts resume text in natural language format - Normalizes real-world
skill variations - Maps user skills to job-role requirements -
Calculates a quantified Career Readiness Score - Identifies existing and
missing skills - Generates a personalized, time-bound learning roadmap

The solution is designed as a multi-agent pipeline to ensure modularity
and clarity in reasoning.

------------------------------------------------------------------------

## System Architecture

The system follows an agentic architecture, where each agent performs a
dedicated task: 1. Resume Analyzer Agent: Extracts and normalizes skills
from free-text resume input 2. Skill Gap Identifier Agent: Compares
extracted skills with role-specific requirements 3. Market
Prioritization Agent: Assigns priority levels to missing skills 4.
Readiness Scoring Agent: Computes employability readiness using weighted
logic 5. Learning Roadmap Agent: Generates a structured learning plan
based on identified gaps

------------------------------------------------------------------------

## Technology Stack

Backend: - Python - FastAPI - LangGraph

Frontend: - Streamlit

Data: - Job role skill requirements - Skill priority mappings - Learning
duration estimations

------------------------------------------------------------------------

## Key Features

-   Free-text skill understanding without rigid forms
-   Skill normalization for real-world resume language
-   Explainable and transparent skill-to-role mapping
-   Career Readiness Score (0--100)
-   Clear visibility of existing and missing skills
-   Personalized learning roadmap

------------------------------------------------------------------------

## Sustainable Development Goal Alignment

This project supports SDG 8 by: - Reducing skill mismatch between
education and employment - Enabling informed and targeted upskilling -
Improving employability awareness and workforce readiness

------------------------------------------------------------------------

## Repository Structure

-   backend/: FastAPI backend and agent logic
-   frontend/: Streamlit user interface
-   docs/: Project documentation (Concept Note, Presentation, Lean
    Canvas)

------------------------------------------------------------------------

## How to Run the Project Locally

1.  Clone the repository
2.  Create and activate a virtual environment
3.  Install dependencies using requirements.txt
4.  Start the backend server using FastAPI
5.  Run the frontend using Streamlit

------------------------------------------------------------------------

## Ethical Considerations

-   No job or salary prediction
-   No career guarantees or advice
-   No use of sensitive personal data
-   Fully explainable and user-centric design

------------------------------------------------------------------------

## Future Enhancements

-   Support for additional job roles
-   Skill progress tracking
-   Institutional dashboards for placement cells
-   Integration with learning platforms

------------------------------------------------------------------------

## License

This project is developed for academic and educational purposes.
