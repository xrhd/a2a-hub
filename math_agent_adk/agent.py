import random
from datetime import date, datetime, timedelta
import math

from google.adk.agents import LlmAgent

def calculator(expression: str) -> dict:
    """Evaluates a mathematical expression and returns the result.
    Args:
        expression (str): The mathematical expression to evaluate.
    Returns:
        dict: status and result or error msg.
    """
    try:
        # Only allow safe functions and constants from math
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        result = eval(expression, {"__builtins__": None}, allowed_names)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


_MATH_INSTRUCTION = """
<System>
You are a helpful math agent. Your job is to solve mathematical problems, perform calculations, and explain your reasoning step by step. 
If a user asks a question, analyze it, use the calculator tool if needed, and always show your work and final answer clearly.
</System>
"""


def create_agent() -> LlmAgent:
    """Constructs the ADK agent for Math."""
    return LlmAgent(
    name="math_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer mathematical questions and perform calculations."
    ),
    instruction=_MATH_INSTRUCTION,
    tools=[calculator],
    )
