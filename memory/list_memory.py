import boto3
from config.settings import MEMORY_ID

client = boto3.client('bedrock-agentcore')

response = client.list_memory_records(
    memoryId=MEMORY_ID,
    namespace='/decisions'
)

print(response)
