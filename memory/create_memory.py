import boto3
import time
from config.settings import MEMORY_NAME

control_client = boto3.client('bedrock-agentcore-control')

response = control_client.create_memory(
    name=MEMORY_NAME,
    description="Episodic memory for credit decisioning agent",
    eventExpiryDuration=90,
    memoryStrategies=[
        {
            'summaryMemoryStrategy': {
                'name': 'DecisionSummarizer',
                'namespaceTemplates': ['/decisions/{actorId}/{sessionId}/']
            }
        }
    ]
)

memory_id = response['memory']['id']

while True:
    status = control_client.get_memory(memoryId=memory_id)['memory']['status']
    if status == "ACTIVE":
        break
    time.sleep(5)

print("Memory ready:", memory_id)
