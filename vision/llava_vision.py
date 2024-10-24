from groq import Groq

client = Groq()

image_url = "https://patient.info/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxxv4b9mbhlgd%2Fimg_7326%2Fe78f4f9231fa4d7b1e872b426d515e2e%2F54d65006-315b-4500-b1a3-e9bb79743760.png&w=1600&q=75"

try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        model="llava-v1.5-7b-4096-preview",
    )

    print(chat_completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
