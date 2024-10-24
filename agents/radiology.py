from swarm import Swarm, Agent
from openai import OpenAI

gpt_client = OpenAI()
swarm_client = Swarm()

def transfer_to_agent_b(message):
    return agent_b, message

agent_a = Agent(
    name='Body part detection agent',
    instructions='From the response find which human body part is this radiology image.',
)

agent_b = Agent(
    name='Anomaly detection agent',
    instructions='From the response find if there is any anomaly in this radiology image.',
)

try:
    response = gpt_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://patient.info/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxxv4b9mbhlgd%2Fimg_7326%2Fe78f4f9231fa4d7b1e872b426d515e2e%2F54d65006-315b-4500-b1a3-e9bb79743760.png&w=1600&q=75",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    print("GPT Analysis:", response.choices[0].message.content)
    print()

    message_a = response.choices[0].message.content
    response_a = swarm_client.run(
        agent=agent_a,
        messages=[{'role': 'user', 'content': message_a}],
    )
    
    print(f"{agent_a.name}: {response_a.messages[-1]['content']}")
    print()

    transfer_agent, message_to_b = transfer_to_agent_b(response_a.messages[-1]['content'])
    response_b = swarm_client.run(
        agent=transfer_agent,
        messages=[{'role': 'user', 'content': message_to_b}],
    )
    
    print(f"{agent_b.name}: {response_b.messages[-1]['content']}")

except Exception as e:
    print(f"An error occurred: {e}")
