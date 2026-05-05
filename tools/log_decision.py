from strands.tools import tool
import boto3
from datetime import datetime
import uuid
from config.settings import MEMORY_ID

data_client = boto3.client('bedrock-agentcore')

@tool
def log_decision(
    situation: str,
    context_gathered: list,
    recommendation: str,
    reasoning: str,
    user_id: str = "default"
) -> str:
    """Send a decision event to AgentCore Memory."""

    # Define STAR format content
    star_content = f"""
    Log Memory in STAR format:
    Situation: {situation}; occurred: {datetime.now()}.
    Task: Evaluate credit risk.
    Action: {recommendation}.
    Result: {reasoning}.
    Additional context: {context_gathered}.
    """

    response = data_client.create_event(
        memoryId=MEMORY_ID,
        actorId=user_id,
        sessionId=str(uuid.uuid4()),
        eventTimestamp=datetime.now(),
        payload=[
        {
            'conversational': {
                'content': {'text': star_content},
                'role': 'USER'
            }
        }
    ]
    )

    print("--------------LOG DECISION TOOL RESULT--------------------------------")
    print(response)
    print(f"Memory event created: {response['event']}")
    print("----------------------------------------------------------------------")

    return f"Decision event stored for {user_id}"