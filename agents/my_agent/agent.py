from google.adk.agents.config_agent_utils import load_agent_from_config
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import asyncio
from pathlib import Path

# CONFIGURATION
APP_NAME = "simple_search_agent"
USER_ID = "user_default"
SESSION_ID = "session_01"

# AGENT DEFINITION - Load from YAML using ADK's built-in method
yaml_path = Path(__file__).parent / 'root_agent.yaml'
root_agent = load_agent_from_config(str(yaml_path))


# Session and Runner
async def setup_session_and_runner():
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    runner = Runner(
        agent=root_agent, app_name=APP_NAME, session_service=session_service
    )
    return session, runner


# Agent Interaction
async def call_agent_async(query):
    content = types.Content(role="user", parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(
        user_id=USER_ID, session_id=SESSION_ID, new_message=content
    )

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)


if __name__ == "__main__":
    asyncio.run(call_agent_async("what's the latest ai news?"))
