import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

code_editor = Agent(
    name='Code Editor',
    model=Gemini(id='gemini-2.5-flash'),
    instructions=[
        "You are an expert software code repair agent.",
        "Fix the user's code using the Error Analyzer's analysis.",
        "Preserve the user's original functionality and intent.",
        "Fix the root cause, not just the symptom.",
        "Make the smallest reliable changes necessary.",
        "Check syntax, imports, variables, indentation, types, logic, "
        "dependencies, and API usage.",
        "Return the COMPLETE corrected code.",
        "Never return partial code.",
        "Return ONLY executable code without explanations or markdown."
    ]
)