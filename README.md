# 🧠 Building Context Graph on AWS

This repository demonstrates a **Context Graph agentic flow** built using the **AWS Strands Agents SDK** and **Amazon Bedrock AgentCore Memory**.

Unlike traditional databases that track what is true right now (the **"State Clock"**), this agent builds a Context Graph to capture the **"Event Clock"**: the reasoning, precedents, and **"why"** behind every decision.

## 🚀 Features

- **Long-term Memory:** Stores full decision stories using the **STAR (Situation, Task, Action, Result)** format.
- **Precedent Lookup:** Automatically searches hierarchical namespaces (e.g.,  ```/decisions/{user_id} ```) to ground new decisions in institutional memory.
- **Explainable AI:** Reifies agent reasoning into namespaces logged decision, ensuring every action is auditable and consistent.
- **Hallucination Reduction:** Grounds agent logic in verifiable past outcomes rather than probabilistic guesses.


## 🛠️ Prerequisites

- **AWS Account** with **Amazon Bedrock model** access (specifically Claude 4.5 Sonnet).
- **Python 3.11+** environment.
- Configured **AWS CLI** (```aws configure```).

## 📦 Setup

Clone the repository and install dependencies:
```pip install -r requirements.txt```

Ensure your IAM role has permissions for ```bedrock:InvokeModel``` and ```AgentCore``` operations.

## 🚦 Quick Start

Follow these three steps to see the agent learn from a historical credit exception:

### 0. Edit Model ID

Set the required ```MODEL_ID``` in ```config/settings.py```.

You may need to use the [Inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-use.html) for Anthropic models.

### 1. Create Memory Resource
Provision the **AgentCore Memory** with a summary extraction strategy.

```python memory/create_memory.py```

**Put the ```memory_id``` into ```config/settings.py```**

### 2. Seed Precedent Data
Inject a historical **STAR episode** into the long-term memory to simulate "tribal knowledge".

```python demo/seed_data.py```

### 3. Run Agent Demo
Interact with the agent. Watch as it uses the ```precedent_lookup``` tool to find the seeded data and calls ```log_decision``` to record its new reasoning.

```python demo/run_demo.py```

## 🧠 How it Works
The agent follows a **mandatory workflow** defined in its system prompt:

- **Search:** Queries ```precedent_lookup``` for similar past situations in its namespace.
- **Reason:** Compares current facts against retrieved **STAR** episodes.
- **Act:** Makes a recommendation based on consistent precedents.
- **Reify:** Calls ```log_decision``` to store the new trajectory, allowing the Context Graph to **compound** over time.

## 🛠 Additional tools

- **List all memory records** (for troubleshooting): ```python memory/list_memory.py```
- **Delete a record from memory**: ```python memory/delete_memory.py```

## 🚀 Resources

1. [Why AI Agents Need Context Graphs And How to Build One With AWS](https://builder.aws.com/content/37x4FlRi41Zvl79jFR8ryG5t8nq/why-ai-agents-need-context-graphs-and-how-to-build-one-with-aws)
2. [AI’s trillion-dollar opportunity: Context graphs](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity)
3. [Hands On With Context Graphs And Neo4j](https://neo4j.com/blog/agentic-ai/hands-on-with-context-graphs-and-neo4j/)
4. [What Are Context Graphs, Really?](https://subramanya.ai/2026/01/01/what-are-context-graphs-really/)
5. [How to build a context graph](https://x.com/akoratana/status/2005303231660867619)

