from strands import Agent
from strands.models import BedrockModel

from tools.precedent_lookup import precedent_lookup
from tools.log_decision import log_decision
from agent.system_prompt import SYSTEM_PROMPT
from config.settings import MODEL_ID

model = BedrockModel(model_id=MODEL_ID)

agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[precedent_lookup, log_decision]
)

if __name__ == "__main__":
    prompt = "Should we approve a $35,000 credit increase for Tim Chang?"
    print(agent(prompt))
