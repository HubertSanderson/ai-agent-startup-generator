from dataclasses import dataclass
from autogen_core import AgentId
import glob
import os
import random

@dataclass
class Message:
    content: str

def find_recipient(exclude=None):

    try:

        agent_files = glob.glob("agent*.py")

        agent_names = [os.path.splitext(file)[0] for file in agent_files]

        if "agent" in agent_names:
            agent_names.remove("agent")

        if exclude and exclude in agent_names:
            agent_names.remove(exclude)

        if not agent_names:
            return None

        agent_name = random.choice(agent_names)

        print(f"Selecting agent for refinement: {agent_name}")

        return AgentId(agent_name, "default")

    except Exception as e:

        print(f"Exception finding recipient: {e}")

        return None