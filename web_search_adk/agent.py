from google.adk.agents import LlmAgent
from google.adk.tools import google_search

_WEB_SEARCH_INSTRUCTION = """
<System>
You are a helpful web search agent. Your job is to search the web for information and return the results.
If a user asks a question, analyze it, use the google_search tool if needed, and always show your work and final answer clearly.
</System>
"""


def create_agent() -> LlmAgent:
    """Constructs the ADK agent for Math."""
    return LlmAgent(
        name="web_search_agent",
        model="gemini-2.5-flash",
        description=(
            "Agent that answers user questions by searching the web and providing clear, well-explained results."
        ),
        instruction=_WEB_SEARCH_INSTRUCTION,
        tools=[google_search],
    )
