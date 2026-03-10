# ai-agent-startup-generator
This project demonstrates a self-expanding multi-agent AI system built using Microsoft's AutoGen framework.
The system starts with a single agent that has the ability to generate entirely new AI agents as Python code. These newly created agents are dynamically loaded, registered in the runtime, and asked to generate startup ideas.
Each agent represents a different entrepreneurial personality, with unique goals, interests, and perspectives. Some agents may also collaborate with other agents by asking them to refine or improve their ideas.
The result is a small ecosystem of AI agents that create, refine, and evolve startup ideas autonomously.
How It Works
A Creator Agent receives a template for an AI agent.
It generates new Python code for a unique agent using a language model.
The new agent is saved, imported, and registered at runtime.
The agent is asked to generate a startup idea.
The idea may optionally be sent to another agent for refinement.
The final idea is saved to a markdown file.
This process can generate many agents and startup ideas automatically.
Key Features
Dynamic AI agent creation
Runtime agent registration
Multi-agent collaboration
Startup idea generation using LLMs
Autonomous idea refinement
Asynchronous multi-agent execution
Technologies Used
Python
AutoGen Core
AutoGen AgentChat
OpenAI language models
AsyncIO
gRPC runtime
Example Output
The system automatically generates files like:
idea1.md
idea2.md
idea3.md
Each file contains a startup idea generated and possibly refined by AI agents.
Purpose
This project demonstrates advanced agentic AI patterns, including:
autonomous agent generation
multi-agent collaboration
AI-driven code generation
dynamic system expansion
It serves as an experimental prototype showing how AI agents can create and interact with other AI agents to explore creative problem solving.
Running the Project
Install dependencies:
pip install -r requirements.txt
Create a .env file:
OPENAI_API_KEY=your_api_key_here
Run the system:
python main.py
