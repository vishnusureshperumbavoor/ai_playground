from swarm import Swarm, Agent

client = Swarm()

def analyze_image(image_url):
    analyzed_data = {
        "description": "The image appears normal.",
        "image_url": image_url
    }
    return agent_b, analyzed_data

agent_a = Agent(
    name='Image Analyzer Agent',
    instructions='Analyze the provided radiology image.',
    functions=[analyze_image],
)

def find_anomalies(analyzed_data):
    if "normal" in analyzed_data["description"]:
        return "No anomalies detected."
    else:
        return "Anomalies detected."

agent_b = Agent(
    name='Anomaly Detector B',
    instructions='Find anomalies in the analyzed data.',
    functions=[find_anomalies],
)

user_message = {
    'role': 'user',
    'content': [
        {"type": "text", "text": "Can you find any abnormalities in this radiology image?"},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://patient.info/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxxv4b9mbhlgd%2Fimg_7326%2Fe78f4f9231fa4d7b1e872b426d515e2e%2F54d65006-315b-4500-b1a3-e9bb79743760.png&w=1600&q=75",
            },
        },
    ],
}

response_a = client.run(
    agent=agent_a,
    messages=[user_message],
)

analyzed_data = response_a.messages[-1]['content']

response_b = client.run(
    agent=agent_b,
    messages=[{'role': 'user', 'content': analyzed_data}],
)

print(response_b.messages[-1]['content'])
