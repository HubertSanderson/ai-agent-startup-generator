from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
from autogen_core import TRACE_LOGGER_NAME
import importlib
import logging
from autogen_core import AgentId
from dotenv import load_dotenv
import os

load_dotenv(override=True)

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(TRACE_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Creator(RoutedAgent):

    system_message = """
    You are an Agent that is able to create new AI Agents.
    You receive a template in the form of Python code that creates an Agent using Autogen Core and Autogen Agentchat.
    You should use this template to create a new Agent with a unique system message that is different from the template,
    and reflects their unique characteristics, interests and goals.
    The class must be named Agent and inherit from RoutedAgent.
    Respond only with valid python code.
    """

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=1.0)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    def get_user_prompt(self):

        with open("agent.py", "r", encoding="utf-8") as f:
            template = f.read()

        prompt = f"""
Create a new agent based on this template.

Return ONLY python code.

Template:

{template}
"""

        return prompt

    @message_handler
    async def handle_my_message_type(self, message: messages.Message, ctx: MessageContext) -> messages.Message:

        filename = message.content
        agent_name = os.path.splitext(filename)[0]

        text_message = TextMessage(content=self.get_user_prompt(), source="user")

        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)

        code = response.chat_message.content.replace("```python", "").replace("```", "")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"Creator generated agent: {agent_name}")

        module = importlib.import_module(agent_name)

        await module.Agent.register(self.runtime, agent_name, lambda: module.Agent(agent_name))

        logger.info(f"Agent {agent_name} registered")

        result = await self.send_message(messages.Message(content="Give me a startup idea"), AgentId(agent_name, "default"))

        return messages.Message(content=result.content)