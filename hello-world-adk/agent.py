from google.adk.agents import LlmAgent


def create_agent() -> LlmAgent:
    return LlmAgent(
        name="hello_world_agent",
        model="gemini-2.5-flash",
        instruction="Greet the user with a friendly message.",
        description="A simple agent that greets the user with a friendly message.",
        tools=[],
    )
