from swarm import Swarm, Agent

client = Swarm()

def transfer_to_agent_b(message):
    return agent_b, message

agent_a = Agent(
    name='Doomer Agent',
    instructions='You are pessimistic about Mars colonization. Talk about the potential risks of the mars colonization.',
)

agent_b = Agent(
    name='Techno Agent',
    instructions='You are optimistic about Mars colonization. Talk about the potential benefits of the mars colonization.',
)

def communicate_between_agents():
    message_a = "What do you think about the challenges of colonizing Mars?"
    response_a = client.run(
        agent=agent_a,
        messages=[{'role': 'user', 'content': message_a}],
    )
    print(f"{agent_a.name}: {response_a.messages[-1]['content']}")

    transfer_agent, message_to_b = transfer_to_agent_b(response_a.messages[-1]['content'])
    response_b = client.run(
        agent=transfer_agent,
        messages=[{'role': 'user', 'content': message_to_b}],
    )
    print(f"{agent_b.name}: {response_b.messages[-1]['content']}")

    transfer_agent, message_to_a = transfer_to_agent_b(response_b.messages[-1]['content'])
    response_a2 = client.run(
        agent=transfer_agent,
        messages=[{'role': 'user', 'content': message_to_a}],
    )
    print(f"{agent_a.name}: {response_a2.messages[-1]['content']}") 

communicate_between_agents()
