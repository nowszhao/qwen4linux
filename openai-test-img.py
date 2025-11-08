
import base64
import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-no-key-required"
)

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

image_base64 = encode_image("a.jpg")

completion = client.chat.completions.create(
    model="Qwen3-VL-2B-Instruct-GGUF",
    messages=[
        {"role": "system", "content": "You are ChatGPT, an AI assistant."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe what you see in this image."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }
    ]
)

print(completion.choices[0].message.content)

