from agent.agent import agent

if __name__ == "__main__":
    prompt = "Should we approve a $35,000 credit increase for Tim Chang?"
    print(f"User: {prompt}\n")
    response = agent(prompt)
    print(f"Agent: {response}")
