from google.adk.agents import Agent
from google.adk.tools import google_search


def create_agent() -> Agent:
    return Agent(
        name="google_search_agent",
        model="gemini-2.5-flash",
        instruction="Answer questions using Google Search when needed. Always cite sources.",
        description="Professional search assistant with Google Search capabilities",
        tools=[google_search],
    )
