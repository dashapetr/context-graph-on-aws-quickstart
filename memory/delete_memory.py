import boto3

client = boto3.client('bedrock-agentcore')

def delete_record(memory_id, record_id):
    response = client.delete_memory_record(
        memoryId=memory_id,
        memoryRecordId=record_id
    )
    print("Deleted:", response['memoryRecordId'])
