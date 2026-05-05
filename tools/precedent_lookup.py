from strands.tools import tool
import boto3
from config.settings import MEMORY_ID

data_client = boto3.client('bedrock-agentcore')

@tool
def precedent_lookup(query: str, user_id: str) -> str:
    """Search AgentCore Memory for past decisions.
    Important: user_id is lowercase "name <underscore> lastname", e.g. Tom Smith -> tom_smith"""

    response = data_client.retrieve_memory_records(
        memoryId=MEMORY_ID,
        namespacePath=f'/decisions/{user_id}',
        searchCriteria={
            'searchQuery': query,
            "topK": 5
        },
    )

    memories = response.get("memoryRecordSummaries", [])

    if not memories:
        return "No prior decisions found."

    all_memories = "\n---\n".join(
        mem.get("content", {}).get("text", "")
        for mem in memories
    )

    print("--------------PRECEDENT LOOKUP TOOL RESULT----------------------------")
    print(all_memories)
    print("----------------------------------------------------------------------")

    return all_memories
