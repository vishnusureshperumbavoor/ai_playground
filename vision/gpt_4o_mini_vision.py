from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
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

print(response.choices[0])
